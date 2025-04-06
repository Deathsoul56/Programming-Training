import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cambia el directorio de trabajo al directorio donde se ejecuta el script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# CONFIGURACIÓN INICIAL
# =============================================================================

# Configurar pandas para mostrar los datos justificados a la izquierda
pd.set_option('display.colheader_justify', 'left')
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# Configuración de estilo para todos los gráficos
sns.set_palette("pastel")
plt.rcParams['font.size'] = 12
COLORES = [
    "#ff9f1c",  # naranja suave
    "#6324b5",  # púrpura base
    "#f24e1e",  # naranja brillante (complementario)
    "#1ecbe1",  # celeste vibrante
    "#f2c94c",  # amarillo dorado
    "#27ae60",  # verde medio
    "#eb5757",  # rojo fuerte
    "#9b51e0",  # lila intenso (parecido al base pero más claro)
    "#2d9cdb",  # azul cielo
    "#6fcf97"  # verde suave
]


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def print_left_aligned(dataframe):
    """
    Función personalizada para mostrar el DataFrame con formato justificado a la izquierda

    Args:
        dataframe: DataFrame a mostrar
    """
    # Determinar el ancho máximo para cada columna
    col_widths = {}
    for col in dataframe.columns:
        # Ancho del nombre de la columna
        col_width = len(str(col))
        # Ancho máximo de los valores en la columna
        data_width = dataframe[col].astype(str).map(len).max()
        # Usar el ancho mayor más un pequeño padding
        col_widths[col] = max(col_width, data_width) + 2

    # Imprimir encabezados
    header = ""
    for col in dataframe.columns:
        header += str(col).ljust(col_widths[col])
    print(header)
    print("-" * sum(col_widths.values()))

    # Imprimir filas
    for _, row in dataframe.iterrows():
        row_str = ""
        for col in dataframe.columns:
            row_str += str(row[col]).ljust(col_widths[col])
        print(row_str)


def calcular_estadisticas_por_responsable(df, total_cuenta, total_con_propina):
    """
    Calcula estadísticas por responsable

    Args:
        df: DataFrame con los datos
        total_cuenta: Total de la cuenta sin propina
        total_con_propina: Total de la cuenta con propina

    Returns:
        DataFrame con estadísticas por responsable
    """
    # Crear un DataFrame para estadísticas
    stats = []

    # Para cada fila en el DataFrame original
    for _, row in df.iterrows():
        # Obtener la lista de responsables
        resp_list = json.loads(row['Responsables_JSON'])
        # Si no hay responsables, omitir
        if not resp_list:
            continue

        # Calcular el monto por persona (sin redondear aún)
        monto_por_persona = row['Total'] / len(resp_list)

        # Asignar el monto a cada responsable
        for resp in resp_list:
            stats.append({
                'Responsable': resp,
                'Producto': row['Producto'],
                'Monto_Asignado': monto_por_persona,
                'Monto_con_propina': monto_por_persona * 1.1,
                'Personas_Compartiendo': len(resp_list)
            })

    # Convertir a DataFrame
    stats_df = pd.DataFrame(stats)

    # Crear resumen por responsable
    resumen = stats_df.groupby('Responsable').agg({
        'Monto_Asignado': 'sum',
        'Monto_con_propina': 'sum',
        'Producto': 'count'
    }).reset_index()

    resumen.columns = ['Responsable', 'Total_Gastado', 'Total_con_Propina', 'Cantidad_Items']
    resumen['Porcentaje_Cuenta'] = (resumen['Total_Gastado'] / total_cuenta * 100).round(2)

    # Redondear los totales a valores enteros
    resumen['Total_Gastado'] = resumen['Total_Gastado'].round().astype(int)
    resumen['Total_con_Propina'] = resumen['Total_con_Propina'].round().astype(int)

    # Ordenar por Total_Gastado (descendente)
    resumen = resumen.sort_values(by='Total_Gastado', ascending=False)

    # Agregar fila de TOTALES
    total_row = pd.DataFrame({
        'Responsable': ['TOTAL'],
        'Total_Gastado': [resumen['Total_Gastado'].sum()],
        'Total_con_Propina': [resumen['Total_con_Propina'].sum()],
        'Cantidad_Items': [resumen['Cantidad_Items'].sum()],
        'Porcentaje_Cuenta': [100.0]  # El total siempre representa el 100%
    })

    # Concatenar el resumen con la fila de totales
    resumen_con_totales = pd.concat([resumen, total_row], ignore_index=True)

    return resumen_con_totales


