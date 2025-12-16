print("=== 13. EXCEPCIONES Y MANEJO DE ERRORES ===")

# Las excepciones son errores que ocurren durante la ejecución del programa
# Python nos permite manejar estos errores para que el programa no se detenga abruptamente

print("\n--- ¿Qué son las excepciones? ---")
print("Las excepciones son eventos que interrumpen el flujo normal del programa")
print("Ejemplos: dividir por cero, acceder a un archivo inexistente, índice fuera de rango")

print("\n--- Estructura básica: try/except ---")

# Ejemplo básico de manejo de excepciones
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"10 dividido entre {numero} es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except ValueError:
    print("Error: Debes ingresar un número válido")

print("\n--- Capturar múltiples excepciones ---")

def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División entre cero")
        return None
    except TypeError:
        print("Error: Los argumentos deben ser números")
        return None

# Ejemplos de uso
print("Resultado 1:", dividir_numeros(10, 2))
print("Resultado 2:", dividir_numeros(10, 0))
print("Resultado 3:", dividir_numeros(10, "abc"))

print("\n--- Except genérico ---")

def operacion_riesgosa(datos):
    try:
        # Operación que puede fallar de varias maneras
        return datos[0] * datos[1] / datos[2]
    except Exception as e:
        print(f"Ocurrió un error: {type(e).__name__}: {e}")
        return None

# Ejemplos que causarán diferentes errores
print("Test 1:", operacion_riesgosa([10, 5, 2]))  # Funciona
print("Test 2:", operacion_riesgosa([10, 5, 0]))  # ZeroDivisionError
print("Test 3:", operacion_riesgosa([10, 5]))     # IndexError
print("Test 4:", operacion_riesgosa("abc"))       # TypeError

print("\n--- try/except/else/finally ---")

def leer_archivo_demo(nombre_archivo):
    archivo = None
    try:
        print(f"Intentando abrir: {nombre_archivo}")
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
        contenido = archivo.read()
        print("Archivo leído exitosamente")
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
        return None
    except PermissionError:
        print(f"Error: No tienes permisos para leer '{nombre_archivo}'")
        return None
    else:
        # Se ejecuta solo si NO hubo excepciones
        print("No hubo errores al leer el archivo")
    finally:
        # Se ejecuta SIEMPRE, haya o no excepciones
        if archivo and not archivo.closed:
            archivo.close()
            print("Archivo cerrado correctamente")
        print("Operación de lectura finalizada")

# Crear un archivo de prueba
with open('prueba.txt', 'w', encoding='utf-8') as f:
    f.write("Contenido de prueba\nSegunda línea")

# Probar la función
leer_archivo_demo('prueba.txt')
print()
leer_archivo_demo('archivo_inexistente.txt')

print("\n--- Tipos de excepciones comunes ---")

excepciones_comunes = {
    "ValueError": "Valor incorrecto para el tipo de dato",
    "TypeError": "Tipo de dato incorrecto",
    "IndexError": "Índice fuera del rango de la lista",
    "KeyError": "Clave no encontrada en diccionario",
    "FileNotFoundError": "Archivo no encontrado",
    "ZeroDivisionError": "División entre cero",
    "AttributeError": "Atributo o método no existe",
    "ImportError": "Error al importar módulo"
}

for excepcion, descripcion in excepciones_comunes.items():
    print(f"{excepcion}: {descripcion}")

print("\n--- Ejemplos de excepciones comunes ---")

# ValueError
try:
    numero = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# IndexError
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    diccionario = {"nombre": "Juan", "edad": 25}
    print(diccionario["altura"])
except KeyError as e:
    print(f"KeyError: {e}")

# AttributeError
try:
    numero = 42
    numero.append(1)  # Los números no tienen método append
except AttributeError as e:
    print(f"AttributeError: {e}")

print("\n--- Lanzar excepciones personalizadas con raise ---")

def validar_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad no puede ser mayor a 150 años")
    return True

# Probar la función
def probar_edad(edad):
    try:
        validar_edad(edad)
        print(f"Edad {edad} es válida")
    except (TypeError, ValueError) as e:
        print(f"Error de validación: {e}")

probar_edad(25)
probar_edad(-5)
probar_edad(200)
probar_edad("veinticinco")

