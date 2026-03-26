# =============================================================================
# CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL EN RUBY
#
# Esta clase cubre los conceptos fundamentales de condiciones en Ruby:
# 1. Entrada de datos con validación y manejo de errores
# 2. Condicional simple y múltiple (if-else, elsif, condicionales inline)
# 3. Condicionales anidados
# 4. Operadores lógicos (&&, ||) y ANY/ALL
# 5. Hashes (Diccionarios) como alternativa a condiciones
# 6. Manejo avanzado de excepciones (begin, rescue, ensure)
#
# Autor: Rafael
# Fecha: Agosto 2024
# =============================================================================

puts "=== CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL EN RUBY ===\n\n"

puts "--- ¿Qué son las condiciones en Ruby? ---"
puts "Las condiciones permiten que el programa tome decisiones"
puts "basándose en si ciertas expresiones son verdaderas o falsas."
puts "En Ruby, TODO es 'verdadero' (truthy) excepto `false` y `nil`."

# =============================================================================
# 1. ENTRADA DE DATOS CON VALIDACIÓN
# =============================================================================

puts "\n1. ENTRADA DE DATOS CON VALIDACIÓN"
puts "=" * 40

puts "\nAntes de trabajar con condiciones, obtengamos un número del usuario:"

# Validación de entrada mediante un begin-rescue
print "Ingrese un número entero: "

begin
  x = Integer(gets.chomp)
  puts "✓ Número ingresado y casteado correctamente: #{x}"
rescue ArgumentError
  puts "✗ Por favor, ingrese un número entero válido."
  exit
end


# =============================================================================
# 2. CONDICIONAL SIMPLE Y MÚLTIPLE (IF, ELSIF Y CONDICIONALES EN LÍNEA)
# =============================================================================

puts "\n2. CONDICIONAL SIMPLE Y MÚLTIPLE"
puts "=" * 40

puts "\n--- Condicional simple clásico (if-else) ---"
# Verificar si un número es par o impar
puts "Evaluando si #{x} es par o impar:"
if x % 2 == 0                       # Si Condicion a cumplir
  puts "✓ El numero #{x} es par"      # Valor si es verdadero
else                                # En caso contrario
  puts "✓ El numero #{x} es impar"    # Valor si es falso
end

puts "\n--- Formas alternativas en línea (Ruby es famoso por esto) ---"
# Forma alternativa (Operador ternario)
x % 2 == 0 ? (puts "Ternario: #{x} es par") : (puts "Ternario: #{x} es impar")

# If y Unless "Modificador" (Va al final del comando)
puts "Modificador If: #{x} es par" if x % 2 == 0
puts "Modificador Unless: #{x} es impar" unless x % 2 == 0 # Execute Unless it is true

puts "\n--- Condicional múltiple (if-elsif-else) ---"
# Verificar múltiples condiciones con elsif
puts "Evaluando divisiones modulares por 3 sobre el #{x}:"
if x % 3 == 0                                              # Si condicion a cumplir
  puts "✓ El valor #{x} es equivalente a 0 en modulo 3"      # Valor si es verdadero
elsif x % 3 == 1                                           # Pero si segunda condicion
  puts "✓ El valor #{x} es equivalente a 1 en modulo 3"      # Valor si segunda condicion es verdadera
else                                                       # En caso contrario
  puts "✓ El valor #{x} es equivalente a 2 en modulo 3"      # Valor si no cumple ninguna condicion
end


# =============================================================================
# 3. CONDICIONALES ANIDADOS
# =============================================================================

puts "\n3. CONDICIONALES ANIDADOS"
puts "=" * 40

puts "\n--- If anidados ---"
y = 5
puts "Comparando x = #{x} con y = #{y}:"

if x > y
  puts "✓ x es mayor que y, procedemos a revisar su paridad:"
  if x % 2 == 0
    puts "  -> x es par"
  else
    puts "  -> x es impar"
  end
else
  puts "✓ x es menor o igual que y"
end


# =============================================================================
# 4. OPERADORES LÓGICOS (AND / OR) Y ARREGLOS CON .ANY? / .ALL?
# =============================================================================

puts "\n4. OPERADORES LÓGICOS Y MÉTODOS .ANY? / .ALL?"
puts "=" * 40

z = 15
puts "\nComparando x = #{x}, y = #{y}, z = #{z}:"

