import numpy as np

# Definir funciones
def funcion (x):
    return x + 5

def funcion2 (x, y):
    z = x - y   # Las variables que se crean en una funcion solo exsiten en la funcion
    return z

# Funcion que devuelve el caracter mas repetido de un String
def caracter_mas_repetido(cadena):
    if not cadena:
        return None
    
    # Crear un diccionario para contar la frecuencia de cada carácter
    frecuencias = {}
    for char in cadena:
        if char in frecuencias and char != '':
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    
    # Encontrar el carácter con la mayor frecuencia
    max_char = max(frecuencias, key=frecuencias.get)
    
    return max_char


# Programa principal
if __name__ == '__main__':
    print(f'Comienzo del programa {funcion(5)}') # Invocar la funcion
    
    valor1 = 10
    valor2 = 4
    valor3 = funcion2(valor1, valor2)
    print(valor3)

    x = "Mi nombre es Máximo decimo Meridio, comandante de los ejércitos del norte, general de las legiones Félix. leal, sirviente del único emperador Marco Aurelio, padre de un hijo asesinado, esposo de una esposa asesinada. Y juro que me vengaré. en esta vida o en la otra."
    resultado = caracter_mas_repetido(x)
    print(f"El carácter que más se repite en '{x}' es '{resultado}'")