def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de manera recursiva.
    
    Parámetros:
    n (int): El número entero no negativo.
    
    Retorna:
    int: El factorial de n.
    
    Lanza:
    ValueError: Si n no es un entero o es negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.") # raise es para lanzar excepciones de manera manual
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo

def fibonacci(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci de manera recursiva.
    Usa memoización para optimizar el cálculo.
    
    Parámetros:
    n (int): El índice del número de Fibonacci a calcular.
    memo (dict): Un diccionario para almacenar resultados previamente calculados.
    
    Retorna:
    int: El n-ésimo número de Fibonacci.
    
    Lanza:
    ValueError: Si n no es un entero positivo.
    """
    if n < 1:
        raise ValueError("El índice debe ser un entero positivo.")
    if n == 1 or n == 2: # Caso base
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def suma_recursiva(lista):
    """
    Calcula la suma de una lista de números de manera recursiva.
    
    Parámetros:
    lista (list): La lista de números.
    
    Retorna:
    int/float: La suma de los elementos de la lista.
    """
    if not lista:  # Caso base: lista vacía
        return 0
    else:
        return lista[0] + suma_recursiva(lista[1:])  # Caso recursivo

def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números usando el algoritmo de Euclides de manera recursiva.
    
    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.
    
    Retorna:
    int: El MCD de a y b.
    """
    if b == 0:  # Caso base
        return a
    else:
        return mcd(b, a % b)  # Caso recursivo

def potencia(base, exponente):
    """
    Calcula la potencia de un número de manera recursiva.
    
    Parámetros:
    base (int/float): La base.
    exponente (int): El exponente (debe ser no negativo).
    
    Retorna:
    int/float: base elevado a exponente.
    
    Lanza:
    ValueError: Si el exponente es negativo.
    """
    if not isinstance(exponente, int) or exponente < 0:
        raise ValueError("El exponente debe ser un entero no negativo.")
    
    # Caso base
    if exponente == 0:
        return 1
    # Optimización para exponentes pares
    elif exponente % 2 == 0:
        mitad = potencia(base, exponente // 2)
        return mitad * mitad
    # Caso recursivo para exponentes impares
    else:
        return base * potencia(base, exponente - 1)


def invertir_cadena(cadena):
    """
    Invierte una cadena de texto de manera recursiva.
    
    Parámetros:
    cadena (str): La cadena a invertir.
    
    Retorna:
    str: La cadena invertida.
    """
    # Caso base
    if len(cadena) <= 1:
        return cadena
    # Caso recursivo
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])


def contar_elementos(lista):
    """
    Cuenta el número de elementos en una lista de manera recursiva.
    
    Parámetros:
    lista (list): La lista a contar.
    
    Retorna:
    int: El número de elementos en la lista.
    """
    # Caso base
    if not lista:
        return 0
    # Caso recursivo
    else:
        return 1 + contar_elementos(lista[1:])


def encontrar_maximo(lista):
    """
    Encuentra el valor máximo en una lista de manera recursiva.
    
    Parámetros:
    lista (list): La lista de números.
    
    Retorna:
    int/float: El valor máximo en la lista.
    
    Lanza:
    ValueError: Si la lista está vacía.
    """
    if not lista:
        raise ValueError("No se puede encontrar el máximo de una lista vacía.")
    
    # Caso base: lista con un único elemento
    if len(lista) == 1:
        return lista[0]
    
    # Caso recursivo
    mitad = len(lista) // 2
    max_izquierda = encontrar_maximo(lista[:mitad])
    max_derecha = encontrar_maximo(lista[mitad:])
    
    return max_izquierda if max_izquierda > max_derecha else max_derecha


def busqueda_binaria(lista, elemento, inicio=0, fin=None):
    """
    Realiza una búsqueda binaria recursiva en una lista ordenada.
    
    Parámetros:
    lista (list): Lista ordenada donde buscar.
    elemento: El elemento a buscar.
    inicio (int): Índice de inicio para la búsqueda.
    fin (int): Índice final para la búsqueda.
    
    Retorna:
    int: El índice del elemento si se encuentra, -1 en caso contrario.
    """
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: elemento no encontrado
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = (inicio + fin) // 2
    
    # Caso base: elemento encontrado
    if lista[medio] == elemento:
        return medio
    # Caso recursivo: buscar en la mitad izquierda
    elif lista[medio] > elemento:
        return busqueda_binaria(lista, elemento, inicio, medio - 1)
    # Caso recursivo: buscar en la mitad derecha
    else:
        return busqueda_binaria(lista, elemento, medio + 1, fin)


def palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo de manera recursiva.
    
    Parámetros:
    cadena (str): La cadena a verificar.
    
    Retorna:
    bool: True si es palíndromo, False en caso contrario.
    """
    # Normalizar la cadena: minúsculas y sin espacios
    cadena = cadena.lower().replace(" ", "")
    
    # Caso base: cadena vacía o de un carácter
    if len(cadena) <= 1:
        return True
    
    # Verificar si el primer y último carácter son iguales
    if cadena[0] != cadena[-1]:
        return False
    
    # Caso recursivo: verificar el resto de la cadena
    return palindromo(cadena[1:-1])


def torres_hanoi(n, origen, auxiliar, destino):
    """
    Resuelve el problema de las Torres de Hanoi de manera recursiva.
    
    Parámetros:
    n (int): Número de discos.
    origen (str): La torre de origen.
    auxiliar (str): La torre auxiliar.
    destino (str): La torre de destino.
    
    Retorna:
    list: Lista de movimientos a realizar.
    """
    movimientos = []
    
    def hanoi_recursivo(n, origen, auxiliar, destino):
        if n == 1:
            movimientos.append(f"Mover disco 1 desde {origen} hasta {destino}")
        else:
            hanoi_recursivo(n-1, origen, destino, auxiliar)
            movimientos.append(f"Mover disco {n} desde {origen} hasta {destino}")
            hanoi_recursivo(n-1, auxiliar, origen, destino)
    
    hanoi_recursivo(n, origen, auxiliar, destino)
    return movimientos


def visualizar_recursion(func, n, nivel=0, prefijo=""):
    """
    Función auxiliar para visualizar la pila de llamadas recursivas.
    
    Parámetros:
    func (function): La función recursiva a visualizar.
    n (int): El valor de entrada para la función.
    nivel (int): El nivel de recursión actual.
    prefijo (str): Prefijo para la visualización.
    
    Retorna:
    El resultado de la función recursiva.
    """
    indent = "  " * nivel
    print(f"{indent}→ {prefijo}({n})")
    
    if n <= 1:
        print(f"{indent}← {prefijo}({n}) = 1")
        return 1
    
    resultado = func(n)
    print(f"{indent}← {prefijo}({n}) = {resultado}")
    return resultado


# Programa principal
if __name__ == "__main__":
    print("\n=== INTRODUCCIÓN A LA RECURSIVIDAD EN PYTHON ===")
    print("La recursividad es una técnica donde una función se llama a sí misma para resolver un problema.")
    print("Componentes clave de una función recursiva:")
    print("1. Caso base: Condición que detiene la recursión")
    print("2. Caso recursivo: La función se llama a sí misma con un problema más pequeño")
    print("3. Acercamiento al caso base: Cada llamada debe acercarse al caso base")
    
    # Ejemplos
    print("\n=== EJEMPLOS DE FUNCIONES RECURSIVAS ===")
    
    print("\n--- Factoriales ---")
    for i in range(0, 11):
        print(f"{i}! = {factorial(i)}")

    print("\n--- Secuencia de Fibonacci ---")
    for i in range(1, 21):  # Ampliado a 20 términos
        print(f"fibonacci_{i} = {fibonacci(i)}")

    lista = [1, 2, 3, 4, 5]
    print(f"\n--- Suma recursiva ---")
    print(f"Suma de {lista}: {suma_recursiva(lista)}")

    a, b = 48, 18
    print(f"\n--- Máximo Común Divisor (MCD) ---")
    print(f"MCD de {a} y {b}: {mcd(a, b)}")
    
    print(f"\n--- Potencia recursiva ---")
    base, exp = 2, 10
    print(f"{base}^{exp} = {potencia(base, exp)}")
    
    print(f"\n--- Invertir cadena ---")
    texto = "Python es divertido"
    print(f'"{texto}" invertido: "{invertir_cadena(texto)}"')
    
    print(f"\n--- Contar elementos ---")
    lista_grande = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(f"Número de elementos en {lista_grande}: {contar_elementos(lista_grande)}")
    
    print(f"\n--- Encontrar máximo ---")
    lista_desordenada = [15, 7, 23, 4, 19, 8]
    print(f"Máximo en {lista_desordenada}: {encontrar_maximo(lista_desordenada)}")
    
    print(f"\n--- Búsqueda binaria ---")
    lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    elemento = 12
    indice = busqueda_binaria(lista_ordenada, elemento)
    if indice != -1:
        print(f"El elemento {elemento} se encuentra en el índice {indice} de {lista_ordenada}")
    else:
        print(f"El elemento {elemento} no se encuentra en {lista_ordenada}")
    
    print(f"\n--- Palíndromos ---")
    frases = ["anita lava la tina", "python", "radar", "reconocer"]
    for frase in frases:
        resultado = "es" if palindromo(frase) else "no es"
        print(f'"{frase}" {resultado} un palíndromo')
    
    print(f"\n--- Torres de Hanoi ---")
    num_discos = 3
    movimientos = torres_hanoi(num_discos, "A", "B", "C")
    print(f"Solución para {num_discos} discos:")
    for i, movimiento in enumerate(movimientos, 1):
        print(f"{i}. {movimiento}")
    
    print("\n=== VISUALIZACIÓN DE LA RECURSIÓN ===")
    print("Ejemplo de visualización para factorial(4):")
    
    def factorial_vis(n):
        return visualizar_recursion(lambda x: x * factorial_vis(x-1) if x > 1 else 1, n, prefijo="factorial")
        # lamda es una pequeña funcion que se puede definir en una sola linea
    
    factorial_vis(4)