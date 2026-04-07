"""
CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL

Esta clase cubre los conceptos fundamentales de condiciones en Python:
1. Entrada de datos con validación
2. Condicional simple (if-else) y múltiple (if-elif-else)
3. Match-Case y condicionales anidados
4. Operadores lógicos y funciones any() / all()
5. Diccionarios como alternativa a condiciones
6. Manejo de excepciones (try-except)
"""

print("=== CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL ===\n")

print("--- ¿Qué son las condiciones? ---")
print("Las condiciones permiten que el programa tome decisiones")
print("basándose en si ciertas expresiones son verdaderas o falsas.")
print("Python evalúa expresiones que devuelven True o False.")

# =============================================================================
# 1. ENTRADA DE DATOS CON VALIDACIÓN
# =============================================================================

print("\n1. ENTRADA DE DATOS CON VALIDACIÓN")
print("=" * 40)

print("\n--- Entrada de datos con validación ---")
print("Antes de trabajar con condiciones, obtengamos un número del usuario:")

# Validación de entrada mediante un try
try:
    x = int(input("Ingrese un número entero: "))
    print(f"Número ingresado correctamente: {x}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    print("Usando valor por defecto: 10")
    x = 10  # Valor por defecto para continuar con el ejemplo

# =============================================================================
# 2. CONDICIONAL SIMPLE Y MÚLTIPLE
# =============================================================================

print("\n2. CONDICIONAL SIMPLE Y MÚLTIPLE")
print("=" * 40)

print("\n--- Condicional simple (if-else) ---")
print("La estructura if-else permite ejecutar código según una condición:")
print("Sintaxis: if condición: ... else: ...")

# Verificar si un número es par o impar
print(f"\nEvaluando si {x} es par o impar:")
if x % 2 == 0:                       # Si la condición es verdadera
    print(f"✓ El número {x} es par")   # Se ejecuta este bloque
else:                                # Si la condición es falsa
    print(f"✓ El número {x} es impar") # Se ejecuta este bloque

print(f"\nOperador ternario (forma compacta):")
resultado = f"{x} es par" if x % 2 == 0 else f"{x} es impar"
print(f"Resultado: {resultado}")

print("\n--- Condicional múltiple (if-elif-else) ---")
print("Cuando tenemos múltiples condiciones, usamos elif:")
print("Sintaxis: if condición1: ... elif condición2: ... else: ...")

# Verificar múltiples condiciones con elif
resto = x % 3
print(f"\nClasificando {x} según su resto al dividir por 3:")
print(f"Resto de {x} ÷ 3 = {resto}")

if x % 3 == 0:                                              # Primera condición
    print(f"✓ El valor {x} es múltiplo de 3 (resto = 0)")   
elif x % 3 == 1:                                            # Segunda condición
    print(f"✓ El valor {x} deja resto 1 al dividir por 3")   
else:                                                       # Caso por defecto
    print(f"✓ El valor {x} deja resto 2 al dividir por 3")   

print("\nNota: Solo se ejecuta el primer bloque cuya condición sea verdadera")

# =============================================================================
# 3. MATCH-CASE Y CONDICIONALES ANIDADOS
# =============================================================================

print("\n3. MATCH-CASE Y CONDICIONALES ANIDADOS")
print("=" * 40)

print("\n--- Match-Case (Python 3.10+) ---")
print("La estructura match-case es similar al switch de otros lenguajes:")
print("Es más limpia para comparar un valor contra múltiples opciones.")

# Forma alternativa, usar match-case para manejar múltiples condiciones
print(f"\nUsando match-case para el mismo ejemplo (resto = {x % 3}):")
match x % 3:
    case 0:
        print(f"✓ Match-case: {x} es múltiplo de 3")
    case 1:
        print(f"✓ Match-case: {x} deja resto 1")
    case 2:
        print(f"✓ Match-case: {x} deja resto 2")
    case _:  # Caso por defecto (wildcard)
        print("✓ Match-case: caso inesperado")

print("Ventaja: más legible cuando comparamos un valor contra muchas opciones")

print("\n--- Condicionales anidados ---")
print("Podemos poner condiciones dentro de otras condiciones:")
print("Útil cuando necesitamos verificar múltiples criterios en secuencia.")

# If anidados
y = 5
print(f"\nComparando x = {x} con y = {y}:")

if x > y:
    print(f"✓ {x} > {y}, ahora verificamos si x es par o impar:")
    if x % 2 == 0:
        print(f"  ✓ {x} es mayor que {y} Y además es par")
    else:
        print(f"  ✓ {x} es mayor que {y} Y además es impar")
else:
    print(f"✓ {x} es menor o igual que {y}")

print("\nCuidado: demasiados niveles de anidación dificultan la lectura")

# =============================================================================
# 4. OPERADORES LÓGICOS Y FUNCIONES ANY/ALL
# =============================================================================

print("\n4. OPERADORES LÓGICOS Y FUNCIONES ANY/ALL")
print("=" * 40)

print("\n--- Operadores lógicos ---")
print("Los operadores lógicos combinan múltiples condiciones:")
print("• and: ambas condiciones deben ser verdaderas")
print("• or: al menos una condición debe ser verdadera") 
print("• not: invierte el valor de verdad")

z = 15
print(f"\nComparando x = {x}, y = {y}, z = {z}:")

print(f"\nUsando AND (ambas condiciones deben cumplirse):")
if x > y and x < z:
    print(f"✓ {x} > {y} Y {x} < {z}: x está entre y y z")
elif x > y and x > z:
    print(f"✓ {x} > {y} Y {x} > {z}: x es mayor que ambos")
elif x < y and x < z:
    print(f"✓ {x} < {y} Y {x} < {z}: x es menor que ambos")
else:
    print("✓ Ninguna combinación and se cumple")

print(f"\nUsando OR (al menos una condición debe cumplirse):")
if x > y or x > z:
    print(f"✓ {x} es mayor que {y} O mayor que {z} (o ambas)")
else:
    print(f"✓ {x} no es mayor que {y} ni que {z}")

print(f"\nUsando NOT (negación):")
if not x == y:
    print(f"✓ {x} NO es igual a {y}")
else:
    print(f"✓ {x} SÍ es igual a {y}")

print("\n--- Funciones any() y all() ---")
print("Útiles para evaluar múltiples condiciones en listas:")
print("• any(): True if al menos una condición es verdadera")
print("• all(): True si TODAS las condiciones son verdaderas")

# Uso de any y all
condiciones = [x > y, x < z, x % 2 == 0]
valores_condiciones = [
    f"{x} > {y} = {x > y}",
    f"{x} < {z} = {x < z}", 
    f"{x} % 2 == 0 = {x % 2 == 0}"
]

print(f"\nEvaluando múltiples condiciones:")
for condicion in valores_condiciones:
    print(f"  • {condicion}")

print(f"\nResultados:")
if all(condiciones):
    print("✓ all(): TODAS las condiciones son verdaderas")
else:
    print("✗ all(): NO todas las condiciones son verdaderas")

if any(condiciones):
    print("✓ any(): Al menos UNA condición es verdadera")
else:
    print("✗ any(): NINGUNA condición es verdadera")

# =============================================================================
# 5. DICCIONARIOS COMO ALTERNATIVA
# =============================================================================

print("\n5. DICCIONARIOS COMO ALTERNATIVA")
print("=" * 40)

print("\n--- Diccionarios como alternativa a condiciones ---")
print("A veces es más eficiente usar diccionarios para mapear valores:")
print("Especialmente útil cuando tenemos muchas opciones fijas.")

# Uso de diccionarios para mapear condiciones
acciones = {
    0: "múltiplo de 3 (resto = 0)",
    1: "deja resto 1 al dividir por 3", 
    2: "deja resto 2 al dividir por 3"
}

resto = x % 3
mensaje = acciones.get(resto, "caso inesperado")
print(f"\nUsando diccionario para {x}:")
print(f"Resto: {resto}")
print(f"Resultado: {x} es {mensaje}")

print(f"\nVentajas del diccionario:")
print("• Más rápido para muchas opciones")
print("• Más limpio que múltiples elif")
print("• Fácil de mantener y modificar")

# =============================================================================
# 6. MANEJO DE EXCEPCIONES
# =============================================================================

print("\n6. MANEJO DE EXCEPCIONES")
print("=" * 40)

print("\n--- Manejo de excepciones (try-except) ---")
print("Las excepciones permiten manejar errores de forma controlada:")
print("Estructura: try -> except -> else -> finally")

# Ejemplo de manejo de excepciones
n1 = 10
n2 = 3

print(f"\nEjemplo: dividiendo {n1} entre {n2}")

try:
    print("→ Intentando realizar la división...")
    resultado = n1 / n2
    
    # Condición dentro del try
    if resultado == int(resultado):
        print(f"✓ La división da un número entero: {int(resultado)}")
    else:
        print(f"✓ La división da un número decimal: {resultado:.3f}")

except ZeroDivisionError:
    print("✗ Error: No se puede dividir entre cero")

except TypeError:
    print("✗ Error de tipo: los valores deben ser números")

except Exception as e:
    print(f"✗ Error inesperado: {e}")

else:
    print("✓ La operación se completó sin errores")

finally:
    print("→ Bloque finally: se ejecuta SIEMPRE")

print(f"\nProbemos con división por cero:")
try:
    resultado_cero = n1 / 0
except ZeroDivisionError:
    print("✓ Excepción capturada correctamente: división por cero")

# =============================================================================
# CONCLUSIONES
# =============================================================================

print("\n" + "=" * 50)
print("CONCLUSIONES SOBRE CONDICIONES Y ESTRUCTURAS DE CONTROL")
print("=" * 50)

print("\n1. ESTRUCTURAS BÁSICAS:")
print("   • if/else evalúan caminos excluyentes basados en una condición (True o False).")
print("   • elif permite anidar más caminos en caso de evaluaciones compuestas.")

print("\n2. MATCH-CASE Y OPERADOR TERNARIO:")
print("   • El operador ternario es ideal para condiciones en una sola línea.")
print("   • Match-Case es más veloz y ordenado cuando se comparan múltiples variantes fijas del mismo valor.")

print("\n3. OPERADORES LÓGICOS Y FUNCIONES:")
print("   • and (todas válidas), or (alguna válida), not (inversión fuerte).")
print("   • any() valida si al menos un elemento en un conjunto de condiciones es True, y all() valida que todos lo sean.")

print("\n4. MANEJO SEGURO:")
print("   • Siempre capturar errores en las partes del código susceptibles a fallos usando try/except.")
print("   • Utilizar diccionarios como rutas rápidas mapeadas ante combinaciones if/elif excesivas.")

print("\n=== FIN DE LA CLASE 2 ===\n")