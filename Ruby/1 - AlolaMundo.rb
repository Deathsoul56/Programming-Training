puts "Alola Mundo Ruby" #Imprimir un mensaje

#Los comentarios se una linea se hacen con el signo de gato #

=begin
Los comentarios largos de varias lineas 
se indicando el inicio con =begin
y el final con =end
=end


x = 123                             # Fixnum
y = 9876543210                      # Bignum
pi = 3.14                           # Float
texto = "Cadena"                    # String
arreglo = [1, 't', 3, "a", 5]       # Array
b = true                            # Booleanos
n = nil                             # Nil
range = 1..9                        # Rangos

puts "Tipos de datos"
print "Fixnum: " , x , " ", x.class, "\n"
print "Bignum: " , y , " ", y.class, "\n"
print "Float: " , pi , " ", pi.class, "\n"
print "String: " , texto , " ", texto.class, "\n"
print "Array: " , arreglo , " ", arreglo.class, "\n"
print "Booleanos: " , b , " ", b.class, "\n"
print "Nil: " , n , " ", n.class, "\n"
print "Rangos: " , range , " ", range.class, "\n"

persona = { "nombre" => "Juan", "edad" => 25, "ciudad" => "Ejemplo" }       #Hash

puts "Hash: " , persona , "\n"

texto = 2.27
puts texto, texto.class

#Funcion para saber si una variable pertenece a cierto tipo
print "A es un float ", texto.is_a?(Float), "\n"
print "A es un String ", texto.is_a?(String), "\n"

#Ruby es Case Sensitive, diferencia mayusculas de minusculas
X = "73"  #Variable tipo string
print "esto es x: " , x, " Esto es X: " + X, "\n"

#Forma alternativa para insertar un valor numerico dentro de un string
nombre = 'Bob Esponja'
Edad = 25
puts "El alumno #{nombre} tiene #{Edad} años"
print "El alumno " + nombre + " tiene " + String(Edad) + " años", "\n"


#Operaciones Basicas
#Suma
print 6 + 5, " ", (6 + 5).class, "\n"              #Int + Int = Int
print x + 33, " ", (x + 33).class, "\n"
print x + y, " ", (x + y).class, "\n"              #Int + Float = Float
print 2.8 + 1.4, " ", (2.8 + 1.4).class, "\n"      #Float + Float = Float
