# Ciclos while
x = -3
while x <= 10
  puts "Valor de x = #{x}"
  x += 1
end

# Ciclo do
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

# Avanzar por un rango
(0..5).each do |i| # Ciclo for imprime de 0 hasta n
  puts "Valor de i = #{i}"
end

# Avanzar por una lista
list = ['a', 'c', 7, 3.1415, true, 'lamda']
list.each_with_index do |i, index|
  puts "En valor #{index} de la lista es = #{i} de tipo = #{i.class}"
end

# Ciclos for
for i in -6..7
  puts "El valor de i es #{i}"
end

# Avanzar por una lista
arr = ['a', 'c', 7, 3.1415, true, 'lamda']
for color in arr
  puts "en valor i es: #{color}"
end


# Ciclos anidados

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

numeros.each do |numero|
  letras.each do |letra|
    puts "#{numero} #{letra}"
  end
end

matriz = [[4, 7, 9, 3], [2, 4, 6, 1]]
puts "La matriz original: #{matriz}"

matriz.each_with_index do |fila, index_fila|
  puts "Valor #{index_fila} es: #{fila}"
  fila.each_with_index do |valor, index_columna|
    puts "El valor #{index_columna} es: #{valor}"
  end
end