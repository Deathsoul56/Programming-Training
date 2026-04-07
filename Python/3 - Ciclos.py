"""
CLASE 3: CICLOS EN PYTHON

Esta clase cubre los conceptos fundamentales de ciclos en Python:
1. Ciclo While
2. Ciclo For
3. Control de flujo (break, continue)
4. Ciclos anidados
5. Optimización de ciclos
6. Manejo de errores en ciclos
"""

print("=== CLASE 3: CICLOS EN PYTHON ===\n")

print("Los ciclos nos permiten repetir código de manera eficiente.")
print("Python ofrece principalmente dos tipos de ciclos: while y for")
print()

# =============================================================================
# 1. CICLO WHILE
# =============================================================================

print("1. CICLO WHILE")
print("=" * 40)
# Tipo While
x = -3 
while x <= 10: # Ciclo while que imprime valores de x desde -3 hasta 10
    print(f"Valor de x = {x}")
    x += 1

y = 0
while True: # while infinito
    y += 1
    if y == 5:
        print("Se rompio el ciclo")
        break # Romper el ciclo
    else:
        print("Ciclo infinito")

# =============================================================================
# 2. CICLO FOR
# =============================================================================

print("\n2. CICLO FOR")
print("=" * 40)

# Avanzar por un rango
for i in range(5+1): #Ciclo for imprime de 0 hasta n-1
    print(f"Valor de i = {i:02d}")  # Formatea el número con dos dígitos

for j in range(-5, 7): # Imprime de -5 hasta 7 el intervalor es semi cerrado [-5, 7)
    print(f"Valor de j = {j}")

# Avanzar por una lista
mi_lista = ['a', 'c', 7, 3.1415, True, 'lambda']
for elemento in mi_lista:
    print(f"El elemento {mi_lista.index(elemento)} de la lista es = {elemento} de tipo = {type(elemento)}") # El metodo index es poco eficiente

for indice, elemento in enumerate(mi_lista):
    print(f"El elemento {indice} de la lista es = {elemento} de tipo = {type(elemento)}") # con el metodo enumerate es mucho mas optimo

# Verificar múltiples valores en una lista
numeros = [10, 15, 20, 25, 30]
for num in numeros:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

# =============================================================================
# 3. CONTROL DE FLUJO (BREAK Y CONTINUE)
# =============================================================================

print("\n3. CONTROL DE FLUJO")
print("=" * 40)

# Ciclos con continue, puede ser útil para saltar ciertas iteraciones en un ciclo
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar números pares
    print(f"Número impar: {i}")

# =============================================================================
# 4. MANEJO DE ERRORES EN CICLOS
# =============================================================================

print("\n4. MANEJO DE ERRORES EN CICLOS")
print("=" * 40)

# Ciclos con manejos de errores
for i in range(-1, 5):
    try:
        print(f"10 / {i}: {10 / i}")
    except ZeroDivisionError:
        print(f"Error: No se puede dividir 10 entre {i} (división por cero).")
        continue  # Continuar con la siguiente iteración

# =============================================================================
# 5. CICLOS ANIDADOS Y OPTIMIZACIÓN
# =============================================================================

print("\n5. CICLOS ANIDADOS Y OPTIMIZACIÓN")
print("=" * 40)
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

for numero in numeros:
    for letra in letras:
        print(numero, letra)

# Los ciclos anidados no son buenos para el rendimiento, una alternativa es usar el metodo Zip
for numero, letra in zip(numeros, letras):
    print(numero, letra)

# Recorrer una matriz
matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
print(f"La matriz original: {matriz}")
for i in matriz:
    print(f"Valor {matriz.index(i)} es: {i}")
    for j in i:
        print(f"Es valor {i.index(j)} es: {j}")

# De manera mas optima
matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
print(f"La matriz original: {matriz}")
for fila_idx, fila in enumerate(matriz):
    print(f"Fila {fila_idx}: {fila}")
    for columna_idx, valor in enumerate(fila):
        print(f"  Columna {columna_idx}: {valor}")

# =============================================================================
# CONCLUSIONES
# =============================================================================

print("\n" + "=" * 50)
print("CONCLUSIONES SOBRE CICLOS EN PYTHON")
print("=" * 50)

print("\n1. CUÁNDO USAR CADA TIPO DE CICLO:")
print("   • while: Cuando no sabemos exactamente cuántas iteraciones necesitamos")
print("   • for: Cuando iteramos sobre una secuencia conocida o un rango definido")

print("\n2. MEJORES PRÁCTICAS:")
print("   • Usar enumerate() en lugar de index() para mejor rendimiento")
print("   • Preferir zip() sobre ciclos anidados cuando sea posible")
print("   • Usar break y continue para controlar el flujo de manera eficiente")
print("   • Manejar errores dentro de ciclos para evitar interrupciones inesperadas")

print("\n3. OPTIMIZACIÓN:")
print("   • Los ciclos anidados pueden ser costosos en términos de rendimiento")
print("   • enumerate() es más eficiente que usar index() repetidamente")
print("   • zip() es más legible y eficiente que ciclos anidados para combinar listas")

print("\n4. CONTROL DE FLUJO:")
print("   • break: Termina el ciclo completamente")
print("   • continue: Salta a la siguiente iteración")
print("   • else en ciclos: Se ejecuta si el ciclo termina normalmente (sin break)")

print("\n5. CASOS DE USO COMUNES:")
print("   • Procesamiento de listas y secuencias")
print("   • Validación de entrada del usuario")
print("   • Operaciones matemáticas repetitivas")
print("   • Recorrido de estructuras de datos complejas")

print("\n=== FIN DE LA CLASE 3 ===\n")