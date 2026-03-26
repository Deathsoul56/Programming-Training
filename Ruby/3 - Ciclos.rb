=begin
CLASE 3: CICLOS EN RUBY

Esta clase cubre los conceptos fundamentales de ciclos en Ruby:
1. Ciclo While y Until
2. Ciclo For y Each
3. Control de flujo (break, next)
4. Ciclos anidados
5. Iteradores específicos de Ruby
6. Manejo de errores en ciclos

Autor: Rafael
Fecha: Agosto 2024
=end

puts "=== CLASE 3: CICLOS EN RUBY ===\n"

puts "Los ciclos nos permiten repetir código de manera eficiente."
puts "Ruby ofrece múltiples formas de iterar: while, until, each, times, etc."
puts ""

# =============================================================================
# 1. CICLO WHILE Y UNTIL
# =============================================================================

puts "=" * 40
puts "1. CICLO WHILE Y UNTIL"
puts "=" * 40
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

# =============================================================================
# 2. CICLO FOR Y EACH
# =============================================================================

print "\n"
puts "=" * 40
puts "2. CICLO FOR Y EACH"
puts "=" * 40

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

# =============================================================================
# 3. CONTROL DE FLUJO (BREAK Y NEXT)
# =============================================================================

print "\n"
puts "=" * 40
puts "3. CONTROL DE FLUJO"
puts "=" * 40

# ciclos con continue (next en Ruby), puede ser útil para saltar ciertas iteraciones en un ciclo
(0...10).each do |i|
  next if i % 2 == 0  # Saltar números pares
  puts "Número impar: #{i}"
end

# =============================================================================
# 4. MANEJO DE ERRORES EN CICLOS
# =============================================================================

print "\n"
puts "=" * 40
puts "4. MANEJO DE ERRORES EN CICLOS"
puts "=" * 40

# Ciclos con manejos de errores
(-1...5).each do |i|
  begin
    puts "10 / #{i}: #{10 / i}"
  rescue ZeroDivisionError
    puts "Error: No se puede dividir 10 entre #{i} (división por cero)."
    next  # Continuar con la siguiente iteración
  end
end

# =============================================================================
# 5. CICLOS ANIDADOS Y OPTIMIZACIÓN
# =============================================================================

print "\n"
puts "=" * 40
puts "5. CICLOS ANIDADOS Y OPTIMIZACIÓN"
puts "=" * 40
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

# =============================================================================
# 6. ITERADORES ESPECÍFICOS DE RUBY
# =============================================================================

print "\n"
puts "=" * 40
puts "6. ITERADORES ESPECÍFICOS DE RUBY"
puts "=" * 40

# Times iterator (específico de Ruby)
puts "\nTimes Iterator:"
5.times do |i|
  puts "Iteración #{i}"
end

# Upto y Downto (específico de Ruby)
puts "\nUpto y Downto:"
1.upto(5) do |i|
  puts "Contando hacia arriba: #{i}"
end

5.downto(1) do |i|
  puts "Contando hacia abajo: #{i}"
end

# Step (similar a range con paso en Python)
puts "\nStep:"
(0..10).step(2) do |i|
  puts "Contando de 2 en 2: #{i}"
end

# Until (opuesto al while)
puts "\nUntil:"
contador = 0
until contador >= 5 do
  puts "Contador: #{contador}"
  contador += 1
end

# =============================================================================
# 7. MÉTODOS DE ITERACIÓN AVANZADOS
# =============================================================================

print "\n"
puts "=" * 40
puts "7. MÉTODOS DE ITERACIÓN AVANZADOS"
puts "=" * 40

# Each_slice (para procesar elementos en grupos)
puts "\nEach_slice:"
(1..6).each_slice(2) do |grupo|
  puts "Grupo: #{grupo}"
end

# Select (similar a filter en Python)
puts "\nSelect:"
numeros = (1..10).to_a
pares = numeros.select { |num| num.even? }
puts "Números pares: #{pares}"

# Map (similar a map en Python)
puts "\nMap:"
cuadrados = numeros.map { |num| num * num }
puts "Cuadrados: #{cuadrados}"

# Each_with_object (acumulador)
puts "\nEach_with_object:"
resultado = (1..5).each_with_object({}) do |i, hash|
  hash[i] = i * i
end
puts "Hash de cuadrados: #{resultado}"

# =============================================================================
# 8. MANEJO DE ERRORES AVANZADO
# =============================================================================

print "\n"
puts "=" * 40
puts "8. MANEJO DE ERRORES AVANZADO"
puts "=" * 40
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

# =============================================================================
# 9. CASE EN CICLOS
# =============================================================================

print "\n"
puts "=" * 40
puts "9. CASE EN CICLOS"
puts "=" * 40
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

# =============================================================================
# CONCLUSIONES
# =============================================================================

puts "=" * 40
puts "\n" + "=" * 50
puts "CONCLUSIONES SOBRE CICLOS EN RUBY"
puts "=" * 50

puts "\n1. CUÁNDO USAR CADA TIPO DE CICLO:"
puts "   • while/until: Cuando no sabemos exactamente cuántas iteraciones necesitamos"
puts "   • each: Para iterar sobre colecciones (arrays, hashes, rangos)"
puts "   • times: Cuando queremos repetir algo un número específico de veces"
puts "   • upto/downto: Para conteos ascendentes o descendentes"

puts "\n2. MEJORES PRÁCTICAS EN RUBY:"
puts "   • Usar each_with_index en lugar de index para mejor rendimiento"
puts "   • Preferir zip sobre ciclos anidados cuando sea posible"
puts "   • Usar next y break para controlar el flujo de manera eficiente"
puts "   • Aprovechar los métodos de enumeración (select, map, reject)"

puts "\n3. CARACTERÍSTICAS ÚNICAS DE RUBY:"
puts "   • Los iteradores son más idiomáticos que los ciclos tradicionales"
puts "   • each_with_object para construir estructuras de datos"
puts "   • step para rangos con incrementos personalizados"
puts "   • until como alternativa más legible a while con negación"

puts "\n4. CONTROL DE FLUJO:"
puts "   • break: Termina el ciclo completamente"
puts "   • next: Salta a la siguiente iteración (equivale a continue)"
puts "   • redo: Repite la iteración actual"
puts "   • else en begin/rescue: Se ejecuta si no hay errores"

puts "\n5. MÉTODOS DE ENUMERACIÓN IMPORTANTES:"
puts "   • select/filter: Filtra elementos que cumplen una condición"
puts "   • map/collect: Transforma cada elemento"
puts "   • each_slice: Procesa elementos en grupos"
puts "   • reduce/inject: Acumula valores"

puts "\n6. MANEJO DE ERRORES:"
puts "   • begin/rescue/ensure para manejo robusto de errores"
puts "   • rescue específico para diferentes tipos de errores"
puts "   • ensure siempre se ejecuta, incluso con errores"

puts "\n7. CASOS DE USO COMUNES:"
puts "   • Procesamiento de arrays y hashes"
puts "   • Transformación de datos con map y select"
puts "   • Validación y filtrado de entrada"
puts "   • Construcción de estructuras de datos complejas"

puts "\n=== FIN DE LA CLASE 3 ===\n"