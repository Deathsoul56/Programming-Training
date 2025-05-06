# Definir funciones con def

# 1. Función básica sin parámetros
def saludar
  puts "¡Hola, bienvenido al curso de Ruby!"
end

# 2. Función con parámetros
def funcion(x)
  x + 5  # En Ruby, la última expresión es implícitamente retornada
end

# 3. Función con varios parámetros
def funcion2(x, y)
  z = x - y   # Las variables que se crean en una función solo existen en la función
  z  # retorno implícito
end

# 4. Función con múltiples valores de retorno
def calcular_estadisticas(numeros)
  return [0, 0.0, nil, nil] if numeros.empty?  # Manejo de array vacío

  suma = numeros.sum
  promedio = suma.to_f / numeros.length
  maximo = numeros.max
  minimo = numeros.min
  [suma, promedio, maximo, minimo]  # Ruby retorna un array
end

# 5. Función que devuelve el caracter más repetido de un String
def caracter_mas_repetido(cadena)
  return nil if cadena.nil? || cadena.empty?

  # Crear un hash para contar la frecuencia de cada carácter
  frecuencias = Hash.new(0)
  cadena.each_char do |char|
    frecuencias[char] += 1 unless char == ' '  # Ignoramos espacios
  end

  # Encontrar el carácter con la mayor frecuencia
  frecuencias.max_by { |_, count| count }&.first
end

# 6. Función con parámetros por defecto
def saludar_persona(nombre = "Invitado")
  "Hola #{nombre}!"
end

# 7. Función con argumentos variables (*args)
def sumar_numeros(*numeros)
  numeros.sum
end

# 8. Función con argumentos de palabra clave variables (**kwargs)
def info_persona(**datos)
  datos.each do |clave, valor|
    puts "#{clave}: #{valor}"
  end
end

# 9. Módulo para medir tiempo de ejecución
module MedirTiempo
  def medir_tiempo(metodo)
    alias_method "original_#{metodo}", metodo

    define_method(metodo) do |*args, &block|
      inicio = Time.now
      resultado = send("original_#{metodo}", *args, &block)
      fin = Time.now
      puts "Tiempo de ejecución de #{metodo}: #{fin - inicio} segundos"
      resultado
    end
  end
end

# 10. Clase con método que usa el módulo de medición de tiempo
class Operaciones
  extend MedirTiempo  # Usamos extend en lugar de include para métodos de clase

  def operacion_lenta
    (0..10_000_000).sum
  end

  medir_tiempo :operacion_lenta
end

# Programa principal
if __FILE__ == $PROGRAM_NAME
  puts "\n--- Función básica ---"
  saludar

  puts "\n--- Función con parámetros ---"
  puts "Resultado de funcion(5): #{funcion(5)}"

  puts "\n--- Función con varios parámetros ---"
  valor1 = 10
  valor2 = 4
  valor3 = funcion2(valor1, valor2)
  puts "Resultado de funcion2(#{valor1}, #{valor2}): #{valor3}"

  puts "\n--- Función con múltiples retornos ---"
  vector = [15, 23, 20, 11, 9, 16, 15, 22, 30, 17]
  suma, promedio, max_num, min_num = calcular_estadisticas(vector)
  puts "Suma: #{suma}, Promedio: #{'%.2f' % promedio}, Máximo: #{max_num}, Mínimo: #{min_num}"
  puts "Estadísticas completas: #{calcular_estadisticas(vector)}"

  puts "\n--- Función de caracteres ---"
  texto = "Mi nombre es Máximo decimo Meridio, comandante de los ejércitos del norte"
  resultado = caracter_mas_repetido(texto)
  puts "El carácter que más se repite en el texto es '#{resultado}'"

  puts "\n--- Función con parámetro por defecto ---"
  puts saludar_persona
  puts saludar_persona("Carlos")

  puts "\n--- Función con argumentos variables ---"
  puts "Suma de (1, 2, 3): #{sumar_numeros(1, 2, 3)}"
  puts "Suma de (4, 5, 6, 7): #{sumar_numeros(4, 5, 6, 7)}"

  puts "\n--- Función con kwargs ---"
  info_persona(nombre: "Juan", edad: 30, ciudad: "Madrid")

  puts "\n--- Función con medición de tiempo ---"
  operaciones = Operaciones.new
  puts "Resultado de operación lenta: #{operaciones.operacion_lenta}"
end