def generar_tablas_detalle(df, stats_responsables):
    """
    Genera tablas de detalle con productos y precios por responsable

    Args:
        df: DataFrame con los datos
        stats_responsables: DataFrame con estadísticas por responsable

    Returns:
        Tuple de (tabla_productos, tabla_precios)
    """
    # Primero determinamos el máximo número de items que tiene cualquier responsable
    max_items = 0
    items_por_responsable = {}

    for responsable in stats_responsables[:-1]['Responsable']:
        items = []
        for _, row in df.iterrows():
            responsables = json.loads(row['Responsables_JSON'])
            if responsable in responsables:
                items.append({
                    'producto': row['Producto'],
                    'precio': row['Total'] * 1.1 / len(responsables)  # Precio con propina
                })
        items_por_responsable[responsable] = items
        max_items = max(max_items, len(items))

    # Crear DataFrames con columnas dinámicas
    columnas_productos = ['Responsable'] + [f'Item_{i + 1}' for i in range(max_items)]
    columnas_precios = ['Responsable'] + [f'Precio_{i + 1}' for i in range(max_items)] + [
        'Subtotal', 'Propina (10%)', 'Total a Pagar'
    ]

    tabla_productos = pd.DataFrame(columns=columnas_productos)
    tabla_precios = pd.DataFrame(columns=columnas_precios)

    # Llenar las tablas
    for responsable, items in items_por_responsable.items():
        fila_productos = {'Responsable': responsable}
        fila_precios = {'Responsable': responsable}
        subtotal = 0

        for i in range(max_items):
            if i < len(items):
                fila_productos[f'Item_{i + 1}'] = items[i]['producto']
                precio = items[i]['precio']
                fila_precios[f'Precio_{i + 1}'] = f"${round(precio)}"
                subtotal += precio / 1.1  # Precio sin propina
            else:
                fila_productos[f'Item_{i + 1}'] = ''
                fila_precios[f'Precio_{i + 1}'] = ''

        # Calcular columnas adicionales
        propina = subtotal * 0.1
        total = subtotal + propina
        fila_precios['Subtotal'] = f"${round(subtotal)}"
        fila_precios['Propina (10%)'] = f"${round(propina)}"
        fila_precios['Total a Pagar'] = f"${round(total)}"

        tabla_productos = pd.concat([tabla_productos, pd.DataFrame([fila_productos])], ignore_index=True)
        tabla_precios = pd.concat([tabla_precios, pd.DataFrame([fila_precios])], ignore_index=True)

    return tabla_productos, tabla_precios


# =============================================================================
# FUNCIONES DE VISUALIZACIÓN
# =============================================================================

def grafico_barras(stats_responsables, palette):
    """
    Genera gráfico de barras de gastos por responsable

    Args:
        stats_responsables: DataFrame con estadísticas por responsable
        palette: Paleta de colores a usar
    """
    plt.figure(figsize=(12, 6))
    bar_plot = sns.barplot(
        data=stats_responsables[:-1],  # Excluye la fila de TOTAL
        x='Responsable',
        y='Total_con_Propina',
        hue='Responsable',
        order=stats_responsables[:-1].sort_values('Responsable', ascending=False)['Responsable'],
        palette=palette,
        legend=False
    )
    plt.title('Distribución del Gasto con Propina (10%) por Responsable', fontsize=16)
    plt.xlabel('Responsable', fontsize=12)
    plt.ylabel('Total + Propina ($)', fontsize=12)
    plt.xticks(rotation=45)

    # Formatear valores en las barras
    for p in bar_plot.patches:
        bar_plot.annotate(
            f"${p.get_height():,.0f}",
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center',
            xytext=(0, 5),
            textcoords='offset points',
            fontsize=10
        )
    plt.tight_layout()
    plt.show()


def grafico_torta(stats_responsables, total_con_propina, colores):
    """
    Genera gráfico de torta de distribución de gastos

    Args:
        stats_responsables: DataFrame con estadísticas por responsable
        total_con_propina: Total de la cuenta con propina
        colores: Lista de colores a usar
    """
    plt.figure(figsize=(10, 10))
    wedges, texts, autotexts = plt.pie(
        stats_responsables[:-1]['Total_con_Propina'],
        labels=stats_responsables[:-1]['Responsable'],
        autopct=lambda p: f"${p * total_con_propina / 100:,.0f}\n({p:.1f}%)",  # Muestra valor y porcentaje
        startangle=90,
        textprops={'fontsize': 12},
        wedgeprops={'edgecolor': 'white', 'linewidth': 1},
        colors=colores
    )

    # Mejorar la legibilidad de los textos
    plt.setp(autotexts, size=10, weight="bold")
    plt.setp(texts, size=12)
    plt.title('Distribución del Total con Propina (10%)', fontsize=16, pad=20)
    plt.tight_layout()
    plt.show()


