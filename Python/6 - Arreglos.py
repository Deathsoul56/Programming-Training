import numpy as np

Numerico = np.array([3, 6, 8, 3, 13, 63, 17, 56, 234, 21, 73, 13, 8, 37, 64, 10, 15])
Flotante = np.array([3.1415, 2.7154, 8.2326])
String = np.array(['Rojo', 'Verde', 'Azul', 'Negro', 'Blanco', 'Cafe'])
Cadena = np.array([2, 'Gauss', 3.1415, 'Noether', 17, 31, 73, 'Newton'])

# Ordenar
print(Numerico)
Numerico.sort()
print(Numerico)

print(String)
String.sort()
print(String)

print(Cadena)
Cadena.sort()
print(Cadena)

# Crear una copia antes de ordenar
Numerico_ordenado = np.sort(Numerico)
print("Arreglo original:", Numerico)
print("Arreglo ordenado:", Numerico_ordenado)


# Indices
print(f"Elemento en la posición 2: {Numerico[2]}") # Imprimer el elemento en la posicion 2

for i in range(len(Flotante)):
    print(f"El valor {i} = {Flotante[i]}")

for indice, valor in enumerate(Flotante):
    print(f"El valor en la posición {indice} = {valor}")

print(Numerico[2:6]) # Imprimer un array con los elementos que esten en la posicion 2 a la 6 [2, 6)
print(Numerico[:6]) # Imprimer un array con los elementos que esten en la posicion 2 a la 6 [0, 6)
print(Numerico[8:]) # Imprimer un array con los elementos que esten en la posicion 8 a la ultima [8, Ultima)
print(Numerico[0:-1]) # Imprimer un array con los elementos que esten en la posicion 0 a la pen-ultima [8, pen-Ultima)
print(Numerico[:]) # Imprimer todo el array

print(f"Subarreglo de la posición 2 a la 6: {Numerico[2:6]}") # Imprimer un array con los elementos 2 y los elementos con 6 posiciones de diferencia [2 ; 2+6 ; 2+6*2]
print(Numerico[1::5]) # Imprimer un array con los elementos 1 y los elementos con 5 posiciones de diferencia [1 ; 1+5; 1+5*2 ; 1+5*3]


# Agregar y quitar datos
Flotante = np.append(Flotante, 65.2345)
print(Flotante)
Flotante = np.delete(Flotante, 2)
print(Flotante)


# Combertir de Array a String
saludo = np.array(['h', 'o', 'l', 'a'])
juntar = ''.join(saludo)
juntar2 = '-'.join(saludo)
print(juntar, juntar2)

# Concatenar arreglos
concatenado = np.concatenate((Numerico, Flotante))
print("Arreglos concatenados:", concatenado)

# Buscar un elemento en el arreglo
if 13 in Numerico:
    print("El número 13 está en el arreglo.")
else:
    print("El número 13 no está en el arreglo.")

# Convertir a mayúsculas
String_mayusculas = np.char.upper(String)
print("Arreglo de cadenas en mayúsculas:", String_mayusculas)


# Crear un array con números del 3 al 15 usando np.arange
numeros = np.arange(3, 16) # forma la eficiente

print("Array con números del 3 al 15:", numeros)

# Crear un array con números del 3 al 15 usando range
numeros = np.array(range(3, 16))

# Lista por comprension 
numeros = np.array([i for i in range(3, 16)])

# Las lista son mutables
a = np.array([1, 2, 3])
b = a
b[0] = 10
print(a)
print(b) # Ambos arreglos son iguales

