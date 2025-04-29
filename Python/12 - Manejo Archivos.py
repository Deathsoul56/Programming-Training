import csv
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- ARCHIVOS DE EJEMPLO (CREACIÓN) ---
def crear_archivos_ejemplo():
    # Crear archivo de texto
    with open('mi_archivo.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("Este es un archivo de texto de ejemplo.\n")
        archivo.write("Contiene varias líneas de texto.\n")
        archivo.write("Cada línea tiene su propio contenido.\n")
        archivo.write("Puedes usar este archivo para practicar\n")
        archivo.write("la lectura de líneas completas,\n")
        archivo.write("la iteración sobre las líneas,\n")
        archivo.write("y quizás incluso buscar palabras específicas.\n")
        archivo.write("¡Espero que te sea útil para tu curso de Python!\n")

    # Crear archivo CSV
    datos_csv = [
        ['Nombre', 'Edad', 'Ciudad'],
        ['Ana', 25, 'Madrid'],
        ['Juan', 30, 'Barcelona'],
        ['María', 28, 'Valencia']
    ]
    with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos_csv)

crear_archivos_ejemplo() # Aseguramos que los archivos existan

print("\n=== 1. MANEJO DE ARCHIVOS .TXT ===")

# Leer archivo .txt
print("Leyendo archivo.txt:")
with open('mi_archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print("\nContenido completo:")
    print(contenido)

# Leer línea por línea
print("\nLeyendo línea por línea:")
with open('mi_archivo.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(f"Línea: {linea.strip()}")

# Agregar contenido al archivo (append)
with open('mi_archivo.txt', 'a', encoding='utf-8') as archivo:
    archivo.write("\n\n--- NUEVO CONTENIDO AGREGADO ---")
    archivo.write("\nEsta línea se añadió al final.")

print("\n=== 2. MANEJO DE ARCHIVOS .CSV ===")

# Leer archivo CSV
print("\nLeyendo archivo CSV:")
with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(f"Fila: {fila}")

#  CSV como Diccionarios
print("\nLeyendo CSV como diccionarios:")
with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(dict(fila))

print("\n=== 3. INFORMACIÓN DEL ARCHIVO Y MANEJO DE ERRORES ===")

# Verificar si un archivo existe y obtener información
def verificar_archivo(nombre_archivo):
    if os.path.exists(nombre_archivo):
        print(f"\nEl archivo '{nombre_archivo}' existe.")
        tamaño = os.path.getsize(nombre_archivo)
        print(f"Tamaño: {tamaño} bytes")
        fecha_modificacion = os.path.getmtime(nombre_archivo) # Timestamp
        print(f"Fecha de última modificación: {fecha_modificacion}")
    else:
        print(f"\nEl archivo '{nombre_archivo}' no existe.")

verificar_archivo('mi_archivo.txt')
verificar_archivo('datos.csv')
verificar_archivo('archivo_inexistente.txt')  # Provocará el "no existe"

# Manejo de errores al leer un archivo
try:
    with open('archivo_inexistente.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("\n¡Error! El archivo no fue encontrado.")
except Exception as e:
    print(f"\nOcurrió un error: {e}")


print("\n=== 4.  OPERACIONES ADICIONALES CON CSV ===")

# Filtrar datos del CSV
print("\nFiltrando personas mayores de 28 años:")
with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        if int(fila['Edad']) > 28:
            print(f"{fila['Nombre']} tiene {fila['Edad']} años.")

# Modificar y escribir un nuevo CSV (ejemplo: incrementar edades)
def incrementar_edades(archivo_entrada, archivo_salida):
    datos_modificados = []
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_in:
            lector = csv.DictReader(archivo_in)
            for fila in lector:
                fila['Edad'] = int(fila['Edad']) + 1
                datos_modificados.append(fila)
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_entrada} no fue encontrado.")
        return

    if datos_modificados:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as archivo_out:
            campos = datos_modificados[0].keys()
            escritor = csv.DictWriter(archivo_out, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos_modificados)
        print(f"\nEdades incrementadas y guardadas en {archivo_salida}")

incrementar_edades('datos.csv', 'datos_modificados.csv')


print("\n=== 5. LIMPIEZA ===")

# Eliminar los archivos creados (opcional, ¡cuidado!)
archivos_a_eliminar = ['mi_archivo.txt', 'datos.csv', 'datos_modificados.csv'] # Evita eliminar archivos importantes!

print("\nEliminando archivos...")
for archivo in archivos_a_eliminar:
    try:
        os.remove(archivo)
        print(f"Archivo '{archivo}' eliminado.")
    except FileNotFoundError:
        print(f"Archivo '{archivo}' no encontrado.")
    except Exception as e:
        print(f"Error al eliminar '{archivo}': {e}")