puts "\n--- Operadores lógicos Clásicos (&&, ||) ---"
if x > y && x < z
  puts "✓ x es mayor que y pero menor que z"
elsif x > y && x > z
  puts "✓ x es mayor que z e y"
elsif x < y && x < z
  puts "✓ x es menor que z e y"
else
  puts "✗ ninguna condición se cumple"
end

if x > y || x > z
  puts "✓ x es mayor que y, o mayor que z"
end

unless x == y
  puts "✓ x no es igual a y (usando bloque unles)"
end

puts "\n--- Métodos para arreglos lógicos (all? / any?) ---"
# Uso de all y any en arreglos de booleanos
condiciones = [x > y, x < z, x % 2 == 0]
puts "Evaluando bloque de condiciones [#{x}>#{y}, #{x}<#{z}, #{x} es par]:"
if condiciones.all?
  puts "✓ all? : x es mayor que y, menor que z, Y además es par"
else
  puts "✗ all? : No cumple todos los requisitos a la vez"
end

if condiciones.any?
  puts "✓ any? : Al menos una condición del array se cumple"
end


# =============================================================================
# 5. HASHES COMO ALTERNATIVAS A CONDICIONALES
# =============================================================================

puts "\n5. HASH COMO ALTERNATIVA DE BÚSQUEDA"
puts "=" * 40

puts "\n--- Uso de Hash para mapear en lugar de If/Elsif ---"
# Uso de hash para mapear condiciones
acciones = {
  0 => "El valor es equivalente a 0 en modulo 3",
  1 => "El valor es equivalente a 1 en modulo 3",
  2 => "El valor es equivalente a 2 en modulo 3"
}

# Fetch intenta acceder y, si no existe la llave, devuelve un valor por defecto
puts "Evaluando por Hash Directo para el remanente #{x%3}:"
puts "-> " + acciones.fetch(x % 3, "Valor de respuesta no encontrado")


# =============================================================================
# 6. MANEJO DE EXCEPCIONES EN RUBY (BEGIN, RESCUE)
# =============================================================================

puts "\n6. MANEJO DE EXCEPCIONES EN RUBY"
puts "=" * 40

puts "\n--- Condicion de Intentar (Begin-Rescue-Ensure) ---"
n1 = 10
n2 = 3

puts "La división entre #{n1} y #{n2}:"

begin
  resultado = n1 / n2
  if resultado == resultado.to_i
    puts "✓ La division da un numero entero #{resultado}"
  else
    puts "✓ La division da un numero decimal #{resultado}"
  end

rescue ZeroDivisionError
  puts "✗ No se pueden dividir números por cero"

rescue TypeError
  puts "✗ Error de tipo: asegúrese de que los valores sean números"

rescue => e
  puts "✗ Ocurrió un error inesperado al calcular matématicas: #{e}"

else
  puts "✓ 'else' de rescate: No se ejecutó ni encendió ningún error durante este bloque"

ensure
  puts "→ 'ensure': Terminó la ejecución de la secuencia begin/rescue exitosamente."
end

# =============================================================================
# CONCLUSIONES
# =============================================================================

puts "\n=================================================="
puts "CONCLUSIONES SOBRE CONDICIONALES EN RUBY"
puts "=================================================="

puts "\n1. LA MAGIA DE 'UNLESS':"
puts "   • Ruby introdujo orgánicamente la palabra `unless` como la antítesis del If. Ayuda inmensamente a leer el código como si fuera un libro: `puts 'Hola' unless x == 2`."

puts "\n2. MODIFICADORES DE EXPRESIÓN EN UNA LÍNEA:"
puts "   • Todo IF en Ruby puede ponerse 'hacia atrás'. Es elegantísimo poder hacer tareas atómicas colocando la acción al frente y la condición atrás."

puts "\n3. MÉTODOS CON SIGNOS DE INTERROGACIÓN (?):"
puts "   • Métodos como `.any?` y `.all?` siempre terminarán en el signo '?' en Ruby. Esto es una convención de estilo universal del lenguaje que avisa visualmente al que lee que esto le devolverá True o False."

puts "\n4. BEGIN, RESCUE Y EL PODEROSO ENSURE:"
puts "   • Es equivalente a Try - Catch - Finally. Rescatamos los fallos con `rescue`, y con `ensure` garantizamos que el programa cierre su proceso."

puts "\n=== FIN DE LA CLASE 2 ===\n"
