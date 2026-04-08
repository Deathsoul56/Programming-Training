print("=== 14. MÓDULOS E IMPORTACIONES ===")

# Los módulos son archivos de Python que contienen código reutilizable
# Nos permiten organizar nuestro código y usar librerías externas

print("\n--- ¿Qué son los módulos? ---")
print("Un módulo es un archivo .py que contiene definiciones y declaraciones de Python")
print("Los módulos nos ayudan a:")
print("- Organizar el código en archivos separados")
print("- Reutilizar código en diferentes programas")
print("- Usar librerías externas")
print("- Evitar repetir código")

print("\n--- Formas de importar módulos ---")

# 1. Importar todo el módulo
import math
print(f"π usando math.pi: {math.pi}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")

# 2. Importar funciones específicas
from math import sin, cos, pi
print(f"Sen(π/2): {sin(pi/2)}")
print(f"Cos(0): {cos(0)}")

# 3. Importar con alias
import datetime as dt
ahora = dt.datetime.now()
print(f"Fecha y hora actual: {ahora}")

# 4. Importar todo con * (no recomendado en general)
# from math import *  # Importa todas las funciones

print("\n--- Módulos de la librería estándar ---")

# Módulo random
import random
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Número aleatorio entre 1 y 100: {random.randint(1, 100)}")
print(f"Elemento aleatorio de la lista: {random.choice(numeros)}")
print(f"Lista mezclada: {random.sample(numeros, len(numeros))}")

# Módulo os (sistema operativo)
import os
print(f"Directorio actual: {os.getcwd()}")
print(f"Listado de archivos Python: {[f for f in os.listdir('.') if f.endswith('.py')]}")

# Módulo sys (sistema)
import sys
print(f"Versión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")

print("\n--- Crear nuestros propios módulos ---")

# Creemos un módulo personalizado
modulo_matematicas = '''# mi_matematicas.py
"""
Módulo personalizado con funciones matemáticas básicas
"""

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(base, exponente):
    """Calcula base elevado a exponente"""
    return base ** exponente

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Variable del módulo
PI = 3.141592653589793

# Esta función se ejecuta solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    print("Probando el módulo mi_matematicas...")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 * 7 = {multiplicar(6, 7)}")
    print(f"15 / 3 = {dividir(15, 3)}")
    print(f"2^8 = {potencia(2, 8)}")
    print(f"5! = {factorial(5)}")
    print(f"Valor de PI: {PI}")
'''

# Escribir el módulo a un archivo
with open('mi_matematicas.py', 'w', encoding='utf-8') as f:
    f.write(modulo_matematicas)

print("Módulo 'mi_matematicas.py' creado exitosamente")

# Ahora podemos importar nuestro módulo
import mi_matematicas

print(f"Usando nuestro módulo: 8 + 5 = {mi_matematicas.sumar(8, 5)}")
print(f"Factorial de 6: {mi_matematicas.factorial(6)}")
print(f"PI desde nuestro módulo: {mi_matematicas.PI}")

print("\n--- Importar funciones específicas de nuestro módulo ---")
from mi_matematicas import multiplicar, potencia, PI

print(f"12 * 7 = {multiplicar(12, 7)}")
print(f"3^4 = {potencia(3, 4)}")
print(f"Valor de PI: {PI}")

print("\n--- __name__ == '__main__' ---")
print("Esta condición es verdadera solo cuando el archivo se ejecuta directamente")
print("No cuando se importa como módulo")
print("Es útil para código de prueba que solo se ejecuta al correr el archivo")

# Ejemplo de uso
if __name__ == "__main__":
    print("Este mensaje aparece porque este archivo se está ejecutando directamente")

print("\n--- Crear un paquete (package) ---")

# Un paquete es una carpeta que contiene módulos
# Debe tener un archivo __init__.py (puede estar vacío)

# Crear estructura de paquete
import os

# Crear directorio del paquete
if not os.path.exists('mi_paquete'):
    os.makedirs('mi_paquete')

# Crear __init__.py
init_content = '''"""
Mi paquete personalizado para operaciones matemáticas y de texto
"""

# Importar funciones principales para facilitar el acceso
from .operaciones import sumar, restar
from .texto import capitalizar, contar_palabras

__version__ = "1.0.0"
__author__ = "Tu Nombre"
'''

