# frozen_string_literal: true

# Calcula el factorial de un número entero no negativo de manera recursiva.
#
# @param n [Integer] El número entero no negativo.
# @return [Integer] El factorial de n.
# @raise [ArgumentError] Si n no es un entero o es negativo.
def factorial(n)
  unless n.is_a?(Integer) && n >= 0
    raise ArgumentError, "El factorial solo está definido para enteros no negativos."
  end

  # Caso base
  return 1 if n == 0 || n == 1

  # Caso recursivo
  n * factorial(n - 1)
end

# Calcula el n-ésimo número de la secuencia de Fibonacci de manera recursiva.
#
# @param n [Integer] El índice del número de Fibonacci a calcular.
# @return [Integer] El n-ésimo número de Fibonacci.
# @raise [ArgumentError] Si n no es un entero positivo.
def fibonacci(n)
  raise ArgumentError, "El índice debe ser un entero positivo." if n < 1

  # Caso base
  return 1 if n == 1 || n == 2

  # Caso recursivo
  fibonacci(n - 1) + fibonacci(n - 2)
end

# Calcula la suma de una lista de números de manera recursiva.
#
# @param lista [Array<Numeric>] La lista de números.
# @return [Numeric] La suma de los elementos de la lista.
def suma_recursiva(lista)
  # Caso base: lista vacía
  return 0 if lista.empty?

  # Caso recursivo
  lista.first + suma_recursiva(lista.drop(1))
end

# Calcula el máximo común divisor (MCD) de dos números usando el algoritmo de Euclides de manera recursiva.
#
# @param a [Integer] El primer número.
# @param b [Integer] El segundo número.
# @return [Integer] El MCD de a y b.
def mcd(a, b)
  # Caso base
  return a if b == 0

  # Caso recursivo
  mcd(b, a % b)
end

# Calcula la potencia de un número de manera recursiva.
#
# @param base [Numeric] La base.
# @param exponente [Integer] El exponente (debe ser no negativo).
# @return [Numeric] base elevado a exponente.
# @raise [ArgumentError] Si el exponente es negativo.
def potencia(base, exponente)
  unless exponente.is_a?(Integer) && exponente >= 0
    raise ArgumentError, "El exponente debe ser un entero no negativo."
  end

  # Caso base
  return 1 if exponente == 0

  # Optimización para exponentes pares
  if exponente.even?
    mitad = potencia(base, exponente / 2)
    mitad * mitad
  else
    # Caso recursivo para exponentes impares
    base * potencia(base, exponente - 1)
  end
end

# Invierte una cadena de texto de manera recursiva.
#
# @param cadena [String] La cadena a invertir.
# @return [String] La cadena invertida.
def invertir_cadena(cadena)
  # Caso base
  return cadena if cadena.length <= 1

  # Caso recursivo
  cadena[-1] + invertir_cadena(cadena[0...-1])
end

# Cuenta el número de elementos en una lista de manera recursiva.
#
# @param lista [Array] La lista a contar.
# @return [Integer] El número de elementos en la lista.
def contar_elementos(lista)
  # Caso base
  return 0 if lista.empty?

  # Caso recursivo
  1 + contar_elementos(lista.drop(1))
end

# Encuentra el valor máximo en una lista de manera recursiva.
#
# @param lista [Array<Numeric>] La lista de números.
# @return [Numeric] El valor máximo en la lista.
# @raise [ArgumentError] Si la lista está vacía.
def encontrar_maximo(lista)
  raise ArgumentError, "No se puede encontrar el máximo de una lista vacía." if lista.empty?

  # Caso base: lista con un único elemento
  return lista.first if lista.length == 1

  # Caso recursivo
  mitad = lista.length / 2
  max_izquierda = encontrar_maximo(lista.take(mitad))
  max_derecha = encontrar_maximo(lista.drop(mitad))

  max_izquierda > max_derecha ? max_izquierda : max_derecha
end

# Realiza una búsqueda binaria recursiva en una lista ordenada.
#
# @param lista [Array] Lista ordenada donde buscar.
# @param elemento El elemento a buscar.
# @param inicio [Integer] Índice de inicio para la búsqueda.
# @param fin [Integer] Índice final para la búsqueda.
# @return [Integer] El índice del elemento si se encuentra, -1 en caso contrario.
def busqueda_binaria(lista, elemento, inicio = 0, fin = nil)
  fin = lista.length - 1 if fin.nil?

  # Caso base: elemento no encontrado
  return -1 if inicio > fin

  # Calcular punto medio
  medio = (inicio + fin) / 2

  # Caso base: elemento encontrado
  return medio if lista[medio] == elemento

  # Caso recursivo: buscar en la mitad izquierda
  if lista[medio] > elemento
    busqueda_binaria(lista, elemento, inicio, medio - 1)
  else
    # Caso recursivo: buscar en la mitad derecha
    busqueda_binaria(lista, elemento, medio + 1, fin)
  end
end

# Verifica si una cadena es un palíndromo de manera recursiva.
#
# @param cadena [String] La cadena a verificar.
# @return [Boolean] true si es palíndromo, false en caso contrario.
def palindromo(cadena)
  # Normalizar la cadena: minúsculas y sin espacios
  cadena = cadena.downcase.gsub(/\s/, "")

  # Caso base: cadena vacía o de un carácter
  return true if cadena.length <= 1

  # Verificar si el primer y último carácter son iguales
  return false unless cadena[0] == cadena[-1]

  # Caso recursivo: verificar el resto de la cadena
  palindromo(cadena[1...-1])
