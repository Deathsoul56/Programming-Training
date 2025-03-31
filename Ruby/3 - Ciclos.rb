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