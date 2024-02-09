import numpy as np

# Numeros Pseudo-Aleatorios
aleatorio = np.random.random() # Numero aleatorio entre 0 y 1
print(f'Numero aleatorio entre 0 y 1: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1) # Numero aleatorio entre -10 y 10, el intervalor es cerrado-abierto [)
print(f'Numero aleatorio: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = 10) # Vector 10 numeros aleatorios
print(f'vector aletario: {aleatorio}')

aleatorio = np.random.sample(5) # Muestra de 5 valores aleatorios 
print(f'Muestra aleatorio: {aleatorio}')

aleatorio = np.random.bytes(12) # Bytes aleatorios 
print(f'Bytes Aleatorios: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = (4, 3)) # Matriz 2x3 aleatorios
print(f'Matris aletario: {aleatorio}')

aleatorio = np.random.rand(2, 2)  # Genera una matriz de 2x2 con números aleatorios entre 0 y 1.
print(f'Matris aletario entre 0 y 1: {aleatorio}')

vector = np.array([7, -4, -3,  7,  9,  7,  0, -5,  3,  3])
v = np.random.choice(vector)
print(f'El vector v = {vector} se escoge al azar un valor {v}')

# Permutations
lista = np.array(["rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"])
print(f'Lista Original = {lista}')
np.random.shuffle(lista) # Funciones para revolver un array
print(f'Lista revuelta = {lista}')

secuencia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Secuencia original: {secuencia}")
permutacion = np.random.permutation(secuencia) # Generamos una permutación aleatoria de la secuencia
print(f"Permutación aleatoria: {permutacion}")


# Distribuciones de probabilidad continuas
# Distribucion Normal
mu = 5
sd = 8
normal = np.random.normal(mu, sd) # Valor aleatorio con distribcion normal (media, Sx)
print(f'Valor aleatorio con distribucion normal media: {mu} desviacion estandar {sd} = {normal}')

normal = np.random.normal(mu, sd, 10) # Vector aleatorio con distribcion normal (media, Sx)
print(f'Vector aleatorio con distribucion normal media: {mu} desviacion estandar {sd} = {normal}')

# Distribucion normal estandar
normalS = np.random.standard_normal() # Valor aleatorio con distribcion normal (media = 0, Sx = 1)
print(f'Valor aleatorio con distribucion normal estandar = {normalS}')

normalS = np.random.standard_normal(10) # Vector aleatorio con distribcion normal (media = 0, Sx = 1)
print(f'Vector aleatorio con distribucion normal estandar = {normalS}')