end

# Resuelve el problema de las Torres de Hanoi de manera recursiva.
#
# @param n [Integer] Número de discos.
# @param origen [String] La torre de origen.
# @param auxiliar [String] La torre auxiliar.
# @param destino [String] La torre de destino.
# @return [Array<String>] Lista de movimientos a realizar.
def torres_hanoi(n, origen, auxiliar, destino)
  movimientos = []

  hanoi_recursivo = lambda do |n, origen, auxiliar, destino|
    if n == 1
      movimientos << "Mover disco 1 desde #{origen} hasta #{destino}"
    else
      hanoi_recursivo.call(n - 1, origen, destino, auxiliar)
      movimientos << "Mover disco #{n} desde #{origen} hasta #{destino}"
      hanoi_recursivo.call(n - 1, auxiliar, origen, destino)
    end
  end

  hanoi_recursivo.call(n, origen, auxiliar, destino)
  movimientos
end

# Función auxiliar para visualizar la pila de llamadas recursivas.
#
# @param n [Integer] El valor de entrada para la función.
# @param nivel [Integer] El nivel de recursión actual.
# @param prefijo [String] Prefijo para la visualización.
# @return El resultado de la función recursiva.
def visualizar_recursion(n, nivel = 0, prefijo = "")
  # Función auxiliar para visualizar la pila de llamadas recursivas.
  indent = "  " * nivel
  puts "#{indent}→ #{prefijo}(#{n})"

  if n <= 1
    puts "#{indent}← #{prefijo}(#{n}) = 1"
    return 1
  end

  resultado = n * visualizar_recursion(n - 1, nivel + 1, prefijo)
  puts "#{indent}← #{prefijo}(#{n}) = #{resultado}"
  resultado
end

# Programa principal
if __FILE__ == $PROGRAM_NAME
  puts "\n=== INTRODUCCIÓN A LA RECURSIVIDAD EN RUBY ==="
  puts "La recursividad es una técnica donde una función se llama a sí misma para resolver un problema."
  puts "Componentes clave de una función recursiva:"
  puts "1. Caso base: Condición que detiene la recursión"
  puts "2. Caso recursivo: La función se llama a sí misma con un problema más pequeño"
  puts "3. Acercamiento al caso base: Cada llamada debe acercarse al caso base"

  # Ejemplos
  puts "\n=== EJEMPLOS DE FUNCIONES RECURSIVAS ==="

  puts "\n--- Factoriales ---"
  (0..10).each do |i|
    puts "#{i}! = #{factorial(i)}"
  end

  puts "\n--- Secuencia de Fibonacci ---"
  (1..20).each do |i|
    puts "fibonacci_#{i} = #{fibonacci(i)}"
  end

  lista = [1, 2, 3, 4, 5]
  puts "\n--- Suma recursiva ---"
  puts "Suma de #{lista}: #{suma_recursiva(lista)}"

  a, b = 48, 18
  puts "\n--- Máximo Común Divisor (MCD) ---"
  puts "MCD de #{a} y #{b}: #{mcd(a, b)}"

  puts "\n--- Potencia recursiva ---"
  base, exp = 2, 10
  puts "#{base}^#{exp} = #{potencia(base, exp)}"

  puts "\n--- Invertir cadena ---"
  texto = "Python es divertido"
  puts "\"#{texto}\" invertido: \"#{invertir_cadena(texto)}\""

  puts "\n--- Contar elementos ---"
  lista_grande = [10, 20, 30, 40, 50, 60, 70, 80, 90]
  puts "Número de elementos en #{lista_grande}: #{contar_elementos(lista_grande)}"

  puts "\n--- Encontrar máximo ---"
  lista_desordenada = [15, 7, 23, 4, 19, 8]
  puts "Máximo en #{lista_desordenada}: #{encontrar_maximo(lista_desordenada)}"

  puts "\n--- Búsqueda binaria ---"
  lista_ordenada = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  elemento = 12
  indice = busqueda_binaria(lista_ordenada, elemento)
  if indice != -1
    puts "El elemento #{elemento} se encuentra en el índice #{indice} de #{lista_ordenada}"
  else
    puts "El elemento #{elemento} no se encuentra en #{lista_ordenada}"
  end

  puts "\n--- Palíndromos ---"
  frases = ["anita lava la tina", "python", "radar", "reconocer"]
  frases.each do |frase|
    resultado = palindromo(frase) ? "es" : "no es"
    puts "\"#{frase}\" #{resultado} un palíndromo"
  end

  puts "\n--- Torres de Hanoi ---"
  num_discos = 3
  movimientos = torres_hanoi(num_discos, "A", "B", "C")
  puts "Solución para #{num_discos} discos:"
  movimientos.each_with_index do |movimiento, i|
    puts "#{i + 1}. #{movimiento}"
  end

  puts "\n=== VISUALIZACIÓN DE LA RECURSIÓN ==="
  puts "Ejemplo de visualización para factorial(4):"
  visualizar_recursion(4, 0, "factorial")

end