print("\n--- Crear excepciones personalizadas ---")

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades inválidas"""
    def __init__(self, edad, mensaje="Edad inválida"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class SaldoInsuficienteError(Exception):
    """Excepción para operaciones bancarias con saldo insuficiente"""
    def __init__(self, saldo_actual, cantidad_solicitada):
        self.saldo_actual = saldo_actual
        self.cantidad_solicitada = cantidad_solicitada
        mensaje = f"Saldo insuficiente. Saldo: ${saldo_actual:.2f}, Solicitado: ${cantidad_solicitada:.2f}"
        super().__init__(mensaje)

# Usar excepciones personalizadas
def crear_persona(nombre, edad):
    try:
        if edad < 0:
            raise EdadInvalidaError(edad, "La edad no puede ser negativa")
        elif edad > 130:
            raise EdadInvalidaError(edad, "La edad es demasiado alta")
        return {"nombre": nombre, "edad": edad}
    except EdadInvalidaError as e:
        print(f"Error al crear persona: {e}")
        return None

def retirar_dinero(saldo, cantidad):
    try:
        if cantidad > saldo:
            raise SaldoInsuficienteError(saldo, cantidad)
        return saldo - cantidad
    except SaldoInsuficienteError as e:
        print(f"Error en retiro: {e}")
        return saldo

# Ejemplos de uso
persona1 = crear_persona("Ana", 25)
persona2 = crear_persona("Luis", -10)
persona3 = crear_persona("María", 150)

print(f"Persona 1: {persona1}")

nuevo_saldo = retirar_dinero(100.0, 150.0)
print(f"Nuevo saldo: ${nuevo_saldo:.2f}")

print("\n--- Mejores prácticas ---")
print("1. Sé específico con las excepciones que capturas")
print("2. No uses except: sin especificar la excepción")
print("3. Usa finally para limpiar recursos")
print("4. Registra errores para debugging")
print("5. No ignores excepciones silenciosamente")

print("\n--- Ejemplo de logging de errores ---")
import traceback
import sys
from datetime import datetime

def log_error(error, contexto=""):
    """Función simple para registrar errores"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[ERROR - {timestamp}] {contexto}")
    print(f"Tipo de error: {type(error).__name__}")
    print(f"Mensaje: {error}")
    print("Traceback:")
    traceback.print_exc()

def operacion_compleja(x, y):
    try:
        # Simulamos una operación que puede fallar
        if x < 0:
            raise ValueError("x no puede ser negativo")
        resultado = (x ** 2 + y ** 2) ** 0.5
        division = resultado / (x - y)
        return division
    except Exception as e:
        log_error(e, f"Error en operacion_compleja({x}, {y})")
        return None

# Ejemplos que generarán errores
operacion_compleja(-5, 3)
operacion_compleja(5, 5)  # División por cero

print("\n--- Context managers (with statement) ---")
print("El statement 'with' garantiza que los recursos se liberen correctamente")

# Ejemplo con archivos
try:
    with open('datos_temp.txt', 'w', encoding='utf-8') as archivo:
        archivo.write("Datos temporales\n")
        archivo.write("Segunda línea\n")
        # El archivo se cierra automáticamente
    print("Archivo creado y cerrado automáticamente")
except Exception as e:
    print(f"Error al crear archivo: {e}")

# Leer el archivo
try:
    with open('datos_temp.txt', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(f"Contenido leído:\n{contenido}")
except FileNotFoundError:
    print("El archivo no existe")

print("\n--- Debugging tips ---")
print("1. Lee el traceback de abajo hacia arriba")
print("2. Usa print() statements para debugging básico")
print("3. El módulo pdb te permite debugging interactivo")
print("4. Los IDEs modernos tienen debuggers visuales")

# Limpieza de archivos de prueba
import os
try:
    os.remove('prueba.txt')
    os.remove('datos_temp.txt')
    print("\nArchivos de prueba eliminados")
except FileNotFoundError:
    pass

print("\n--- Resumen ---")
print("✓ try/except para manejar errores")
print("✓ else se ejecuta si no hay errores")
print("✓ finally se ejecuta siempre")
print("✓ raise para lanzar excepciones")
print("✓ Crear excepciones personalizadas")
print("✓ Logging para debugging")
print("✓ Context managers con 'with'")