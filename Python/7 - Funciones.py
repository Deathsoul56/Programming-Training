# Definir funciones con def

# 1. Función básica sin parámetros
def saludar():
    """Imprime un mensaje de bienvenida."""
    print("¡Hola, bienvenido la clase de funciones de Python!")

# 2. Función con parámetros
def funcion (x):
    return x + 5

# 3. Funcion con varios parametros
def funcion2 (x, y):
    z = x - y   # Las variables que se crean en una funcion solo exsiten en la funcion
    return z

# 4. Función con múltiples valores de retorno
def calcular_estadisticas(numeros):
    """Calcula la suma, promedio, máximo y mínimo de una lista de números."""
    suma = sum(numeros)
    promedio = suma / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    return suma, promedio, maximo, minimo

# 5. Funcion que devuelve el caracter mas repetido de un String
def caracter_mas_repetido(cadena):
    if not cadena:
        return None
    
    # Crear un diccionario para contar la frecuencia de cada carácter
    frecuencias = {}
    for char in cadena:
        if char in frecuencias and char != ' ':
            frecuencias[char] += 1
        else:
            frecuencias[char] = 1
    
    # Encontrar el carácter con la mayor frecuencia
    max_char = max(frecuencias, key=frecuencias.get)
    
    return max_char

# 6. Función con parámetros por defecto
def saludar_persona(nombre="Invitado"):
    """Saluda a una persona usando un valor por defecto si no se proporciona nombre."""
    return f"Hola {nombre}!"

# 7. Función con argumentos variables (*args)
def sumar_numeros(*numeros):
    """Suma una cantidad variable de números."""
    return sum(numeros)

# 8. Función con argumentos de palabra clave variables (**kwargs)
def info_persona(**datos):
    """Muestra información de una persona con pares clave-valor variables."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# 9. Función con decorador para medir tiempo de ejecución
from time import time
def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time()
        resultado = funcion(*args, **kwargs)
        fin = time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return wrapper

# 10. Decorador aplicado a una función
@medir_tiempo # Decorador para medir tiempo de ejecución. la función se ejecuta antes de la decoradora
def operacion_lenta():
    return sum(range(10000000))

# Programa principal
if __name__ == '__main__':
    saludar() # Invocar la funcion
    print(f'Comienzo del programa {funcion(5)}')
    
    valor1 = 10
    valor2 = 4
    valor3 = funcion2(valor1, valor2)
    print(valor3)

    vector = [15, 23, 20, 11, 9, 16, 15, 22, 30, 17]
    suma, promedio, max_num, min_num = calcular_estadisticas(vector)
    print(f"Suma: {suma}, Promedio: {promedio:.2f}, Máximo: {max_num}, Mínimo: {min_num}")
    print(f'Estadisticas: {calcular_estadisticas(vector)}')

    x = "Mi nombre es Máximo decimo Meridio, comandante de los ejércitos del norte, general de las legiones Félix. leal, sirviente del único emperador Marco Aurelio, padre de un hijo asesinado, esposo de una esposa asesinada. Y juro que me vengaré. en esta vida o en la otra."
    resultado = caracter_mas_repetido(x)
    print(f"El carácter que más se repite en '{x}' \nes '{resultado}'")

    suma = sumar_numeros(1, 2, 3)  # Suma números fijos
    print(f"La suma de (1, 2, 3) es: {suma}")  # Suma números variables
    
    info_persona(nombre="Juan", edad=30, ciudad="Madrid")  # Kwargs ejemplo

    # Los decoradores sirven para añadir funcionalidades a funciones ya definidas
    # sin modificar su código. Se utilizan para añadir funcionalidades a funciones ya definidas
    operacion_lenta()