# =============================================================================
# CLASE 1: ALOLA MUNDO RUBY
#
# Esta clase cubre los conceptos fundamentales en Ruby:
# 1. Características del lenguaje y comentarios
# 2. Variables, tipos de datos y comprobación
# 3. Formateo y Hash (Diccionarios)
# 4. Operaciones aritméticas, lógicas y de comparación
# 5. Conversión de tipos y entrada de usuario
# 6. Métodos útiles de Strings y Operadores
# =============================================================================

puts "=== CLASE 1: ALOLA MUNDO RUBY ===\n\n"

# =============================================================================
# 1. CARACTERÍSTICAS DEL LENGUAJE Y COMENTARIOS
# =============================================================================

puts "1. CARACTERÍSTICAS DEL LENGUAJE Y COMENTARIOS"
puts "=" * 40

puts "\n--- Comentarios en Ruby ---"
# Los comentarios en ruby de una línea se hacen con el signo de gato #
puts "Los comentarios de una línea usan #"

=begin
Los comentarios largos de varias líneas 
se indicando el inicio con =begin
y el final con =end
=end
puts "Los comentarios multilínea usan =begin y =end"

puts "\n--- Case Sensitivity ---"
# Ruby es Case Sensitive, diferencia mayúsculas de minúsculas
x = 23
X = "73"  # Variable tipo string
puts "Variable x minúscula: #{x}"
puts "Variable X mayúscula: #{X}"
puts "¡Son variables completamente diferentes!"

# =============================================================================
# 2. VARIABLES, TIPOS DE DATOS Y ESTRUCTURAS BÁSICAS
# =============================================================================

puts "\n2. VARIABLES Y TIPOS DE DATOS BÁSICOS"
puts "=" * 40

puts "\n--- Tipos de Datos ---"
x = 123                             # Int (Integer)
y = 3.14                            # Float
z = Complex(5.25, 12)               # Complex 
texto = "Cadena"                    # String
arreglo = [1, 't', 3.1, "a", 5]     # Array
b = true                            # Boolean
n = nil                             # Nil
range = 1..9                        # Range
persona = { nombre: "Juan", "edad" => 25, :ciudad => "Ejemplo" } # Hash

# Imprimir los tipos
printf("%-15s %-30s %s\n", "Categoría", "Valor", "Clase (Type)")
printf("%-15s %-30s %s\n", "Entero:", x, x.class)
printf("%-15s %-30s %s\n", "Float:", y, y.class)
printf("%-15s %-30s %s\n", "Complejo:", z, z.class)
printf("%-15s %-30s %s\n", "String:", texto, texto.class)
printf("%-15s %-30s %s\n", "Array:", arreglo.to_s, arreglo.class)
printf("%-15s %-30s %s\n", "Boolean:", b, b.class)
printf("%-15s %-30s %s\n", "Nil:", n.inspect, n.class)
printf("%-15s %-30s %s\n", "Rango:", range, range.class)
printf("%-15s %-30s %s\n", "Hash:", persona.to_s, persona.class)

puts "\n--- Tipado Dinámico ---"
# Una variable puede cambiar de tipo (tipado dinámico)
texto_original = texto
texto = 2.27
puts "La variable 'texto' ha cambiado de: '#{texto_original}' a #{texto} (#{texto.class})"

puts "\n--- Verificación de Tipos ---"
# Función para saber si una variable pertenece a cierto tipo
puts "¿Es 'texto' un Float? -> #{texto.is_a?(Float)}"
puts "¿Es 'texto' un String? -> #{texto.is_a?(String)}"
puts "¿Es 'x' una instancia Integer pura? -> #{x.instance_of?(Integer)}"

# =============================================================================
# 3. FORMATEO Y ESTRUCTURAS HASH
# =============================================================================

puts "\n3. FORMATEO Y ESTRUCTURAS HASH"
puts "=" * 40

puts "\n--- Formateo de Strings ---"
nombre = 'Bob Esponja'
Edad = 25
puts "1. Usando Interpolación (Recomendado): El alumno #{nombre} tiene #{Edad} años"
puts "2. Usando Concatenación (+): El alumno " + nombre + " tiene " + String(Edad) + " años"
printf("3. Usando Printf (Estilo C): El alumno %s tiene %s años\n", nombre, Edad)

puts "\n--- Formateo de Números Grandes ---"
Millonada = 6_325_412.32563215 
# Se pueden escribir _ para separar los miles, el compilador los ignora
puts "Numero definido con separadores de miles (_): #{Millonada}"

puts "\n--- Operaciones con Hash (Diccionarios) ---"
# En un Hash los valores se pueden asignar con : o con =>
edad_hash = persona[:edad]  # Extraer el valor
puts "La edad de #{persona[:nombre]} es #{edad_hash} años."
altura = persona.fetch(:altura, 'No especificada')  # Con valor default preventivo
puts "La altura de #{persona[:nombre]} es: #{altura}."

# =============================================================================
# 4. OPERACIONES ARITMÉTICAS, LÓGICAS Y DE COMPARACIÓN
# =============================================================================

puts "\n4. OPERACIONES ARITMÉTICAS, LÓGICAS Y DE COMPARACIÓN"
puts "=" * 40

puts "\n--- Operaciones Aritméticas Básicas ---"
puts "Suma:               #{x} + #{y} = #{x + y}"
puts "Resta:              #{x} - #{y} = #{x - y}"
puts "Multiplicación:     #{x} * #{y} = #{x * y}"
puts "División:           5 / 6 = #{5 / 6} (Int / Int devuelve Int truncado)"
puts "División Precisa:   5 / 6.0 = #{5 / 6.0} (Si hay float, hay precisión)"
puts "División Entera:    5.div(6) = #{5.div(6)}"
puts "Módulo:             5 % 6 = #{5 % 6}"

