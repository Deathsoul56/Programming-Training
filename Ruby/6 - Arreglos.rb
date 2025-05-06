require 'matrix'

# Introducción a los arreglos
puts "Los arreglos son estructuras de datos que permiten almacenar múltiples valores."

# Creación de arreglos
numerico = [3, 6, 8, 3, 13, 63, 17, 56, 234, 21, 73, 13, 8, 37, 64, 10, 15]
flotante = [3.1415, 2.7154, 8.2326]
cadenas = ['Rojo', 'Verde', 'Azul', 'Negro', 'Blanco', 'Cafe']
mixto = [2, 'Gauss', 3.1415, 'Noether', 17, 31, 73, 'Newton']

puts "\n--- Creación de arreglos ---"
p numerico
p flotante
p cadenas
p mixto

# Otras formas de crear arreglos
zeros = Array.new(5, 0)
ones = Array.new(5, 1)
full = Array.new(5, 7)
linspace = (0..10).to_a.sample(5).sort

puts "\n--- Otras formas de crear arreglos ---"
puts "Arreglo de ceros: #{zeros}"
puts "Arreglo de unos: #{ones}"
puts "Arreglo lleno de 7 con 5 elementos: #{full}"
puts "Arreglo con valores espaciados: #{linspace}"

# Ordenar arreglos
puts "\n--- Ordenar arreglos ---"
puts "Arreglo original: #{numerico}"
puts "Arreglo ordenado: #{numerico.sort}"
puts "Arreglo de cadenas original: #{cadenas}"
puts "Arreglo de cadenas ordenado: #{cadenas.sort}"

# Indexación y slicing
puts "\n--- Indexación y slicing ---"
puts "Elemento en la posición 2: #{numerico[2]}"

flotante.each_with_index do |valor, indice|
  puts "El valor #{indice} = #{valor}"
end

puts "Subarreglo de la posición 2 a la 6: #{numerico[2..6]}"
puts "Todo el arreglo: #{numerico}"

# Agregar y quitar datos
puts "\n--- Agregar y quitar datos ---"
flotante.push(65.2345)
puts "Arreglo después de agregar un elemento: #{flotante}"
flotante.delete_at(2)
puts "Arreglo después de eliminar un elemento: #{flotante}"

# Matrices
puts "\n--- Introducción a las matrices ---"
matriz_numerica = Matrix[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matriz_cadenas = [
  ['Rojo', 'Verde', 'Azul'],
  ['Negro', 'Blanco', 'Cafe'],
  ['Amarillo', 'Morado', 'Rosa']
]

puts "Matriz numérica: #{matriz_numerica}"
puts "Matriz de cadenas: #{matriz_cadenas}"

# Acceso a elementos de una matriz
puts "\nAcceso a elementos de una matriz:"
puts "Elemento en la fila 1, columna 2 de la matriz numérica: #{matriz_numerica[1, 2]}"
puts "Elemento en la fila 0, columna 1 de la matriz de cadenas: #{matriz_cadenas[0][1]}"

# Operaciones estadísticas básicas
puts "\n--- Funciones estadísticas ---"
puts "Media del arreglo numérico: #{numerico.sum.to_f / numerico.length}"
puts "Suma de los elementos del arreglo numérico: #{numerico.sum}"

# Búsqueda
puts "\n--- Buscar un elemento en el arreglo ---"
if numerico.include?(13)
  puts "El número 13 está en el arreglo."
else
  puts "El número 13 no está en el arreglo."
end

# Convertir a mayúsculas
puts "\n--- Convertir a mayúsculas ---"
cadenas_mayusculas = cadenas.map(&:upcase)
puts "Arreglo de cadenas en mayúsculas: #{cadenas_mayusculas}"