import numpy as np
import scipy as sp

# Introducción a las matrices y Vectores
print("\n --- Introducción a las matrices y Vectores ---")

print("Los vectores son estructuras de datos unidimensionales que permiten almacenar múltiples valores del mismo tipo. En Python, numpy es una librería muy utilizada para trabajar con vectores.")

# Crear vectores
print("\nCreación de vectores:")
v1 = np.array([5, 2, 7])
v2 = np.array([3, 7, 8])
escalar = 2

print("Vector v1:", v1)
print("Vector v2:", v2)
print("Escalar:", escalar)

# Operaciones con vectores

# Operaciones básicas
print("\n1. Operaciones básicas:")
print(f"Suma de vectores: {v1 + v2}")
print(f"Resta de vectores: {v1 - v2}")
print(f"Multiplicación por escalar: {escalar * v1}")
print(f"División por escalar: {v1 / escalar}")

# Productos entre vectores
print("\n2. Productos entre vectores:")
print(f"Producto punto: {np.dot(v1, v2)}")
print(f"Producto punto (alternativo): {v1 @ v2}")
print(f"Producto cruz: {np.cross(v1, v2)}")
print(f"Producto exterior:\n{np.outer(v1, v2)}")

# Normas y magnitudes
print("\n3. Normas y magnitudes:")
print(f"Norma L1 (Manhattan): {np.linalg.norm(v1, 1)}")
print(f"Norma L2 (Euclidiana): {np.linalg.norm(v1)}")
print(f"Norma máxima: {np.linalg.norm(v1, np.inf)}")
print(f"Suma de elementos: {np.sum(v1)}")
print(f"Producto de elementos: {np.prod(v1)}")

# Operaciones angulares
print("\n4. Operaciones angulares:")
angulo = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(f"Ángulo entre vectores (radianes): {angulo}")
print(f"Ángulo entre vectores (grados): {np.degrees(angulo)}")

# Normalización y proyección
print("\n5. Normalización y proyección:")
v1_norm = v1 / np.linalg.norm(v1)
print(f"Vector v1 normalizado: {v1_norm}")
print(f"Comprobación magnitud = 1: {np.linalg.norm(v1_norm)}")

# Proyección de v1 sobre v2
proy = (np.dot(v1, v2) / np.dot(v2, v2)) * v2
print(f"Proyección de v1 sobre v2: {proy}")

# Vectores especiales
print("\n6. Vectores especiales:")
print(f"Vector unitario: {np.ones(3)}")
print(f"Vector cero: {np.zeros(3)}")
print(f"Vector con valores espaciados uniformemente: {np.linspace(0, 1, 5)}")
print(f"Vector con valores aleatorios: {np.random.rand(3)}")

# Operaciones lógicas
print("\n7. Operaciones lógicas:")
print(f"¿Elementos de v1 > 1?: {v1 > 1}")
print(f"¿Vectores iguales?: {np.array_equal(v1, v2)}")
print(f"¿Algún elemento > 2?: {np.any(v1 > 2)}")
print(f"¿Todos los elementos > 0?: {np.all(v1 > 0)}")

# Estadísticas básicas
print("\n8. Estadísticas básicas:")
print(f"Vector ordenado: {np.sort(v1)}")
print(f"Valor máximo: {np.max(v1)}")
print(f"Valor mínimo: {np.min(v1)}")
print(f"Media: {np.mean(v1)}")
print(f"Desviación estándar: {np.std(v1)}")
print(f"Varianza: {np.var(v1)}")


print("Las matrices son estructuras de datos bidimensionales que permiten almacenar múltiples valores del mismo tipo organizados en filas y columnas. En Python, numpy es una librería muy utilizada para trabajar con matrices.")

