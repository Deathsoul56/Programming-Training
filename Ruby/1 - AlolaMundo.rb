puts "Alola Mundo Ruby" # Imprimir un mensaje

# Los comentarios en ruby de una línea se hacen con el signo de gato #

=begin
Los comentarios largos de varias líneas 
se indicando el inicio con =begin
y el final con =end
=end

x = 123                             # Int
y = 3.14                            # Float
z = Complex(5.25, 12)               # Complex 
texto = "Cadena"                    # String
arreglo = [1, 't', 3.1, "a", 5]     # Array
b = true                            # Booleanos
n = nil                             # Nil
range = 1..9                        # Rangos
persona = { nombre: "Juan", "edad" => 25, :ciudad => "Ejemplo" }       #Hash
# Vemos que en un Hash los valores se pueden asignar con : o con =>

puts "Tipos de datos"
print "Esto es un entero: " , x, " ", x.class, "\n"
print "Esto es un Float: " , y, " ", y.class, "\n"
print "Esto es un Complejo: " , z, " ", z.class, "\n"
print "Esto es un String: " , texto, " ", texto.class, "\n"
print "Esto es un Array: " , arreglo, " ", arreglo.class, "\n"
print "Esto es un Booleano: " , b, " ", b.class, "\n"
print "Esto es un Nil: " , n, " ", n.class, "\n"
print "Esto es un Rango: " , range, " ", range.class, "\n"
print "Esto es un Hash: " , persona, " ", persona.class, "\n"

# Una variable puede cambiar de tipo (tipado dinámico)
texto = 2.27
print "Nueva valor de texto: ", texto, " ", texto.class, "\n"

# Función para saber si una variable pertenece a cierto tipo
print "A es un float ", texto.is_a?(Float), "\n"
print "A es un String ", texto.is_a?(String), "\n"

# Ruby es Case Sensitive, diferencia mayúsculas de minúsculas
X = "73"  # Variable tipo string
print "esto es x: " , x, " Esto es X: " + X, "\n"

# Forma alternativa para imprimir y/o insertar un valor numérico dentro de un string
nombre = 'Bob Esponja'
Edad = 25
puts "El alumno #{nombre} tiene #{Edad} años"
print "El alumno " + nombre + " tiene " + String(Edad) + " años", "\n"
printf("El alumno %s tiene %s años\n", nombre, Edad)

# Representacion de miles
Millonada = 6_325_412.32563215 # Se pueden escribir _ para separar los miles, el número se imprimirá normal
puts "Numero con separador de miles: #{Millonada}"

# Operaciones Básicas
# Suma
puts "6 + 5 = #{6 + 5} #{(6 + 5).class}"                 # Int + Int = Int
puts "#{x} + 33 = #{x + 33} #{(x + 33).class}"
puts "#{x} + #{y} = #{x + y} #{(x + y).class}"           # Int + Float = Float
puts "2.8 + 1.4 = #{2.8 + 1.4} #{(2.8 + 1.4).class}"  # Float + Float = Float

# Resta
puts "6 - 5 = #{6 - 5} #{(6 - 5).class}"                 # Int - Int = Int
puts "#{x} - 33 = #{x - 33} #{(x - 33).class}"
puts "#{x} - #{y} = #{x - y} #{(x - y).class}"           # Int - Float = Float
puts "2.8 - 1.4 = #{2.8 - 1.4} #{(2.8 - 1.4).class}"  # Float - Float = Float

# Multiplicación
puts "6 * 5 = #{6 * 5} #{(6 * 5).class}"                 # Int * Int = Int
puts "#{x} * 33 = #{x * 33} #{(x * 33).class}"
puts "#{x} * #{y} = #{x * y} #{(x * y).class}"           # Int * Float = Float
puts "2.8 * 1.4 = #{2.8 * 1.4} #{(2.8 * 1.4).class}"  # Float * Float = Float

# División
puts "5 / 6 = #{5 / 6} #{(5 / 6).class}"             # Int / Int = Int
puts "#{x} / 33 = #{x / 33} #{(x / 33).class}"
puts "#{x} / #{y} = #{x / y} #{(x / y).class}"           # Int / Float = Float
puts "2.8 / 1.4 = #{2.8 / 1.4} #{(2.8 / 1.4).class}"  # Float / Float = Float

# Modulo
puts "5 % 6 = #{5 % 6} #{(5 % 6).class}"              # Int % Int = Int
puts "#{x} % 33 = #{x % 33} #{(x % 33).class}"
puts "#{x} % #{y} = #{x % y} #{(x % y).class}"        # Int % Float = Float
puts "#{2.8} % 1.4 = #{2.8 % 1.4} #{(2.8 % 1.4).class}"  # Float % Float = Float