def mapa_calor(df, stats_responsables):
    """
    Genera mapa de calor de productos por responsable

    Args:
        df: DataFrame con los datos
        stats_responsables: DataFrame con estadísticas por responsable
    """
    # Preparar matriz de valores monetarios
    heatmap_data = df.copy()
    heatmap_data['Responsables'] = heatmap_data['Responsables_JSON'].apply(json.loads)

    responsables_unicos = stats_responsables[:-1]['Responsable'].tolist()
    productos_unicos = heatmap_data['Producto'].unique()

    matriz_valores = pd.DataFrame(0, index=productos_unicos, columns=responsables_unicos)
    matriz_valores = matriz_valores.astype(float)

    for _, row in heatmap_data.iterrows():
        responsables = json.loads(row['Responsables_JSON'])
        monto_por_persona = row['Total'] * 1.1 / len(responsables) if len(responsables) > 0 else 0
        for resp in responsables:
            if resp in responsables_unicos:
                matriz_valores.loc[row['Producto'], resp] += monto_por_persona

    # Ordenar por productos más caros
    matriz_valores = matriz_valores.loc[matriz_valores.sum(axis=1).sort_values(ascending=False).index]

    plt.figure(figsize=(12, 8))
    sns.heatmap(
        matriz_valores,
        cmap="YlOrRd",
        annot=False,  # Ocultamos los valores numéricos
        linewidths=.5,
        cbar_kws={'label': 'Valor asignado ($)'}
    )
    plt.title('Distribución de Valor (con propina) por Producto y Responsable', fontsize=16)
    plt.xlabel('Responsable', fontsize=12)
    plt.ylabel('Producto', fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

# =============================================================================
# FUNCIÓN PRINCIPAL
# =============================================================================


# Ejecutar función principal solo si se ejecuta como script principal
if __name__ == "__main__":
    """Función principal que ejecuta todo el análisis"""

    # Lista de responsables
    responsables = [
        ["Mario"],
        ["Mario"],
        ["Pan"],
        ["Pan"],
        ["Gabriel"],
        ["Gabriel"],
        ["Rafa"],
        ["Rafa"],
        ["Nova"],
        ["Nova"],
        ["German"],
        ["German"],
        ["Shaga"],
        ["Negro"],
        ["Negro", "Shaga"],
        ["Gabriel"],
        ["Negro", "Shaga", "Mario", "Nova"],
        ["Rafa", "German"],
        ["Negro", "Shaga", "Nova", "Pan"],
        ["Negro", "Shaga", "Nova", "Pan"],
        ["Pan"],
        ["Mario"],
        ["German"],
        ["Shaga"],
        ["Nova"],
        ["Negro"],
        ["Negro"],
        ["Shaga"],
        ["Nova"]
    ]

    # Convertir la lista de responsables a formato JSON
    responsables_json = [json.dumps(resp) for resp in responsables]

    # =============================================================================
    # CARGAR Y PROCESAR DATOS
    # =============================================================================

    # Leer el archivo CSV
    df_original = pd.read_csv('boleta.csv')

    # Guardar valores totales para uso futuro
    total_cuenta = df_original.loc[df_original['Cant'] == 'Total', 'Total'].values[0]
    total_con_propina = df_original.loc[df_original['Producto'] == 'c/propina', 'Total'].values[0]

    # Eliminar las filas de resumen (las últimas 4 filas)
    df = df_original[:-4].copy()

    # Eliminar la columna "Cant"
    if 'Cant' in df.columns:
        df = df.drop('Cant', axis=1)

    # Añadir la columna de responsables al DataFrame
    if len(responsables_json) >= len(df):
        df['Responsables_JSON'] = responsables_json[:len(df)]
    else:
        # Si no hay suficientes responsables, completar con una lista vacía
        df['Responsables_JSON'] = responsables_json + ['[]'] * (len(df) - len(responsables_json))

    # =============================================================================
    # ANÁLISIS Y RESULTADOS
    # =============================================================================

    # Mostrar el DataFrame procesado
    print("DataFrame procesado:")
    print_left_aligned(df)

    # Verificar que el total de la suma coincide con nuestro total_cuenta guardado
    suma_productos = df['Total'].sum()

    if suma_productos != total_cuenta:
        print(f"Hay una diferencia de {total_cuenta - suma_productos} entre el total calculado y el guardado.")

    if suma_productos * 1.1 != total_con_propina:
        print(
            f"Hay una diferencia de {total_con_propina - suma_productos * 1.1} entre el total con propina calculado y el guardado.")

    # Mostrar estadísticas básicas
    print("\nEstadísticas básicas:")
    print(df.describe())

    # Calcular y mostrar estadísticas por responsable
    print("\nEstadísticas por responsable:")
    stats_responsables = calcular_estadisticas_por_responsable(df, total_cuenta, total_con_propina)
    print_left_aligned(stats_responsables)

    # =============================================================================
    # VISUALIZACIONES
    # =============================================================================

    # Obtener responsables ordenados por Total_con_Propina (sin incluir TOTAL)
    responsables_ordenados = stats_responsables[:-1].sort_values('Total_con_Propina', ascending=False)['Responsable']

    # Ajustar número de colores
    num_responsables = len(responsables_ordenados)
    palette = COLORES[:num_responsables] if num_responsables <= len(COLORES) else sns.color_palette("husl",
                                                                                                    num_responsables)

    # Generar gráficos
    grafico_barras(stats_responsables, palette)
    grafico_torta(stats_responsables, total_con_propina, COLORES)
    mapa_calor(df, stats_responsables)

    # =============================================================================
    # TABLAS DE DETALLE
    # =============================================================================

    # Generar tablas detalladas
    tabla_productos, tabla_precios = generar_tablas_detalle(df, stats_responsables)

    # Mostrar tablas
    print("\nTabla de Productos por Responsable:")
    print_left_aligned(tabla_productos)
    print("\nTabla de Precios por Responsable:")
    print_left_aligned(tabla_precios)