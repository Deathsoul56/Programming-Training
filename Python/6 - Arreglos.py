import numpy as np

# Introducción a los arreglos
print("Los arreglos son estructuras de datos que permiten almacenar múltiples valores del mismo tipo. En Python, numpy es una librería muy utilizada para trabajar con arreglos.")


# Creación de arreglos
Numerico = np.array([3, 6, 8, 3, 13, 63, 17, 56, 234, 21, 73, 13, 8, 37, 64, 10, 15])
Flotante = np.array([3.1415, 2.7154, 8.2326])
String = np.array(['Rojo', 'Verde', 'Azul', 'Negro', 'Blanco', 'Cafe'])
Cadena = np.array([2, 'Gauss', 3.1415, 'Noether', 17, 31, 73, 'Newton'])

print("\n --- Creacion de arreglos ---")
print(Numerico)
print(Flotante)
print(String)
print(Cadena)


# Otras formas de crear arreglos
zeros = np.zeros(5)  # Arreglo de ceros
ones = np.ones(5)    # Arreglo de unos
full = np.full(5, 7) # Arreglo lleno de un valor específico, arreglo de solo 7 con 5 elementos
linspace = np.linspace(0, 10, 5)  # Arreglo con valores espaciados uniformemente, empieza en 0 termina en 10 y tiene 5 elementos

print("\n --- Otras formas de crear arreglos ---")
print(f"Arreglo de ceros: {zeros}")
print(f"Arreglo de unos: {ones}")
print(f"Arreglo lleno de 7 con 5 elementos: {full}")
print(f"Arreglo con valores espaciados uniformemente, comienza en 0 termina el 10 y tiene 5 elementos: {linspace}")


# Ordenar arreglos
print("\n --- Ordenar arreglos ---")

print(f"Arreglo original: {Numerico}")
Numerico.sort()
print(f"Arreglo ordenado: {Numerico}")

print(f"Arreglo de cadenas original: {String}")
String.sort()
print(f"Arreglo de cadenas ordenado: {String}")

print(f"Arreglo de cadenas original: {Cadena}")
Cadena.sort()
print(f"Arreglo de cadenas ordenado: {Cadena}")

# Crear una copia antes de ordenar
Flotante_ordenado = np.sort(Flotante)
print(f"Arreglo original: {Flotante}")
print(f"Arreglo ordenado: {Flotante_ordenado}")


# Indexación y slicing
print("\n --- Indexación y slicing ---")

print(f"Elemento en la posición 2: {Numerico[2]}") # Imprimer el elemento en la posicion 2

for i in range(len(Flotante)):
    print(f"El valor {i} = {Flotante[i]}")

for indice, valor in enumerate(Flotante):
    print(f"El valor en la posición {indice} = {valor}")

print(f"Subarreglo de la posición 2 a la 6: {Numerico[2:6]}")  # Imprime un array con los elementos que estén en la posición 2 a la 6 [2, 6)
print(f"Subarreglo desde el inicio hasta la posición 6: {Numerico[:6]}")  # Imprime un array con los elementos que estén en la posición 0 a la 6 [0, 6)
print(f"Subarreglo desde la posición 8 hasta el final: {Numerico[8:]}")  # Imprime un array con los elementos que estén en la posición 8 a la última [8, última)
print(f"Subarreglo desde el inicio hasta la penúltima posición: {Numerico[0:-1]}")  # Imprime un array con los elementos que estén en la posición 0 a la penúltima [0, última)
print(f"Todo el arreglo: {Numerico[:]}")  # Imprime todo el array

print(f"Subarreglo de la posición 2 a la 6: {Numerico[2:6]}") # Imprimer un array con los elementos 2 y los elementos con 6 posiciones de diferencia [2 ; 2+6 ; 2+6*2]
print(f"Subarreglo con paso 5: {Numerico[1::5]}")  # Imprime un array con los elementos 1 y los elementos con 5 posiciones de diferencia [1, 1+5, 1+5*2, ...]


# Agregar y quitar datos
print("\n --- Agregar y quitar datos ---")
Flotante = np.append(Flotante, 65.2345)
print(f"Arreglo después de agregar un elemento: {Flotante}")
Flotante = np.delete(Flotante, 2)
print(f"Arreglo después de eliminar un elemento: {Flotante}")


# Combertir de Array a String
print("\n --- Combertir de Array a String ---")
saludo = np.array(['h', 'o', 'l', 'a'])
juntar = ''.join(saludo)
juntar2 = '-'.join(saludo)
print(f"Cadena concatenada: {juntar} {juntar2}")


# Concatenar arreglos
print("\n --- Concatenar arreglos ---")
concatenado = np.concatenate((Numerico, Flotante))
print(f"Arreglos concatenados: {concatenado}")

# Buscar un elemento en el arreglo
print("\n --- Buscar un elemento en el arreglo ---")
if 13 in Numerico:
    print("El número 13 está en el arreglo.")
else:
    print("El número 13 no está en el arreglo.")