with open('mi_paquete/__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_content)

# Crear módulo de operaciones
operaciones_content = '''"""
Módulo de operaciones matemáticas
"""

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def es_par(numero):
    """Verifica si un número es par"""
    return numero % 2 == 0
'''

with open('mi_paquete/operaciones.py', 'w', encoding='utf-8') as f:
    f.write(operaciones_content)

# Crear módulo de texto
texto_content = '''"""
Módulo para operaciones con texto
"""

def capitalizar(texto):
    """Capitaliza cada palabra del texto"""
    return ' '.join(palabra.capitalize() for palabra in texto.split())

def contar_palabras(texto):
    """Cuenta las palabras en un texto"""
    return len(texto.split())

def invertir_texto(texto):
    """Invierte el texto"""
    return texto[::-1]

def es_palindromo(texto):
    """Verifica si un texto es palíndromo"""
    texto_limpio = texto.lower().replace(' ', '')
    return texto_limpio == texto_limpio[::-1]
'''

with open('mi_paquete/texto.py', 'w', encoding='utf-8') as f:
    f.write(texto_content)

print("Paquete 'mi_paquete' creado exitosamente")

# Usar el paquete
import mi_paquete

print(f"Suma usando el paquete: {mi_paquete.sumar(10, 15)}")
print(f"Capitalizar texto: {mi_paquete.capitalizar('hola mundo python')}")

# Importar módulos específicos del paquete
from mi_paquete.operaciones import es_par
from mi_paquete.texto import es_palindromo

print(f"¿Es 8 par? {es_par(8)}")
print(f"¿Es 'anilina' palíndromo? {es_palindromo('anilina')}")

print("\n--- sys.path y PYTHONPATH ---")
print("sys.path es la lista de directorios donde Python busca módulos")
print("Los primeros elementos de sys.path:")
for i, path in enumerate(sys.path[:5]):
    print(f"  {i+1}. {path}")

print("\n--- Módulos útiles de la librería estándar ---")

modulos_utiles = {
    "datetime": "Trabajar con fechas y horas",
    "json": "Leer y escribir archivos JSON",
    "csv": "Trabajar con archivos CSV",
    "sqlite3": "Base de datos SQLite",
    "urllib": "Trabajar con URLs",
    "re": "Expresiones regulares",
    "pathlib": "Manipulación de rutas de archivos",
    "collections": "Tipos de datos especializados",
    "itertools": "Herramientas para iteradores",
    "functools": "Herramientas para funciones de orden superior"
}

for modulo, descripcion in modulos_utiles.items():
    print(f"{modulo}: {descripcion}")

print("\n--- Ejemplo con módulo collections ---")
from collections import Counter, defaultdict, deque

# Counter - contar elementos
texto = "python es genial y python es poderoso"
contador = Counter(texto.split())
print(f"Contador de palabras: {contador}")
print(f"Palabra más común: {contador.most_common(1)}")

# defaultdict - diccionario con valores por defecto
dd = defaultdict(list)
dd['frutas'].append('manzana')
dd['frutas'].append('pera')
dd['verduras'].append('zanahoria')
print(f"defaultdict: {dict(dd)}")

# deque - lista doblemente enlazada
cola = deque(['a', 'b', 'c'])
cola.appendleft('z')
cola.append('d')
print(f"deque: {cola}")

print("\n--- Ejemplo con módulo itertools ---")
import itertools

# Combinaciones
numeros = [1, 2, 3, 4]
combinaciones = list(itertools.combinations(numeros, 2))
print(f"Combinaciones de 2 elementos: {combinaciones}")

# Permutaciones
permutaciones = list(itertools.permutations(['A', 'B', 'C'], 2))
print(f"Permutaciones de 2 elementos: {permutaciones}")

# Ciclo infinito (cuidado!)
contador_infinito = itertools.count(start=10, step=2)
primeros_5 = [next(contador_infinito) for _ in range(5)]
print(f"Primeros 5 números del contador: {primeros_5}")

print("\n--- Recarga de módulos ---")
print("En desarrollo, puedes recargar un módulo con importlib.reload()")

import importlib
# importlib.reload(mi_matematicas)  # Recarga el módulo si ha cambiado

print("\n--- Mejores prácticas ---")
print("1. Usa nombres descriptivos para tus módulos")
print("2. Incluye docstrings en tus módulos y funciones")
print("3. Organiza código relacionado en paquetes")
print("4. Usa __init__.py para controlar qué se importa")
print("5. Evita import * en código de producción")
print("6. Usa import al inicio del archivo")
print("7. Agrupa imports: estándar, terceros, locales")

print("\n--- Gestión de dependencias ---")
print("pip: Instalador de paquetes de Python")
print("requirements.txt: Lista de dependencias del proyecto")
print("virtual environments: Entornos aislados para proyectos")

# Ejemplo de requirements.txt
requirements_example = '''# requirements.txt
numpy>=1.20.0
pandas>=1.3.0
matplotlib>=3.4.0
requests>=2.25.0
'''

print("Ejemplo de requirements.txt:")
print(requirements_example)

print("Comandos útiles:")
print("pip install package_name")
print("pip install -r requirements.txt")
print("pip freeze > requirements.txt")
print("pip list")

print("\n--- Limpieza ---")
# Limpiar archivos creados
archivos_a_limpiar = [
    'mi_matematicas.py',
    'mi_paquete/__init__.py',
    'mi_paquete/operaciones.py',
    'mi_paquete/texto.py'
]

for archivo in archivos_a_limpiar:
    try:
        os.remove(archivo)
    except FileNotFoundError:
        pass

try:
    os.rmdir('mi_paquete')
except OSError:
    pass

print("Archivos de ejemplo limpiados")

print("\n--- Resumen ---")
print("✓ import modulo - importa todo el módulo")
print("✓ from modulo import funcion - importa función específica")
print("✓ import modulo as alias - importa con alias")
print("✓ Crear módulos propios con .py")
print("✓ Crear paquetes con carpetas y __init__.py")
print("✓ __name__ == '__main__' para código de prueba")
print("✓ sys.path controla dónde busca Python los módulos")
print("✓ Muchos módulos útiles en la librería estándar")