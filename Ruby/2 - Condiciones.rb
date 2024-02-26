# Si condicional
x = 13

if x % 2 == 0
  puts "El numero #{x} es par"
else
  puts "El numero #{x} es impar"
end

# Forma alternativa
x % 2 == 0 ? (puts "#{x} es par") : (puts "#{x} es impar")

# Mas de 1 condicion
if x % 3 == 0
  puts "El valor #{x} es equivalente a 0 en modulo 3"
elsif x % 3 == 1
  puts "El valor #{x} es equivalente a 1 en modulo 3"
else
  puts "El valor #{x} es equivalente a 2 en modulo 3"
end

# If anidados
x = 10
y = 5

if x > y
  puts "x es mayor que y"
  if x.even?
    puts "x es par"
  else
    puts "x es impar"
  end
else
  puts "x es menor o igual que y"
end

# If con operadores logicos
x = 10
y = 5
z = 15

if x > y && x < z
  puts "x es mayor que y pero menor que z"
elsif x > y && x > z
  puts "x es mayor que z e y"
elsif x < y && x < z
  puts "x es menor que z e y"
else
  puts "ninguna condición se cumple"
end


# Condicion de Intentar
n1 = 10
n2 = 3

puts "La división entre #{n1} y #{n2}"

begin
  resultado = n1 / n2
  if resultado == resultado.to_i
    puts "La división da un número entero: #{resultado}"
  else
    puts "La división da un número decimal: #{resultado}"
  end
rescue ZeroDivisionError
  puts "No se pueden dividir números por cero"
else
  puts "No se produjo ningún error"
ensure
  puts "Terminó la ejecución de la secuencia begin"
end
