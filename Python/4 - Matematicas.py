# Importar Librerias
import numpy as np
import matplotlib.pyplot as plt

# Numeros especiales
Pi = np.pi          # Valor de pi 3.141592653589793
e = np.e            # Valor de e 2.718281828459045
inf = np.inf        # Infinito Positivo
minf = np.NINF      # Infinito Negativo
NoNumero = np.NaN   # No es un numero (Not a number)
print(f"Valor de Pi: {Pi}, Valor de e: {e}")
print(f"Infinito positivo: {inf}, infinito negativo: {minf}")
print(f"No es un numero: {NoNumero}")

# Definir algunos valores
x = 24
y = 17.4
z = 3 + 4j

# Operaciones
print(f"{x} + {y} = {x + y}")          # Suma
print(f"{x} - {y} = {x - y}")          # Resta
print(f"{x} * {y} = {x * y}")          # Multiplicacion
print(f"{x} / {y} = {x / y}")          # Division
print(f"{x} // 9 = {x // 9}")          # Division entera
print(f"{x} % 9 = {x % 9}")            # Modulo
print(f"√{x} = {np.sqrt(x)}")          # Raiz Cuadrada
print(f"{x}^3 = {x ** 3}")             # Potencia
print(f"{x}^3 = {np.power(x, 3)}")     # Potencia con numpy
print(f"3√{x} = {np.power(x, 1/3)}")   # Raiz N-esima con numpy
print(f"|-{y}| = {np.abs(-y)}")        # Valor absoluto
print(f'Re({z}) = {np.real(z)}')       # Parte Real
print(f'Im({z}) = {np.imag(z)}')       # Parte Imaginaria
print(f"|{z}| = {np.abs(z)}")          # Modulo Numero complejo
print(f'Arg({z}) = {np.angle(z)}')     # Argumento de un complejo
print(f'{z}* = {np.conj(z)}')          # Conjugado

# Funciones matematicas
print(f"e^2 = {np.exp(2)}")                  # Funcinoes exponencial
print(f"Ln({x}) = {np.log(x)}")              # Logaritmo Natural
print(f"Log_7({x}) = {np.emath.logn(7, x)}") # Logaritmo cualquier base (base, argumento)
print(f"floor({y}) = {np.floor(y)}")         # Funciones Piso
print(f"Ceil({y}) = {np.ceil(y)}")           # Funciones Cielo
print(f'√(5^2+12^2) = {np.hypot(5, 12)}')    # Hipotenusa

#Funciones Trigonometricas (Por defecto estan en Radianes)
print(f"sin(π/6) = {np.sin(Pi/6)}")         # Funcion Seno
print(f"cos(π/6) = {np.cos(Pi/6)}")         # Funcion Coseno
print(f"tg(π/6) = {np.tan(Pi/6)}")          # Funcion Tangente
print(f"sec(π/6) = {1 / np.cos(Pi/6)}")     # Funcion Secante
print(f"csc(π/6) = {1 / np.sin(Pi/6)}")     # Funcion Cosecante
print(f"cotg(π/6) = {1 / np.tan(Pi/6)}")    # Funcion Cotangente

#Funciones Trigonometricas Inversas
print(f'Arcosen(1/2) = {np.arcsin(1/2)}')   # Arcoseno
print(f'Arcocosen(1/2) = {np.arccos(1/2)}') # Arcocoseno
print(f'Arcotg(1/2) = {np.arctan(1/2)}')    # Arcotangente

# Cambios de Angulos
print(f'180° en radianes es: {np.deg2rad(180)}')    # De deg a radianes
print(f'π/4 en grados es: {np.rad2deg(Pi/4)}')      # De radianes a deg

# Funciones Hiporbolicas
print(f"sinh(3) = {np.sinh(3)}")        # Funcion Seno Hiporbolico
print(f"cosh(3) = {np.cosh(3)}")        # Funcion Coseno Hiporbolico
print(f"tanh(3) = {np.tanh(3)}")        # Funcion Tangente Hiporbolico
print(f"sech(3) = {1 / np.cosh(3)}")    # Funcion Secante Hiporbolico
print(f"csch(3) = {1 / np.sinh(3)}")    # Funcion Cosecante Hiporbolico
print(f"cotanh(3) = {1 / np.tanh(3)}")  # Funcion Cotangente Hiporbolico

