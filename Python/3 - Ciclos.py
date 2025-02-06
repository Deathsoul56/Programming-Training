# Ciclos

print("\n--- Ciclo While ---")
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

print("\n--- Ciclo For ---")
# Ciclos for

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

# ciclos con continue, puede ser útil para saltar ciertas iteraciones en un ciclo
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar números pares
    print(f"Número impar: {i}")

# Ciclos con manejos de errores
for i in range(-1, 5):
    try:
        print(f"10 / {i}: {10 / i}")
    except ZeroDivisionError:
        print(f"Error: No se puede dividir 10 entre {i} (división por cero).")
        continue  # Continuar con la siguiente iteración

print("\n--- Ciclos Anidados ---")
# Ciclos Anidados
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