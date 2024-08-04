import numpy as np
from prettytable import PrettyTable

# Función para imprimir una matriz usando PrettyTable
def print_matrix(matrix, title):
    table = PrettyTable()
    table.title = title
    table.field_names = ["", *range(matrix.shape[1])]
    for i, row in enumerate(matrix):
        table.add_row([i, *row])
    print(table)


vector2d = np.array([3, 4])
vector3d = np.array([7, 4, 6])
vector3d = np.array([8, 14, 7, 11])

matrix = np.matrix('2 4; 3 7') # Forma antigua de definir matrices, no se recomienda, se mantiene para compatibilidad con codigos antiguos
matrix = np.array([[2, 4], [3, 7]]) # Forma nueva de definir matrices
matrix_1 = np.array([[6, 8], [12, 9]])


print_matrix(matrix, "Matriz de prueba")


# Operaciones de Vectores
# Define los vectores
v1 = np.array([7, 4, 6])
v2 = np.array([5, 9, 8])

# Calcula el producto punto y producto cruz
producto_punto = np.dot(v1, v2)
producto_cruz = np.cross(v1, v2)

print(f"El producto punto entre {v1} y {v2} es: {producto_punto}")
print(f"El producto cruz entre {v1} y {v2} es: {producto_cruz}")



# Operaciones de Matrices

# Define las matrices
matriz1 = np.array([[11, 5, 13, 9], [6, 9, 14, 11], [9, 4, 5, 3]])
matriz2 = np.array([[5, 3], [9, 4], [10, 3], [13, 5]])

# Multiplica las matrices
resultado = np.dot(matriz1, matriz2)
resultado2 = matriz1 @ matriz2

print(f"El resultado de la multiplicación de las matrices {matriz1} y {matriz2}:")
print(resultado)
print(resultado2)