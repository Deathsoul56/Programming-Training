# Si condicional

x = 13

if x % 2 == 0:                       # Si Condicion a cumplir
    print(f"El numero {x} es par")   # Valor si es verdadero
else:                                # En caso contrario
    print(f"El numero {x} es impar") # Calor si es falso

# Forma alternativa
print(f"{x} es par") if x % 2 == 0 else print(f"{x} es impar")

# Mas de 1 condicion
if x % 3 == 0:                                              # Si condicion a cumplir
    print(f"El valor {x} es equivalente a 0 en modulo 3")   # Valor si es verdadero
elif x % 3 == 1:                                            # Pero si segunda condicion
    print(f"El valor {x} es equivalente a 1 en modulo 3")   # Valor si segunda condicion es verdadera
else:                                                       # En caso contrario
    print(f"El valor {x} es equivalente a 2 en modulo 3")   # Valor si no cumple ninguna condicion

# If anidados
x = 10
y = 5

if x > y:
    print("x es mayor que y")
    if x % 2 == 0:
        print("x es par")
    else:
        print("x es impar")
else:
    print("x es menor o igual que y")

# If con operadores logicos
x = 10
y = 5
z = 15

if x > y and x < z:
    print("x es mayor que y pero menor que z")
elif x > y and x > z:
    print("x es mayor que z e y")
elif x < y and x < z:
    print("x es menor que z e y")
else:
    print("ninguna condición se cumple")


# Condicion de Intentar
n1 = 10
n2 = 3

print(f"La división entre {n1} y {n2}")

try:
    resultado = n1 / n2
    if resultado == int(resultado):
        print("La division da un numero estero", resultado)
    else:
        print("La division da un numero decimal", resultado)

except ZeroDivisionError:
    print("No se pueden dividir números por cero")

else:
    print("No se ejecuto algun error")

finally:
    print("Termino la ejecicion de la secuencia Try")