# Creación de matrices
Numerica = np.array([[2, 4, 5], [3, 7, 2], [1, 6, 8]])
Flotante = np.array([[3.1415, 2.7154], [8.2326, 1.4142], [0.5772, 1.7320]])
String = np.array([['Rojo', 'Verde', 'Azul'], ['Negro', 'Blanco', 'Cafe'], ['Amarillo', 'Morado', 'Rosa']])
Mixta = np.array([[1, 'Gauss', 3.1415], [4, 'Noether', 6.2831], [7, 'Newton', 9.8696]])

print("\n --- Creacion de matrices ---")
print("Matriz numérica:")
print(Numerica)
print("\nMatriz flotante:")
print(Flotante)
print("\nMatriz de cadenas:")
print(String)
print("\nMatriz mixta:")
print(Mixta)

# Matriz por comprensión
matriz_comp = [[i+j for j in range(3)] for i in range(3)]
print("\nMatriz por comprensión:")
print(np.array(matriz_comp))


# Otras formas de crear matrices
zeros = np.zeros((3, 3))  # Matriz de ceros
ones = np.ones((2, 4))    # Matriz de unos
full = np.full((3, 5), 7) # Matriz llena de un valor específico
identity = np.eye(3)      # Matriz identidad
random = np.random.rand(2, 4)  # Matriz con valores aleatorios entre 0 y 1

print("\n --- Otras formas de crear matrices ---")
print(f"Matriz de ceros (3x3):\n{zeros}")
print(f"\nMatriz de unos (2x4):\n{ones}")
print(f"\nMatriz llena de 7 (3x5):\n{full}")
print(f"\nMatriz identidad (3x3):\n{identity}")
print(f"\nMatriz con valores aleatorios (2x4):\n{random}")


# Dimensiones y forma de una matriz
print("\n --- Dimensiones y forma de una matriz ---")
print(f"Forma de la matriz numérica: {Numerica.shape}")
print(f"Dimensiones de la matriz numérica: {Numerica.ndim}")
print(f"Tamaño total de la matriz numérica: {Numerica.size}")
print(f"Tipo de datos de la matriz numérica: {Numerica.dtype}")


# Acceso a elementos de una matriz
print("\n --- Acceso a elementos de una matriz ---")
print(f"Elemento en la fila 1, columna 2 de la matriz numérica: {Numerica[1, 2]}")
print(f"Elemento en la fila 0, columna 1 de la matriz de cadenas: {String[0][1]}")
print(f"Primera fila de la matriz numérica: {Numerica[0]}")
print(f"Primera columna de la matriz numérica: {Numerica[:, 0]}")


# Slicing en matrices
print("\n --- Slicing en matrices ---")
print("usando matriz numérica")
print(f"Submatriz (filas 0-1, columnas 1-2):\n{Numerica[0:2, 1:3]}")
print(f"Últimas dos filas de la matriz numérica:\n{Numerica[1:3]}")
print(f"Últimas dos columnas de la matriz numérica:\n{Numerica[:, 1:3]}")


# Modificación de elementos
print("\n --- Modificación de elementos ---")
matriz_modificable = Numerica.copy()
print(f"Matriz original:\n{matriz_modificable}")
matriz_modificable[0, 0] = 99
print(f"Matriz después de modificar un elemento:\n{matriz_modificable}")
matriz_modificable[1:3, 1:3] = [[57, 86], [21, 173]]
print(f"Matriz después de modificar una submatriz:\n{matriz_modificable}")


# Operaciones matemáticas con matrices
print("\n --- Operaciones matemáticas con matrices ---")
A = np.array([[7, 6], [1, 9]])
B = np.array([[2, 3], [3, 5]])
print(f"Matriz A:\n{A}")
print(f"Matriz B:\n{B}")
print(f"Suma de matrices (A + B):\n{A + B}")
print(f"Resta de matrices (A - B):\n{A - B}")
print(f"Multiplicación elemento a elemento (A * B):\n{A * B}")
print(f"División elemento a elemento (A / B):\n{A / B}")
print(f"Multiplicación de matrices (producto matricial A @ B):\n{A @ B}")
print(f"Multiplicación de matrices (producto matricial con np.dot):\n{np.dot(A, B)}")


