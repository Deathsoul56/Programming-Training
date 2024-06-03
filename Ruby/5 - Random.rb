require 'securerandom'
require 'rubystats'

# Números Pseudo-Aleatorios
aleatorio = rand # Numero aleatorio entre 0 y 1
puts "Número aleatorio entre 0 y 1: #{aleatorio}"

aleatorio = rand(-10..10) # Numero aleatorio entre -10 y 10
puts "Número aleatorio: #{aleatorio}"

aleatorio = Array.new(10) { rand(-10..10) } # Vector 10 números aleatorios
puts "Vector aletario: #{aleatorio}"

aleatorio = Array.new(5) { rand } # Muestra de 5 valores aleatorios
puts "Muestra aleatorio: #{aleatorio}"

aleatorio = SecureRandom.random_bytes(12) # Bytes aleatorios
puts "Bytes Aleatorios: #{aleatorio}"

aleatorio = Array.new(4) { Array.new(3) { rand(-10..10) } } # Matriz 4x3 aleatorios
puts "Matriz aletario: #{aleatorio}"

aleatorio = Array.new(2) { Array.new(2) { rand } } # Matriz 2x2 aleatorios entre 0 y 1
puts "Matris aletario entre 0 y 1: #{aleatorio}"

vector = [7, -4, -3, 7, 9, 7, 0, -5, 3, 3]
v = vector.sample
puts "El vector v = #{vector} se escoge al azar un valor #{v}"

# Permutaciones
lista = ["rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"]
puts "Lista Original = #{lista}"
lista.shuffle! # Funciones para revolver un array
puts "Lista revuelta = #{lista}"

secuencia = (1..10).to_a
puts "Secuencia original: #{secuencia}"
permutacion = secuencia.shuffle # Generamos una permutación aleatoria de la secuencia
puts "Permutación aleatoria: #{permutacion}"

# Distribuciones de probabilidad continuas
mu = 5 # Media
sd = 8 # Desviación estándar

# Valor aleatorio con distribución normal (media, Sx)
normal = Rubystats::NormalDistribution.new(mu, sd).rng
puts "Valor aleatorio con distribución normal media: #{mu} desviación estándar: #{sd} = #{normal}"

# Vector aleatorio con distribución normal (media, Sx)
normals = Rubystats::NormalDistribution.new(mu, sd).rng(10)
puts "Vector aleatorio con distribución normal media: #{mu} desviación estándar: #{sd} = #{normals}"