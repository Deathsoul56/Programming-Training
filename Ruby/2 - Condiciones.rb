# Si condicional

# Validación de entrada mediante un begin-rescue
begin
  print "Ingrese un número entero: "
  x = Integer(gets.chomp)
rescue ArgumentError
  puts "Por favor, ingrese un número entero válido."
  exit
end

# Verificar si un número es par o impar
if x % 2 == 0                       # Si Condicion a cumplir
  puts "El numero #{x} es par"      # Valor si es verdadero
else                                # En caso contrario
  puts "El numero #{x} es impar"    # Valor si es falso
end

# Forma alternativa
x % 2 == 0 ? (puts "#{x} es par") : (puts "#{x} es impar")
puts "#{x} es par" if x % 2 == 0
puts "#{x} es impar" unless x % 2 == 0

# Verificar múltiples condiciones con elsif
if x % 3 == 0                                              # Si condicion a cumplir
  puts "El valor #{x} es equivalente a 0 en modulo 3"      # Valor si es verdadero
elsif x % 3 == 1                                           # Pero si segunda condicion
  puts "El valor #{x} es equivalente a 1 en modulo 3"      # Valor si segunda condicion es verdadera
else                                                       # En caso contrario
  puts "El valor #{x} es equivalente a 2 en modulo 3"      # Valor si no cumple ninguna condicion
end

# If anidados
y = 5

if x > y
  puts "x es mayor que y"
  if x % 2 == 0
    puts "x es par"
  else
    puts "x es impar"
  end
else
  puts "x es menor o igual que y"
end

# If con operadores logicos
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

if x > y || x > z
  puts "x es mayor que y o mayor que z"
end

unless x == y
  puts "x no es igual a y"
end

# Uso de all y any
condiciones = [x > y, x < z, x % 2 == 0]
if condiciones.all?
  puts "x es mayor que y, menor que z y es par"
end
if condiciones.any?
  puts "Al menos una condición se cumple"
end

# Uso de hash para mapear condiciones
acciones = {
  0 => "El valor es equivalente a 0 en modulo 3",
  1 => "El valor es equivalente a 1 en modulo 3",
  2 => "El valor es equivalente a 2 en modulo 3"
}
puts acciones.fetch(x % 3, "Valor no encontrado")


# Condicion de Intentar
n1 = 10
n2 = 3

puts "La división entre #{n1} y #{n2}"

begin
  resultado = n1 / n2
  if resultado == resultado.to_i
    puts "La division da un numero entero #{resultado}"
  else
    puts "La division da un numero decimal #{resultado}"
  end
rescue ZeroDivisionError
  puts "No se pueden dividir números por cero"

rescue TypeError
  puts "Error de tipo: asegúrese de que los valores sean números"

rescue => e
  puts "Ocurrió un error inesperado: #{e}"

else
  puts "No se ejecutó ningún error"

ensure
  puts "Terminó la ejecución de la secuencia begin"
end