# Transposición de matrices
print("\n --- Transposición de matrices ---")
print(f"Matriz original A:\n{Numerica}")
print(f"Matriz transpuesta A.T:\n{Numerica.T}")


# Concatenación de matrices
print("\n --- Concatenación de matrices ---")
C = np.array([[9, 8], [7, 6]])
print(f"Matriz A:\n{A}")
print(f"Matriz C:\n{C}")
print(f"Concatenación vertical (filas):\n{np.vstack((A, C))}")
print(f"Concatenación horizontal (columnas):\n{np.hstack((A, C))}")


# Funciones estadísticas en matrices
print("\n --- Funciones estadísticas en matrices ---")
print(f"Matriz numérica:\n{Numerica}")
print(f"Suma de todos los elementos: {np.sum(Numerica)}")
print(f"Suma por filas: {np.sum(Numerica, axis=1)}")
print(f"Suma por columnas: {np.sum(Numerica, axis=0)}")
print(f"Media de todos los elementos: {np.mean(Numerica)}")
print(f"Valor máximo: {np.max(Numerica)}")
print(f"Valor mínimo: {np.min(Numerica)}")
print(f"Desviación estándar: {np.std(Numerica)}")
print(f"Varianza: {np.var(Numerica)}")
print(f"Mediana: {np.median(Numerica)}")
print(f"Percentil 25: {np.percentile(Numerica, 25)}")
print(f"Percentil 75: {np.percentile(Numerica, 75)}")
print(f"Desviación absoluta media: {np.mean(np.abs(Numerica - np.mean(Numerica)))}")
print(f"Desviación absoluta mediana: {np.median(np.abs(Numerica - np.median(Numerica)))}")
print(f"Rango: {np.max(Numerica) - np.min(Numerica)}")


# Producto de Kronecker
print("\n --- Producto de Kronecker ---")
# Crear matrices ejemplo
A = np.array([[1, 2],
              [3, 1]])
B = np.array([[0, 3],
              [2, 1]])

print(f"Matriz A:\n{A}")
print(f"Matriz B:\n{B}")

# Calcular el producto de Kronecker
kron_product = np.kron(A, B)
print("\nProducto de Kronecker A ⊗ B:")
print(kron_product)

# Operaciones avanzadas con matrices
print("\n --- Operaciones avanzadas con matrices ---")

# Creamos una matriz compleja para mostrar todas las operaciones
M = np.array([[2+1j, 3-2j], [1+1j, 4-3j]])
print(f"Matriz compleja M:\n{M}")

# Traza (suma de elementos en la diagonal principal)
trace = np.trace(M)
print(f"\nTraza de M: {trace}")

# Rango de la matriz
rank = np.linalg.matrix_rank(M)
print(f"Rango de M: {rank}")

# Verificar si es simétrica (M = M^T)
is_symmetric = np.array_equal(M, M.T)
print(f"¿M es simétrica?: {is_symmetric}")

# Matriz conjugada (conjugado de cada elemento)
conjugate = np.conjugate(M)
print(f"\nMatriz conjugada de M:\n{conjugate}")

# Matriz transpuesta conjugada (hermitiana o daga)
hermitian = M.conj().T
print(f"\nMatriz transpuesta conjugada (hermitianao o daga) de M:\n{hermitian}")

# Verificar si M * M^(-1) = I
print(f"Matiz inversa de M^-1 = {np.linalg.inv(M)}:")
try:
    inverse = np.linalg.inv(M)
    identity_check = np.allclose(M @ inverse, np.eye(M.shape[0]))
    print(f"\nVerificación M * M^(-1) = I: {identity_check}")
    if identity_check:
        print("Resultado de M * M^(-1):\n", M @ inverse)