# Convertir a mayúsculas
print("\n --- Convertir a mayúsculas ---")
String_mayusculas = np.char.upper(String)
print(f"Arreglo de cadenas en mayúsculas: {String_mayusculas}")

# Crear un array con números del 3 al 15 usando np.arange
print("\n --- Crear lista ---")

numeros = np.arange(3, 16)  # Forma mas eficiente
print(f"Array con números del 3 al 15 con np.arange: {numeros}")

numeros = np.array(range(3, 16)) # Crear un array con números del 3 al 15 usando range
print(f"Array con números del 3 al 15 con range(): {numeros}")

numeros = np.array([i for i in range(3, 16)]) # Lista por comprensión
print(f"Array con números del 3 al 15 por comprension: {numeros}")


# Las listas son mutables
print("\n --- Las listas son mutables ---")
a = np.array([1, 2, 3])
print(f"Arreglo orignial: {a}")
b = a
b[0] = 10
print(f" b = a \n b[0] = {b[0]}")
print(f"Arreglo a: {a}")
print(f"Arreglo b: {b}")  # Ambos arreglos son iguales
print(f"Ambos arreglos son iguales")

# Operaciones matemáticas
print("\n --- Operaciones matemáticas ---")

a = np.array([10, 3, 11, 2, 5])
b = np.array([3, 8, 6, 2, 7])
print(f"primer arreglo: {a} \nsegundo arreglo: {b} \nlos arreglos deben que tener la misma cantidad de elementos para operarlos")
print(f"Suma de arreglos: a + b = {a + b}")
print(f"Resta de arreglos: a - b = {a - b}")
print(f"Multiplicación de arreglos: a * b = {a * b}")
print(f"División de arreglos: a / b = {a / b}")


# Funciones estadísticas
print("\n --- Funciones estadísticas ---")

print("Media del arreglo Numerico:", np.mean(Numerico))
print("Mediana del arreglo Numerico:", np.median(Numerico))
print("Desviación estándar del arreglo Numerico:", np.std(Numerico))
print("Suma de los elementos del arreglo Numerico:", np.sum(Numerico))

# Cambiar la forma de un arreglo
print("\n ---Cambiar la forma de un arreglo ---")

arreglo = np.arange(10)
print(f"Arreglo original: {arreglo}")
arreglo_reshape = arreglo.reshape(2, 5)
print(f"Arreglo reshapeado a 2x5: {arreglo_reshape}")

# Comparación de arreglos
print("\n ---Comparación de arreglos ---")

arreglo1 = np.array([1, 2, 3])
arreglo2 = np.array([1, 2, 3])
print(f"¿Los arreglos {arreglo1} y {arreglo2} son iguales? {np.array_equal(arreglo1, arreglo2)}")

# Introducción a las matrices
print("\n --- Introducción a las matrices ---")
print("Una matriz es una estructura de datos bidimensional que contiene elementos organizados en filas y columnas. En Python, numpy es una librería muy utilizada para trabajar con matrices.")

# Creación de matrices numéricas
print("\n --- Creación de matrices numéricas ---")

matriz_numerica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz numérica:")
print(matriz_numerica)

# Creación de matrices de cadenas
matriz_cadenas = np.array([['Rojo', 'Verde', 'Azul'], ['Negro', 'Blanco', 'Cafe'], ['Amarillo', 'Morado', 'Rosa']])
print("\nMatriz de cadenas:")
print(matriz_cadenas)

# Creación de matrices con diferentes tipos de datos
matriz_mixta = np.array([[1, 'Gauss', 3.1415], [4, 'Noether', 6.2831], [7, 'Newton', 9.8696]])
print("\nMatriz mixta (números y cadenas):")
print(matriz_mixta)

# Acceso a elementos de una matriz
print("\nAcceso a elementos de una matriz:")
print(f"Elemento en la fila 1, columna 2 de la matriz numérica: {matriz_numerica[1, 2]}") # Ingresando el valor como Array
print(f"Elemento en la fila 0, columna 1 de la matriz de cadenas: {matriz_cadenas[0][1]}") # Ingresando el valor como 2 int
print(f"fila 2 de la matriz de mixta: {matriz_mixta[2]}")
print(f"columna 1 de la matriz de mixta: {matriz_mixta[:, 1]}")

# Concatenación de matrices
print("\n --- Concatenación de matrices ---")

matriz_a = np.array([[9, 7], [8, 4]])
matriz_b = np.array([[5, 3], [5, 2]])
print("Matriz A:")
print(matriz_a)
print("Matriz B:")
print(matriz_b)

matriz_concatenada = np.concatenate((matriz_a, matriz_b), axis=0)
print("Concatenación vertical:")
print(matriz_concatenada)

matriz_concatenada = np.concatenate((matriz_a, matriz_b), axis=1)
print("\nConcatenación horizontal:")
print(matriz_concatenada)

# Operaciones con matrices de cadenas
print("\nOperaciones con matrices de cadenas:")
print("Convertir todas las cadenas a mayúsculas:")
print(np.char.upper(matriz_cadenas))

print("\nConcatenar cadenas en la matriz:")
print(np.char.add(matriz_cadenas, matriz_cadenas))