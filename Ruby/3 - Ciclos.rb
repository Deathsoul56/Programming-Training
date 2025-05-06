# Ciclos

puts "\n--- Ciclo While ---"
# Tipo While
x = -3
while x <= 10
  puts "Valor de x = #{x}"
  x += 1
end

y = 0
loop do
  y += 1
  if y == 5
    puts "Se rompio el ciclo"
    break # Romper el ciclo
  else
    puts "Ciclo infinito"
  end
end

puts "\n--- Ciclo For ---"
# Ciclos for

# Avanzar por un rango
(0..5).each do |i| # Ciclo for imprime de 0 hasta n
  puts "Valor de i = #{format('%02d', i)}"  # Formatea el número con dos dígitos
end

(-5...7).each do |j| # Imprime de -5 hasta 6 (equivalente a range(-5, 7) en Python)
  puts "Valor de j = #{j}"
end

# Avanzar por una lista
mi_lista = ['a', 'c', 7, 3.1415, true, 'lambda']
mi_lista.each do |elemento|
  puts "El elemento #{mi_lista.index(elemento)} de la lista es = #{elemento} de tipo = #{elemento.class}" # El método index es poco eficiente
end

mi_lista.each_with_index do |elemento, indice|
  puts "El elemento #{indice} de la lista es = #{elemento} de tipo = #{elemento.class}" # con each_with_index es mucho más óptimo
end

# Verificar múltiples valores en una lista
numeros = [10, 15, 20, 25, 30]
numeros.each do |num|
  if num % 2 == 0
    puts "#{num} es par"
  else
    puts "#{num} es impar"
  end
end

# ciclos con continue (next en Ruby), puede ser útil para saltar ciertas iteraciones en un ciclo
(0...10).each do |i|
  next if i % 2 == 0  # Saltar números pares
  puts "Número impar: #{i}"
end

# Ciclos con manejos de errores
(-1...5).each do |i|
  begin
    puts "10 / #{i}: #{10 / i}"
  rescue ZeroDivisionError
    puts "Error: No se puede dividir 10 entre #{i} (división por cero)."
    next  # Continuar con la siguiente iteración
  end
end

puts "\n--- Ciclos Anidados ---"
# Ciclos Anidados
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

numeros.each do |numero|
  letras.each do |letra|
    puts "#{numero} #{letra}"
  end
end

# Los ciclos anidados no son buenos para el rendimiento, una alternativa es usar zip
numeros.zip(letras).each do |numero, letra|
  puts "#{numero} #{letra}"
end

# Recorrer una matriz
matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
puts "La matriz original: #{matriz}"
matriz.each do |i|
  puts "Valor #{matriz.index(i)} es: #{i}"
  i.each do |j|
    puts "Es valor #{i.index(j)} es: #{j}"
  end
end

# De manera más óptima
matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
puts "La matriz original: #{matriz}"
matriz.each_with_index do |fila, fila_idx|
  puts "Fila #{fila_idx}: #{fila}"
  fila.each_with_index do |valor, columna_idx|
    puts "  Columna #{columna_idx}: #{valor}"
  end
end

# Times iterator (específico de Ruby)
puts "\n--- Times Iterator ---"
5.times do |i|
  puts "Iteración #{i}"
end

# Upto y Downto (específico de Ruby)
puts "\n--- Upto y Downto ---"
1.upto(5) do |i|
  puts "Contando hacia arriba: #{i}"
end

5.downto(1) do |i|
  puts "Contando hacia abajo: #{i}"
end

# Step (similar a range con paso en Python)
puts "\n--- Step ---"
(0..10).step(2) do |i|
  puts "Contando de 2 en 2: #{i}"
end

# Until (opuesto al while)
puts "\n--- Until ---"
contador = 0
until contador >= 5 do
  puts "Contador: #{contador}"
  contador += 1
end

# Each_slice (para procesar elementos en grupos)
puts "\n--- Each_slice ---"
(1..6).each_slice(2) do |grupo|
  puts "Grupo: #{grupo}"
end

# Select (similar a filter en Python)
puts "\n--- Select ---"
numeros = (1..10).to_a
pares = numeros.select { |num| num.even? }
puts "Números pares: #{pares}"

# Map (similar a map en Python)
puts "\n--- Map ---"
cuadrados = numeros.map { |num| num * num }
puts "Cuadrados: #{cuadrados}"

# Each_with_object (acumulador)
puts "\n--- Each_with_object ---"
resultado = (1..5).each_with_object({}) do |i, hash|
  hash[i] = i * i
end
puts "Hash de cuadrados: #{resultado}"

# Manejo de errores más detallado
puts "\n--- Manejo de Errores Detallado ---"
[-2, -1, 0, 1, 2].each do |divisor|
  begin
    resultado = 10 / divisor
    puts "10 / #{divisor} = #{resultado}"
  rescue ZeroDivisionError
    puts "No se puede dividir por cero"
  rescue StandardError => e
    puts "Error inesperado: #{e.message}"
  else
    puts "División exitosa"
  ensure
    puts "Proceso completado para #{divisor}"
  end
end

# Ciclos con case (switch)
puts "\n--- Case en Ciclos ---"
['A', 'B', 'C', 'D', 'F'].each do |nota|
  case nota
  when 'A'
    puts "Excelente"
  when 'B'
    puts "Bien"
  when 'C'
    puts "Regular"
  when 'D'
    puts "Suficiente"
  else
    puts "Reprobado"
  end
end