except np.linalg.LinAlgError:
    print("\nLa matriz no es invertible")

# Verificar si es ortogonal (M * M^T = I)
orthogonal_check = np.allclose(M @ M.T, np.eye(M.shape[0]))
print(f"¿M es ortogonal? (M * M^T = I): {orthogonal_check}")
print("Resultado de M * M^T:\n", M @ M.T)

# Verificar si es unitaria (M * M^dagger = I)
unitary_check = np.allclose(M @ hermitian, np.eye(M.shape[0]))
print(f"¿M es unitaria? (M * M^dagger = I): {unitary_check}")
print("Resultado de M * M^dagger:\n", M @ hermitian)

# Elevar la matriz a una potencia
power = 3
matrix_power = np.linalg.matrix_power(M, power)
print(f"\nM elevada a la {power}:\n{matrix_power}")

# Ejemplo con matriz real para comparar
print("\n--- Ejemplo con matriz ---")
Q = np.array([
    [np.sqrt(2)/2, -np.sqrt(2)/2, 0],
    [np.sqrt(2)/2,  np.sqrt(2)/2, 0],
    [0,             0,            1j]
])
print(f"Matriz Compleja Q:\n{Q}")
print(f"¿R es simétrica?: {np.array_equal(Q, Q.T)}")
print(f"¿R es ortogonal?: {np.allclose(Q @ Q.T, np.eye(Q.shape[0]))}")
print(f"¿R es unitaria?: {np.allclose(Q @ Q.conj().T, np.eye(Q.shape[0]))}")

Q = (np.sqrt(2) / 2) * np.array([
    [1/2, -np.sqrt(3)/2, -1/2, np.sqrt(3)/2],
    [np.sqrt(3)/2, 1/2, -np.sqrt(3)/2, -1/2],
    [1/2, -np.sqrt(3)/2, 1/2, -np.sqrt(3)/2],
    [np.sqrt(3)/2, 1/2, np.sqrt(3)/2, 1/2]
])
print(f"Matriz real Q:\n{Q}")
print(f"¿R es simétrica?: {np.array_equal(Q, Q.T)}")
print(f"¿R es ortogonal?: {np.allclose(Q @ Q.T, np.eye(Q.shape[0]))}")
print(f"¿R es unitaria?: {np.allclose(Q @ Q.conj().T, np.eye(Q.shape[0]))}")


# Autovalores y autovectores
print("\n --- Autovalores y autovectores ---")
A = np.array([[3, 1], [2, 2]])
print(f"Matriz A:\n{A}")
autovalores, autovectores = np.linalg.eig(A)
print(f"Autovalores: {autovalores}")
print(f"Autovectores:\n{autovectores}") # np.linalg.eig devuelve autovectores con norma 1

autoVector_1 = np.array(autovectores[:,0])
print(f"Verificación (A * v = λ * v):")
print(f"{A} * {autoVector_1} : {np.dot(A, autoVector_1)}")
print(f"{autovalores[0]} * {autoVector_1} = {np.dot(A, autoVector_1)}")


# Determinante y matriz inversa
print("\n --- Determinante y matriz inversa ---")
print(f"Matriz A:\n{A}")
print(f"Determinante de A: {np.linalg.det(A)}")
print(f"Matriz inversa de A:\n{np.linalg.inv(A)}")


# Resolución de sistemas de ecuaciones lineales
print("\n --- Resolución de sistemas de ecuaciones lineales ---")
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
print(f"Sistema de ecuaciones:\n{A} * x = {b}")
x = np.linalg.solve(A, b)
print(f"Solución: x = {x}")
print(f"Verificación: {np.allclose(np.dot(A, x), b)}")


# Matrices triangulares y descomposición LU
print("\n --- Matrices triangulares y descomposición LU ---")

A = np.array([[4, 3, 2], 
              [1, 4, 5], 
              [2, 3, 6]])
