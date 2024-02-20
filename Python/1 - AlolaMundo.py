print("Alola mundo Python") # Imprimir un mensaje

# Los comentarios en python de una línea se hacen con el signo de gato #
"""
Los comentarios largos de varias líneas 
se hacen con 3 comillas dobles
"""

# Tipos de datos, con el signo = asignamos el valor a una variable
x = 23                                                      # Int
y = 2.434                                                   # Float
z = 3 + 5.5j                                                # Complex
A = "Cadena 3"                                              # String
b = True                                                    # Boolean
list = [1, 2, 3, 'a', 'b']                                  # Lista
tuple = (1, 2, 3, 'a', 'b')                                 # Tupla
set = {1, 2, 23, x, 3, 3, 4, y, A, 'A', 'A', 'A', 'a'}      # Conjunto (solo aparecera los elementos 1 sola vez)
dick = {'Nombre': 'Bob Esponja', 
        'Edad': 25,
        'Cursos': ['Calculo', 'Algebra', 'Ingles']}          # Diccionario
Nulo = None # Esto es un valor nulo

print("Esto es un entero", x, type(x))
print("Esto es un flotante", y, type(y))
print("Esto es un complejo", z, type(z))
print("Esto es un String: " + A, type(A))       # es este caso el signo + se usa para concatenas 2 string
print("Esto es un Booleano", b, type(b))
print("Esto es una lista", list, type(list))
print("Esto es una tupla", tuple, type(tuple))
print("Esto es un conjunto", set, type(set))
print("Esto es un diccionario", dick, type(dick))
print("Esto es un nulo", Nulo, type(Nulo))

# Una variable puede cambiar de tipo (tipado dinámico)
A = 2.27
print(A, type(A))

# Función para saber si una variable pertenece a cierto tipo
print("A es un floar", isinstance(A, float))
print("A es un String", isinstance(A, str))

# Python es Case Sensitive, diferencia mayúsculas de minúsculas
X = "73"  #Variable tipo string
print("esto es x:" , x, "Esto es X: " + X)

# Forma alternativa para imprimir y/o insertar un valor numérico dentro de un string
nombre = 'Bob Esponja'
Edad = 25
print(f"El alumno {nombre} tiene {Edad} años")
print("El alumno " + nombre + " tiene " + str(Edad) + " años")

# Representación de miles
Millonada = 6_325_412.32563215 # Se pueden escribir _ para separar los miles, el número se imprimirá normal
Millonada_formateado = "{:,}".format(Millonada)
print(f'Número con separador de miles: {Millonada_formateado}')

# Operaciones Básicas
# Suma
print(6 + 5, type(6 + 5))              # Int + Int = Int
print(x + 33, type(x + 33))
print(x + y, type(x + y))              # Int + Float = Float
print(2.8 + 1.4, type(2.8 + 1.4))      # Float + Float = Float

# Resta
print(6 - 5, type(6 - 5))              # Int - Int = Int
print(x - 33, type(x - 33))
print(x - y, type(x - y))              # Int - Float = Float
print(2.8 - 1.4, type(2.8 - 1.4))      # Float - Float = Float

# Multiplicación
print(6 * 5, type(6 * 5))              # Int * Int = Int
print(x * 33, type(x * 33))
print(x * y, type(x * y))              # Int * Float = Float
print(2.8 * 1.4, type(2.8 * 1.4))      # Float * Float = Float

# División
print(5 / 6, type(6 / 5))              # Int / Int = Float
print(x / 33, type(x / 35))
print(x / y, type(x / y))              # Int / Float = Float
print(2.8 / 1.4, type(2.8 / 1.4))      # Float / Float = Float