# Funciones Hiporbolicas Inversas
print(f"Arcosinh(5) = {np.arcsinh(5)}")     # Funcion ArcoSeno Hiporbolico
print(f"Arcocosh(5) = {np.arccosh(5)}")     # Funcion ArcoCoseno Hiporbolico
print(f"Arcotanh(1/2) = {np.arctanh(1/2)}") # Funcion ArcoTangente Hiporbolico

# Funciones inversas restante
"""
θ = arcsec(x)
sec(θ) = x
1 / cos(θ) = x
cos(θ) = 1 / x
θ = arccos(1/x)
"""
print(f"Arcsec(5) = {np.arccos(1 / 5)}")            # Funcion ArcoSecante
print(f"Arccsc(5) = {np.arcsin(1 / 5)}")            # Funcion ArcoCosecante
print(f"Arccotg(5) = {np.arctan(1 / 5)}")           # Funcion ArcoCotangente
print(f"Arcsech(1/2) = {np.arccosh(1 / (1/2))}")    # Funcion ArcoSecante Hiporbolico
print(f"Arccsch(5) = {np.arcsinh(1 / 5)}")          # Funcion ArcoCosecante Hiporbolico
print(f"Arccotanh(5) = {np.arctanh(1 / 5)}")        # Funcion ArcoCotangente Hiporbolico

lista = np.array([12, 24, 8])
print(f'Minimo comun multiplo {lista} = {np.lcm.reduce(lista)}')    # Minimo comun multiplo
print(f'Maximo comun divisor {lista} = {np.gcd.reduce(lista)}')     # Maximo comun divisor

# Graficos
# Grafico de una funcion f(x)
x = np.linspace(- 5, 5, 50) # Crear un vector que empieza en -5, termina en 5 y tiene 50 elementos equidistantes
y = np.exp(x)

plt.plot(x, y, label='exp(x)') # Crear el gráfico de una funcion

# Agregar etiquetas y título al gráfico
plt.xlabel('x')
plt.ylabel('Funcion: exp(x)')
plt.title('Función Exponencial')

plt.xlim(-6, 6) # Limites de visualizacion en X
plt.ylim(-1, 20 ) # Limites de visualizacion en Y

plt.legend() # Mostrar la leyenda
plt.grid() # El grafico tiene cuadriculas   

plt.show() # Mostrar el gráfico

# Grafico de puntos
x = np.random.randint(-100, 101, size = 50) # Vector de numeros aleatorios entre -100 y 100
y = np.random.randint(-100, 101, size = 50)
plt.scatter(x, y, label = 'Datos dispersos')
plt.xlabel('Valor x')
plt.ylabel('Valor Y')
plt.title('Scatterplot')

plt.xlim(-105, 105) 
plt.ylim(-105, 105 )
plt.legend()
plt.grid() 

plt.show() 

# Grafico de Barras
categorias = np.array(['Rojo', 'Azul', 'Verde', 'Amarillo', 'Blanco'])
valores = np.array([23, 45, 56, 78, 33])
colores = np.array(['red', 'green', 'blue', 'orange', 'purple']) # Los colores de las barras se pueden agregan con caracteres 
colores_hex = np.array(['#FF5733', '#00FF00', '#0000FF', '#FFA500', '#800080']) # O en hexadecimal

plt.bar(categorias, valores, label = 'Preferencias', color = colores_hex) # Crear el gráfico de barras

plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de barras')
plt.legend()
plt.show()

# Histograma
datos = np.random.randn(1000)  # 1000 puntos de datos distribuidos normalmente

# Crear el histograma
plt.hist(datos, bins = 30, color='skyblue', edgecolor='black')  # 'bins' controla el número de barras

plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de datos aleatorios')

plt.show()