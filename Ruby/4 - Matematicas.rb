# Importar Librerias
require 'bigdecimal'
require 'bigdecimal/math'

# Numeros especiales
Pi = Math::PI           # Valor de pi 3.141592653589793
e = Math::E             # Valor de e 2.718281828459045
inf = Float::INFINITY   # Infinito Positivo
minf = -Float::INFINITY # Infinito Negativo
NoNumero = Float::NAN   # No es un numero (Not a number)
puts "Valor de Pi: #{Pi}, Valor de e: #{e}"
puts "Infinito positivo: #{inf}, infinito negativo: #{minf}"
puts "No es un numero: #{NoNumero}"

# Definir algunos valores
x = 24
y = 17.4
z = Complex(3, 4)

# Operaciones
puts "#{x} + #{y} = #{x + y}"          # Suma
puts "#{x} - #{y} = #{x - y}"          # Resta
puts "#{x} * #{y} = #{x * y}"          # Multiplicación
puts "#{x} / #{y} = #{x.to_f / y}"     # División
puts "#{x} / 9 = #{x / 9}"             # División entera
puts "#{x} % 9 = #{x % 9}"             # Módulo
puts "√#{x} = #{Math.sqrt(x)}"         # Raíz cuadrada
puts "#{x}^3 = #{x ** 3}"              # Potencia
puts "3√#{x} = #{x ** (1.0/3)}"        # Raíz N-ésima
puts "|-#{y}| = #{y.abs}"              # Valor absoluto
puts "Re(#{z}) = #{z.real}"            # Parte Real
puts "Im(#{z}) = #{z.imag}"            # Parte Imaginaria
puts "|#{z}| = #{z.abs}"               # Módulo Número complejo
puts "Arg(#{z}) = #{z.angle}"          # Argumento de un complejo
puts "#{z}* = #{z.conj}"               # Conjugado


# Funciones matemáticas
puts "e^2 = #{Math.exp(2)}"                  # Funciones exponencial
puts "Ln(#{x}) = #{Math.log(x)}"             # Logaritmo Natural
puts "Log_7(#{x}) = #{Math.log(7, x)}"       # Logaritmo cualquier base (base, argumento)
puts "floor(#{y}) = #{y.floor}"              # Funciones Piso
puts "Ceil(#{y}) = #{y.ceil}"                # Funciones Cielo
puts "√(5^2+12^2) = #{Math.hypot(5, 12)}"    # Hipotenusa

# Funciones trigonométricas (por defecto en radianes)
puts "sin(π/6) = #{Math.sin(Pi/6)}"         # Función Seno
puts "cos(π/6) = #{Math.cos(Pi/6)}"         # Función Coseno
puts "tg(π/6) = #{Math.tan(Pi/6)}"          # Función Tangente
puts "sec(π/6) = #{1 / Math.cos(Pi/6)}"     # Función Secante
puts "csc(π/6) = #{1 / Math.sin(Pi/6)}"     # Función Cosecante
puts "cotg(π/6) = #{1 / Math.tan(Pi/6)}"    # Función Cotangente

# Funciones trigonométricas inversas
puts "Arcosen(1/2) = #{Math.asin(1.0/2)}"    # Arcoseno
puts "Arcocosen(1/2) = #{Math.acos(1.0/2)}"  # Arcocoseno
puts "Arcotg(1/2) = #{Math.atan(1.0/2)}"     # Arcotangente

# Funciones Hiporbolicas
puts "sinh(3) = #{Math.sinh(3)}"        # Funcion Seno Hiporbolico
puts "cosh(3) = #{Math.cosh(3)}"        # Funcion Coseno Hiporbolico
puts "tanh(3) = #{Math.tanh(3)}"        # Funcion Tangente Hiporbolico
puts "sech(3) = #{1 / Math.cosh(3)}"    # Funcion Secante Hiporbolico
puts "csch(3) = #{1 / Math.sinh(3)}"    # Funcion Cosecante Hiporbolico
puts "cotanh(3) = #{1 / Math.tanh(3)}"  # Funcion Cotangente Hiporbolico

# Funciones Hiporbolicas Inversas
puts "Arcosinh(5) = #{Math.asinh(5)}"           # Funcion ArcoSeno Hiporbolico
puts "Arcocosh(5) = #{Math.acosh(5)}"           # Funcion ArcoCoseno Hiporbolico
puts "Arcotanh(1/2) = #{Math.atanh(1.0/2)}"     # Funcion ArcoTangente Hiporbolico

# Funciones inversas restante
"""
θ = arcsec(x)
sec(θ) = x
1 / cos(θ) = x
cos(θ) = 1 / x
θ = arccos(1/x)
"""
puts "Arcsec(5) = #{Math.acos(1.0 / 5)}"               # Funcion ArcoSecante
puts "Arccsc(5) = #{Math.asin(1.0 / 5)}"               # Funcion ArcoCosecante
puts "Arccotg(5) = #{Math.atan(1.0 / 5)}"              # Funcion ArcoCotangente
puts "Arcsech(1/2) = #{Math.acosh(1 / (1.0/2))}"       # Funcion ArcoSecante Hiporbolico
puts "Arccsch(5) = #{Math.asinh(1.0 / 5)}"             # Funcion ArcoCosecante Hiporbolico
puts "Arccotanh(5) = #{Math.atanh(1.0 / 5)}"           # Funcion ArcoCotangente Hiporbolico

lista = [12, 24, 8]
puts "Minimo comun multiplo #{lista} = #{lista.reduce(:lcm)}"    # Minimo comun multiplo
puts "Maximo comun divisor #{lista} = #{lista.reduce(:gcd)}"     # Maximo comun divisor