# División Entera
print(5 // 6, type(6 // 5))            # Int // Int = Int
print(x // 33, type(x // 33))
print(x // y, type(x // y))            # Int // Float = Float
print(2.8 // 1.4, type(2.8 // 1.4))    # Float // Float = Float

# Modulo
print(5 % 6, type(6 % 5))            # Int % Int = Int
print(x % 33, type(x % 33))
print(x % y, type(x % y))            # Int % Float = Float
print(2.8 % 1.4, type(2.8 % 1.4))    # Float % Float = Float

# Como vimos el signo + cambio su función según los parámetros que entreguen
print(1 + 2, "Suma de adición")
print("1" + "2", "Suma de concatenar")

# Operaciones Comparación
print("Operadores de Comparación")
Op1 = 23
Op2 = 57

print(f"Es {Op1} > {Op2}", Op1 > Op2, "Mayor estricto")
print(f"Es {Op1} < {Op2}",Op1 < Op2, "Menor estricto")
print(f"Es {Op1} >= 23", Op1 >= 23, "Mayor o igual")
print(f"Es 44 <= {Op2}", 44 <= Op2, "Mayor o igual")
print(f"Es {Op1} == {Op2}", Op1 == Op2, "igual a")
print(f"Es {Op2} == 57", Op2 == 57)
print(f"Es {Op1} != {Op2}", Op1 != Op2, "Distinto a")
print(f"Es {Op1} es entero", type(Op1) is int, "Es: ")
print(f"Es {Op1} no es entero", type(Op1) is not int, "No es: ")

# Algebra Booleana
print("Operaciones Lógicas")
t = True
f = False
t2 = True

print("Valor de t", t)
print("Valor de ~t", not t)             # Negación Lógica (~)
print("Valor de t ∧ f", t and f)        # Conjunción Lógica (y)
print("Valor de t ∧ t2", t and t2)
print("Valor de t ∨ f", t or f)         # Disyunción Lógica (o)

# Cambio de tipo de variable (Type Cast)
# Transformar una variable a Int
print("Transformar a Int")
print("La variable era:", X, "y su tipo:", type(X))
X = int(X)
print("La variable es:", X, "y su tipo:", type(X)) # Cuando se aplica a un numero que estaba como string se conserva
print("La variable era:", y, "y su tipo:", type(y))
print("La variable es:", int(y), "y su tipo:", type(y)) # Cuando se aplica a un float solo se toma la parte entera

# Transformar una variable a String
print("Transformar a String")
print("La variable es:", y, "y su tipo:", type(y))
y = str(y)
print("La variable es:", y, "y su tipo:", type(y))

# Transformar una variable a Float
print("Transformar a Float")
print("La variable es:", X, "y su tipo:", type(X))
X = float(X)
print("La variable es:", X, "y su tipo:", type(X))

# Ingresar un valor de forma manual
valor = input("Ingrese su valor aqui: ")
print(f"En valor es: {valor} Y es de tipo {type(valor)}")  # Siempre será un string

# Incrementar valores
x = x + 1 # El valor x se le asigna su sucesor
x += 1  # Forma acortada, todas las operaciones tienen su forma acortada

# Operaciones Acortadas
x = 30
x += 5  # x ahora es 35
x -= 3  # x ahora es 32
x *= 2  # x ahora es 64
x /= 4  # x ahora es 16.0
x //= 3 # x ahora es 5
x %= 3  # x ahora es 2
x **= 3 # x ahora es 8

# Funciones para string
mi_string = 'cazuEla'
print(len(mi_string), "Largo de mi string")
print(mi_string.find('z'), "Posición de la z en mi string, si se repiten se devuelve la menor posición") 
print(mi_string.capitalize(), "Primer carácter en mayúsculas")
print(mi_string.upper(), "Todo el string en mayúsculas")  
print(mi_string.lower(), "Todo el string en minúsculas")
print(mi_string.isdigit(), "Devuelve verdadero si es un número, falso en caso contrario")
print(mi_string.isalpha(), "Devuelve verdadero si el string solo contiene letras, falso en caso contrario")
print(mi_string.isalnum(), "Devuelve verdadero si el string solo contiene alpha numéricos, falso en caso contrario")
print(mi_string.count('a'), "Cuanta todas las a que contiene")
print(mi_string.replace('z', 'ss'), "Remplaza todas las z por ss")
print(mi_string * 3, "Se imprime el string 3 veces")


linea1 = "**********************"
linea2 = "*                    *"
linea3 = "*       Adios!       *"
print(linea1)
print(linea2)
print(linea3)
print(linea2)
print(22 * "*")