# Hay que tener cuidado operando con float, vemos que a veces hay falta de precisión
# para asegurarnos que el resultado de una división será un float podemos forzar 5/2.0

# Como vimos el signo + cambio su función según los parámetros que entreguen
print 1 + 2, " Suma de adición", "\n"
print "1" + "2", " Concatenación de cadenas", "\n"

# Operaciones Comparación
puts "Operadores de Comparación"
Op1 = 23
Op2 = 57

puts "Es #{Op1} > #{Op2}: #{Op1 > Op2} (Mayor estricto)"
puts "Es #{Op1} < #{Op2}: #{Op1 < Op2} (Menor estricto)"
puts "Es #{Op1} >= 23: #{Op1 >= 23} (Mayor o igual)"
puts "Es 44 <= #{Op2}: #{44 <= Op2} (Mayor o igual)"
puts "Es #{Op1} = #{Op2}: #{Op1 == Op2} Igual a"
puts "Es #{Op2} = 57: #{Op2 == 57}"
puts "Es #{Op1} != #{Op2}: #{Op1 != Op2} Distinto a"
puts "Es #{Op1} es entero: #{Op1.is_a?(Integer)}"
puts "Es #{Op1} no es entero: #{!(Op1.is_a?(Integer))}"

# Álgebra Booleana
t = true
f = false
t2 = true

puts "Valor de t: #{t}"
puts "Valor de ~t: #{!t}"           # Negación Lógica (~)
puts "Valor de t ∧ f: #{t && f}"    # Conjunción Lógica (y)
puts "Valor de t ∧ t2: #{t && t2}"
puts "Valor de t ∨ f: #{t || f}"    # Disyunción Lógica (o)

# Cambio de tipo de variable (Type Cast)
# Transformar una variable a Int
puts "Transformar a Int"
puts "La variable era: #{X} y su tipo: #{X.class}"
X = X.to_i
puts "La variable es: #{X} y su tipo: #{X.class}" # Cuando se aplica a un numero que estaba como string se conserva
puts "La variable era: #{y} y su tipo: #{y.class}"
puts "La variable es: #{y.to_i} y su tipo: #{(y.to_i).class}" # Cuando se aplica a un float solo se toma la parte entera

# Transformar una variable a String
puts "Transformar a String"
puts "La variable es: #{y} y su tipo: #{y.class}"
y = y.to_s
puts "La variable es: #{y} y su tipo: #{y.class}"

# Transformar una variable a Float
puts "Transformar a Float"
puts "La variable es: #{x} y su tipo: #{x.class}"
x = x.to_f
puts "La variable es: #{x} y su tipo: #{x.class}"

# Ingresar un valor de forma manual
print "Ingrese su valor aqui: "
valor = gets.chomp
puts "El valor es: #{valor} y es de tipo: #{valor.class}"  # Siempre será un string

# Incrementar valores
x = x + 1 # El valor x se le asigna su sucesor
x += 1    # Forma acortada, todas las operaciones tienen su forma acortada

# Operaciones Acortadas
x = 30
x += 5  # x ahora es 35
x -= 3  # x ahora es 32
x *= 2  # x ahora es 64
x /= 4  # x ahora es 16.0
x = x.to_i  # Convertimos a entero para el operador de división entera
x /= 3  # x ahora es 5
x %= 3  # x ahora es 2
x **= 3 # x ahora es 8

# Funciones para string
mi_string = 'cazuEla'
puts "#{mi_string.length} Largo de mi string"
puts "#{mi_string.index('z')} Posición de la z en mi string, si se repiten se devuelve la menor posición"
puts "#{mi_string.capitalize} Primer carácter en mayúsculas"
puts "#{mi_string.upcase} Todo el string en mayúsculas"
puts "#{mi_string.downcase} Todo el string en minúsculas"
puts "#{mi_string.match?(/\A\d+\z/)} Devuelve verdadero si es un número, falso en caso contrario"
puts "#{mi_string.match?(/\A[a-zA-Z]+\z/)} Devuelve verdadero si el string solo contiene letras, falso en caso contrario"
puts "#{mi_string.match?(/\A\w+\z/)} Devuelve verdadero si el string solo contiene alpha numéricos, falso en caso contrario"
puts "#{mi_string.count('a')} Cuanta todas las a que contiene"
puts "#{mi_string.gsub('z', 'ss')} Remplaza todas las z por ss"
puts "#{mi_string * 3} Se imprime el string 3 veces"

linea1 = "**********************"
linea2 = "*                    *"
linea3 = "*       Adios!       *"
puts linea1
puts linea2
puts linea3
puts linea2
puts "*" * 22