print(f"Matriz original A:\n{A}")

# Obtener matriz triangular superior usando eliminación gaussiana
U = np.triu(A)  # triu = triangle upper
print(f"\nMatriz triangular superior:\n{U}")

# Obtener matriz triangular inferior
L = np.tril(A)  # tril = triangle lower
print(f"\nMatriz triangular inferior:\n{L}")

# Descomposición LU
try:
    P, L, U = sp.linalg.lu(A)  # Necesitas importar scipy.linalg
    print(f"\nDescomposición LU:")
    print(f"Matriz de permutación P:\n{P}")
    print(f"Matriz triangular inferior L:\n{L}")
    print(f"Matriz triangular superior U:\n{U}")
    
    # Verificar la descomposición
    print(f"\nVerificación A = P @ L @ U:")
    print(f"Matriz original A:\n{A}")
    print(f"P @ L @ U:\n{P @ L @ U}")
    print(f"¿Son iguales? {np.allclose(A, P @ L @ U)}")
    
except np.linalg.LinAlgError:
    print("No se pudo realizar la descomposición LU")


# Cambio de forma de matrices
print("\n --- Cambio de forma de matrices ---")
vector = np.arange(1, 10)
print(f"Vector original: {vector}")
matriz_3x3 = vector.reshape(3, 3)
print(f"Matriz 3x3:\n{matriz_3x3}")
matriz_3x3_T = matriz_3x3.T
print(f"Matriz 3x3 transpuesta:\n{matriz_3x3_T}")
aplanada = matriz_3x3.flatten()
print(f"Matriz aplanada: {aplanada}")


# Operaciones con matrices de cadenas
print("\n --- Operaciones con matrices de cadenas ---")
print("Matriz de cadenas original:")
print(String)
print("\nConvertir todas las cadenas a mayúsculas:")
print(np.char.upper(String))
print("\nConvertir todas las cadenas a minúsculas:")
print(np.char.lower(String))
print("\nLongitud de cada cadena:")
longitudes = np.vectorize(len)(String)
print(longitudes)


# Máscaras y filtros en matrices
print("\n --- Máscaras y filtros en matrices ---")
matriz = np.array([[1, 5, 3], [4, 2, 6], [7, 8, 9]])
print(f"Matriz original:\n{matriz}")
mascara = matriz > 5
print(f"Máscara (elementos > 5):\n{mascara}")
print(f"Elementos > 5: {matriz[mascara]}")
print(f"Filtrado por condición (elementos pares):\n{matriz[matriz % 2 == 0]}")


# Ejercicio práctico: Operaciones con una matriz de temperaturas
print("\n --- Ejercicio práctico: Matriz de temperaturas ---")
temperaturas = np.array([
    [22, 24, 21, 25, 23, 27, 26],  # Ciudad 1 (días de la semana)
    [19, 21, 20, 22, 24, 25, 23],  # Ciudad 2
    [24, 26, 28, 30, 31, 29, 27]   # Ciudad 3
])
print(f"Matriz de temperaturas (3 ciudades x 7 días):\n{temperaturas}")
print(f"Temperatura promedio por ciudad: {np.mean(temperaturas, axis=1)}")
print(f"Temperatura promedio por día: {np.mean(temperaturas, axis=0)}")
print(f"Ciudad con mayor temperatura promedio: Ciudad {np.argmax(np.mean(temperaturas, axis=1)) + 1}")
print(f"Día más caluroso en promedio: Día {np.argmax(np.mean(temperaturas, axis=0)) + 1}")
print(f"Temperatura máxima registrada: {np.max(temperaturas)}")
print(f"Ubicación de la temperatura máxima: Ciudad {np.unravel_index(np.argmax(temperaturas), temperaturas.shape)[0] + 1}, Día {np.unravel_index(np.argmax(temperaturas), temperaturas.shape)[1] + 1}")