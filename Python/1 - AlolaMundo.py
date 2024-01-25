print("Alola mundo Python") #Imprimir un mensaje

#Los comentarios se una linea se hacen con el signo de gato #
"""
Los comentarios largos de varias lineas 
se hacen con 3 comillas dobles
"""

#Tipos de datos, con el signo = asignamos el valor a una variable
x = 23                                                      # Int
y = 2.434                                                   # Float
A = "Cadena 3"                                              # String
b = True                                                    # Boolean
list = [1, 2, 3, 'a', 'b']                                  # Lista
tuple = (1, 2, 3, 'a', 'b')                                 # Tupla
set = {1, 2, 23, x, 3, 3, 4, y, A, 'A', 'A', 'A', 'a'}      # Conjunto (solo aparecera los elementos 1 sola bez)
dick = {'Nombre': 'Bob Esponja', 
        'Edad': 25,
        'Cursos': ['Calculo', 'ALgebra', 'Inges']}          # Diccionario
Nulo = None #esto es un valor nulo

print("Esto es un entero", x, type(x))
print("Esto es un flotante", y, type(y))
print("Esto es un String: " + A, type(A))
print("Esto es un Boleano", b, type(b))
print("Esto es una lista", list, type(list))
print("Esto es una tupla", tuple, type(tuple))
print("Esto es un conjunto", set, type(set))
print("Esto es un diccionario", dick, type(dick))
print("Esto es un nulo", Nulo, type(Nulo))


#Una variable puede cambiar de tipo (tipado dinamico)
A = 2.27
print(A, type(A))

#Python es Case Sensitive, diferencia mayusculas de minusculas
X = "73"  #Variable tipo string
print("esto es x:" , x, "Esto es X: " + X)

#Operaciones Basicas
#Suma
print(6 + 5, type(6 + 5))              #Int + Int = Int
print(x + 33, type(x + 33))
print(x + y, type(x + y))              #Int + Float = Float
print(2.8 + 1.4, type(2.8 + 1.4))      #Float + Float = Float

#resta
print(6 - 5, type(6 - 5))              #Int - Int = Int
print(x - 33, type(x - 33))
print(x - y, type(x - y))              #Int - Float = Float
print(2.8 - 1.4, type(2.8 - 1.4))      #Float - Float = Float

#Multiplicacion
print(6 * 5, type(6 * 5))              #Int * Int = Int
print(x * 33, type(x * 33))
print(x * y, type(x * y))              #Int * Float = Float
print(2.8 * 1.4, type(2.8 * 1.4))      #Float * Float = Float

#Division
print(5 / 6, type(6 / 5))              #Int / Int = Float
print(x / 33, type(x / 35))
print(x / y, type(x / y))              #Int / Float = Float
print(2.8 / 1.4, type(2.8 / 1.4))      #Float / Float = Float

#Division Entera
print(5 // 6, type(6 // 5))            #Int // Int = Int
print(x // 33, type(x // 33))
print(x // y, type(x // y))            #Int // Float = Float
print(2.8 // 1.4, type(2.8 // 1.4))    #Float // Float = Float

#Modulo
print(5 % 6, type(6 % 5))            #Int % Int = Int
print(x % 33, type(x % 33))
print(x % y, type(x % y))            #Int % Float = Float
print(2.8 % 1.4, type(2.8 % 1.4))    #Float % Float = Float


#transformar una variable a Int
print("Transformar a Int")
print("La variable era:", X, "y su tipo:", type(X))
X = int(X)
print("La variable es:", X, "y su tipo:", type(X)) #Cuando se aplica a un numero que estaba como string se conversa
print("La variable era:", y, "y su tipo:", type(y))
print("La variable es:", int(y), "y su tipo:", type(y)) #Cuando se aplica a un float solo se toma la parte entera

#transformar una variable a String
print("Transformar a String")
print("La variable es:", y, "y su tipo:", type(y))
y = str(y)
print("La variable es:", y, "y su tipo:", type(y))

#transformar una variable a Float
print("Transformar a Float")
print("La variable es:", X, "y su tipo:", type(X))
X = float(X)
print("La variable es:", X, "y su tipo:", type(X))

#Ingresar un valor de forma manual
valor = input("Ingrese su valor aqui: ")
print("En valor es: ", valor, "Y es de tipo", type(valor))  #Siempre sera un string