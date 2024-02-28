# Ciclos

# Tipos While
x = -3
while x <= 10:
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

# Ciclos for

# Avanzar por un rango
for i in range(5+1): #Ciclo for imprime de 0 hasta n-1
    print(f"Valor de i = {i}")

for j in range(-5, 7): # Imprime de -5 hasta 3 el intervalor es semi cerrado [-5, 4)
    print(f"Valor de j = {j}")

# Avanzar por una lista
list = ['a', 'c', 7, 3.1415, True, 'lamda']
for i in list:
    print(f"en elemento {list.index(i)} de la lista es = {i} de tipo =  {type(i)}")

# Ciclos Anidados
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

for numero in numeros:
    for letra in letras:
        print(numero, letra)

# Recorrer una matriz
matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
print(f"La matriz original: {matriz}")
for i in matriz:
    print(f"Valor {matriz.index(i)} es: {i}")
    for j in i:
        print(f"Es valor {i.index(j)} es: {j}")