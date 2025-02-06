# Si condicional

# Validación de entrada mediante un try
try:
    x = int(input("Ingrese un número entero: "))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    exit() # Terminar Programa

# Verificar si un número es par o impar
if x % 2 == 0:                       # Si Condicion a cumplir
    print(f"El numero {x} es par")   # Valor si es verdadero
else:                                # En caso contrario
    print(f"El numero {x} es impar") # Calor si es falso

# Forma alternativa
print(f"{x} es par") if x % 2 == 0 else print(f"{x} es impar")

# Verificar múltiples condiciones con elif
if x % 3 == 0:                                              # Si condicion a cumplir
    print(f"El valor {x} es equivalente a 0 en modulo 3")   # Valor si es verdadero
elif x % 3 == 1:                                            # Pero si segunda condicion
    print(f"El valor {x} es equivalente a 1 en modulo 3")   # Valor si segunda condicion es verdadera
else:                                                       # En caso contrario
    print(f"El valor {x} es equivalente a 2 en modulo 3")   # Valor si no cumple ninguna condicion


# Forma alternativa, usar match-case para manejar múltiples condiciones (Python 3.10+)
match x % 3:
    case 0:
        print(f"El valor {x} es equivalente a 0 en modulo 3")
    case 1:
        print(f"El valor {x} es equivalente a 1 en modulo 3")
    case 2:
        print(f"El valor {x} es equivalente a 2 en modulo 3")

# If anidados
y = 5

if x > y:
    if x % 2 == 0:
        print("x es mayor que y ademas de que x es par")
    else:
        print("x es mayor que y ademas de que x es impar")
else:
    print("x es menor o igual que y")


# If con operadores logicos
z = 15
if x > y and x < z:
    print("x es mayor que y pero menor que z")
elif x > y and x > z:
    print("x es mayor que z e y")
elif x < y and x < z:
    print("x es menor que z e y")
else:
    print("ninguna condición se cumple")

if x > y or x > z:
    print("x es mayor que y o mayor que z")

if not x == y:
    print("x no es igual a y")


# Uso de any y all
condiciones = [x > y, x < z, x % 2 == 0]
if all(condiciones):
    print("x es mayor que y, menor que z y es par")
if any(condiciones):
    print("Al menos una condición se cumple")


# Uso de diccionarios para mapear condiciones
acciones = {
    0: "El valor es equivalente a 0 en modulo 3",
    1: "El valor es equivalente a 1 en modulo 3",
    2: "El valor es equivalente a 2 en modulo 3"
}
print(acciones.get(x % 3, "Valor no encontrado"))


# Condicion de Intentar
n1 = 10
n2 = 3

print(f"La división entre {n1} y {n2}")

try:
    resultado = n1 / n2
    if resultado == int(resultado):
        print("La division da un numero entero", resultado)
    else:
        print("La division da un numero decimal", resultado)

except ZeroDivisionError:
    print("No se pueden dividir números por cero")

except TypeError:
    print("Error de tipo: asegúrese de que los valores sean números")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

else:
    print("No se ejecutó ningún error")

finally:
    print("Terminó la ejecución de la secuencia Try")