puts "\n--- Operadores de Comparación ---"
Op1 = 23
Op2 = 57
puts "¿#{Op1} > #{Op2}?  #{Op1 > Op2} (Mayor estricto)"
puts "¿#{Op1} < #{Op2}?  #{Op1 < Op2} (Menor estricto)"
puts "¿#{Op1} >= 23? #{Op1 >= 23} (Mayor o igual)"
puts "¿44 <= #{Op2}? #{44 <= Op2} (Mayor o igual)"
puts "¿#{Op1} == #{Op2}? #{Op1 == Op2} (Igual a)"
puts "¿#{Op1} != #{Op2}? #{Op1 != Op2} (Distinto a)"

puts "\n--- Operaciones Lógicas (Álgebra Booleana) ---"
t = true
f = false
t2 = true

puts "Valor de t: #{t}"
puts "Valor de !t: #{!t} (Negación Lógica NOT)"
puts "Valor de t && f: #{t && f} (Conjunción Lógica AND)"
puts "Valor de t || f: #{t || f} (Disyunción Lógica OR)"

# =============================================================================
# 5. CONVERSIÓN DE TIPOS Y ENTRADA DE USUARIO
# =============================================================================

puts "\n5. CONVERSIÓN DE TIPOS Y ENTRADA DE USUARIO"
puts "=" * 40

puts "\n--- Conversión de Tipos (Type Casting) ---"
puts "\nTransformar a Entero (.to_i):"
puts "X string inicial: '#{X}' -> convertido a: #{X.to_i}" 
puts "y float inicial: #{y} -> convertido a: #{y.to_i} (Se trunca el decimal)"

puts "\nTransformar a String (.to_s):"
puts "y numérico: #{y} -> convertido a string: '#{y.to_s}'"

puts "\nTransformar a Float (.to_f):"
puts "x entero: #{x} -> convertido a float: #{x.to_f}"

puts "\n--- Entrada de datos del usuario ---"
# Ingresar un valor de forma manual
print "Ingrese su valor aqui: "
valor = gets.chomp
puts "El valor ingresado es: '#{valor}'"
puts "Este valor siempre entra como clase: #{valor.class}"

# =============================================================================
# 6. MÉTODOS ÚTILES Y OPERADORES DE ASIGNACIÓN
# =============================================================================

puts "\n6. MÉTODOS ÚTILES DE STRINGS Y ASIGNADORES"
puts "=" * 40

puts "\n--- Operadores de Asignación Compuesta ---"
# Incrementar valores de manera abreviada
var_op = 30
puts "Valor inicial: #{var_op}"
var_op += 5  ; puts "+= 5  -> #{var_op}"
var_op -= 3  ; puts "-= 3  -> #{var_op}"
var_op *= 2  ; puts "*= 2  -> #{var_op}"
var_op /= 4  ; puts "/= 4  -> #{var_op}"
var_op %= 3  ; puts "%= 3  -> #{var_op}"
var_op **= 3 ; puts "**= 3 -> #{var_op}"

puts "\n--- Métodos potentes para Strings ---"
mi_string = 'cazuEla'
puts "String original: '#{mi_string}'"

puts "Largo (.length): #{mi_string.length}"
puts "Posición de 'z' (.index): #{mi_string.index('z')}"
puts "Capitalizar (.capitalize): '#{mi_string.capitalize}'"
puts "Mayúsculas (.upcase): '#{mi_string.upcase}'"
puts "Minúsculas (.downcase): '#{mi_string.downcase}'"
puts "Reemplazar (.gsub): '#{mi_string.gsub('z', 'ss')}'"
puts "Multiplicador de strings (* 3): '#{mi_string * 3}'"

puts "\nComprobaciones Regex Directas (.match?):"
puts "¿Solo números?: #{mi_string.match?(/\A\d+\z/)}"
puts "¿Solo letras?: #{mi_string.match?(/\A[a-zA-Z]+\z/)}"
puts "¿Contar letras 'a' (.count): #{mi_string.count('a')}"

puts "\n--- Despedida ---"
linea1 = "**********************"
linea2 = "*                    *"
linea3 = "*       Adios!       *"
puts linea1
puts linea2
puts linea3
puts linea2
puts "*" * 22

# =============================================================================
# CONCLUSIONES
# =============================================================================

puts "\n=================================================="
puts "CONCLUSIONES SOBRE ALOLA MUNDO Y RUBY BÁSICO"
puts "=================================================="

puts "\n1. TODO ES UN OBJETO:"
puts "   • En Ruby el paradigma de objetos es radical. Todos los datos, hasta los números primitivos, son objetos con métodos propios y clases (por ejemplo 5.div(2))."

puts "\n2. STRINGS E INTERPOLACIÓN:"
puts "   • Ruby brilla en el formateo de strings usando el formato nativo \#{variable} que evalúa código arbitrario incrustado dentro del texto."

puts "\n3. LOS BLOQUES HASH (DICCIONARIOS):"
puts "   • Los diccionarios en Ruby, llamados Hashes, son poderosos y usan símbolos especiales (:nombre) para acceder a memoria más eficientemente que usando strings normales (\"nombre\")."

puts "\n4. SIMPLICIDAD MATEMÁTICA Y CASTEO:"
puts "   • Modificar un tipo de base a otro es tan simple como pedirle al objeto convertirse usando los métodos estándar como `.to_i`, `.to_f` y `.to_s`."

puts "\n=== FIN DE LA CLASE 1 ===\n"
