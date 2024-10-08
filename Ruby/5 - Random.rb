require 'securerandom'
require 'rubystats'
require 'matrix'

# Números Pseudo-Aleatorios
aleatorio = rand # Número aleatorio entre 0 y 1
puts "Número aleatorio entre 0 y 1: #{aleatorio}"

aleatorio = rand(-10..10) # Número aleatorio entre -10 y 10 [-10, 10]
puts "Número aleatorio entre -10 y 10: #{aleatorio}"

aleatorio = Array.new(10) { rand(-10..10) } # Vector de 10 números aleatorios entre -10 y 10 [-10, 10]
puts "Vector aleatorio: #{aleatorio}"

aleatorio = Array.new(5) { rand } # Muestra de 5 valores aleatorios
puts "Muestra aleatoria: #{aleatorio}"

aleatorio = SecureRandom.random_bytes(12) # Bytes aleatorios
puts "Bytes aleatorios: #{aleatorio.inspect}" # inspect para mostrar bytes legiblemente

aleatorio = Array.new(4) { Array.new(3) { rand(-10..10) } } # Matriz 4x3 de aleatorios
puts "Matriz aleatoria: #{aleatorio}"

aleatorio = Array.new(2) { Array.new(2) { rand } } # Matriz 2x2 aleatoria entre 0 y 1
puts "Matriz aleatoria entre 0 y 1: #{aleatorio}"

vector = [7, -4, -3, 7, 9, 7, 0, -5, 3, 3]
v = vector.sample
puts "El vector v = #{vector} se escoge al azar un valor #{v}"

# Permutaciones
lista = ["rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"]
puts "Lista Original = #{lista}"
lista.shuffle! # Función para revolver un array
puts "Lista revuelta = #{lista}"

secuencia = (1..10).to_a
puts "Secuencia original: #{secuencia}"
permutacion = secuencia.shuffle # Generamos una permutación aleatoria de la secuencia
puts "Permutación aleatoria: #{permutacion}"

# Distribuciones de probabilidad continuas
# Distribución Normal
mu = 5 # Media
sd = 8 # Desviación estándar

normal = Rubystats::NormalDistribution.new(mu, sd).rng # Valor aleatorio con distribución normal (media, Sx)
puts "Valor aleatorio con distribución normal media: #{mu} desviación estándar: #{sd} = #{normal}"

normal = Rubystats::NormalDistribution.new(mu, sd).rng(10) # Vector aleatorio con distribución normal (media, Sx)
puts "Vector aleatorio con distribución normal media: #{mu} desviación estándar: #{sd} = #{normal}"

# Distribución Log-Normal
mu_x = 1 # Parámetro localización
sd_x = 2 # Parámetro Forma
lognormal_dist = Rubystats::LognormalDistribution.new(mu_x, sd_x) # Inicializa la distribucion LogNormal

lognormal = lognormal_dist.rng # Valor aleatorio con distribución Log-normal (mu_x, sd_x)
puts "Valor aleatorio con distribución log-normal localización: #{mu_x} forma: #{sd_x} = #{lognormal}"

lognormal = Array.new(10) { lognormal_dist.rng } # Vector aleatorio con distribución Log-normal (mu_x, sd_x)
puts "Vector aleatorio con distribución log-normal localización: #{mu_x} forma: #{sd_x} = #{lognormal}"

# Distribución Uniforme
inferior = 2 # Límite Inferior
superior = 5 # Límite Superior
uniforme = Rubystats::UniformDistribution.new(inferior, superior).rng # Valor aleatorio con distribución Uniforme (a, b)
puts "Valor aleatorio con distribución Uniforme a: #{inferior} b: #{superior} = #{uniforme}"

uniforme_vector = Rubystats::UniformDistribution.new(inferior, superior).rng(10) # Vector aleatorio con distribución Uniforme (a, b)
puts "Vector aleatorio con distribución Uniforme a: #{inferior} b: #{superior} = #{uniforme_vector}"

# Distribución Exponencial
Lambda = 3
exponential_dist = Rubystats::ExponentialDistribution.new(Lambda) # Inicializa la distribucion exponencial

exponencial = exponential_dist.rng # Valor aleatorio con distribución Exponencial (Lambda)
puts "Valor aleatorio con distribución Exponencial Lambda: #{Lambda} = #{exponencial}"

exponencial = Array.new(10) { exponential_dist.rng } # Vector aleatorio con distribución Exponencial (Lambda)
puts "Vector aleatorio con distribución Exponencial Lambda: #{Lambda} = #{exponencial}"

# Distribucion Weibull
k = 2  # Parámetro de forma (alpha)
Lambda = 1  # Parámetro de localización (lambda)
weibull_dist = Rubystats::WeibullDistribution.new(k, Lambda) # Inicializa la distribucion Weibull

weibull = weibull_dist.rng # Valor aleatorio con distribución Weibull (Lambda, k)
puts "Valor aleatorio con distribución Weibull (shape: #{k}, scale: #{Lambda}) = #{weibull}"

weibull = Array.new(10) { weibull_dist.rng } # Vector aleatorio con distribución Weibull (Lambda, k)
puts "Vector aleatorio con distribución Weibull (shape: #{k}, scale: #{Lambda}) = #{weibull}"

# Distribución Beta
alpha = 1.0 # Parámetro de forma
beta = 5.0 # Parámetro de forma

beta_dist = Rubystats::BetaDistribution.new(alpha, beta) # Inicializa la distribucion 

beta_dis = beta_dist.rng # Valor aleatorio con distribución Beta (alpha, beta)
puts "Valor aleatorio con distribución Beta Alpha: #{alpha} Beta: #{beta} = #{beta_dis}"

beta_dis_vector = 10.times.map { beta_dist.rng } # Vector aleatorio con distribución Beta (alpha, beta)
puts "Vector aleatorio con distribución Beta Alpha: #{alpha} Beta: #{beta} = #{beta_dis_vector}"

# Distribución Gamma
alpha = 12
lambda = 17
gamma_dist = Rubystats::GammaDistribution.new(alpha, lambda) # Inicializa la distribucion gamma

gamma_value = gamma_dist.rng # Valor aleatorio con distribución Gamma (Alpha, Lambda)
puts "Valor aleatorio con distribución Gamma Alpha: #{alpha} Lambda: #{lambda} = #{gamma_value}"

gamma_vector = Array.new(10) { gamma_dist.rng } # Vector aleatorio con distribución Gamma (Alpha, Lambda)
puts "Vector aleatorio con distribución Gamma Alpha: #{alpha} Lambda: #{lambda} = #{gamma_vector}"

# Distribución Cauchy
x_0 = 0 # Parámetro de localización 
gamma = 1 # Parámetro de forma
cauchy = Rubystats::CauchyDistribution.new(x_0, gamma) # Inicializa la distribucion Cauchy

cauchy_value = cauchy.rng # Valor aleatorio con distribución Cauchy (x_0, gamma)
puts "Valor aleatorio con distribución Cauchy x_0: #{x_0} gamma: #{gamma} = #{cauchy_value}"

cauchy_vector = Array.new(10) { cauchy.rng } # Vector aleatorio con distribución Cauchy (x_0, gamma)
puts "Vector aleatorio con distribución Cauchy = #{cauchy_vector}"

# Distribución T de Student
GradosLibertad = 10
t_dist = Rubystats::StudentTDistribution.new(GradosLibertad)

T_value = t_dist.rng # Valor aleatorio con distribcion T (Nu)
puts "Valor aleatorio con distribución T Nu: #{GradosLibertad} = #{T_value}"

T_vector = Array.new(10) { t_dist.rng } # Vector aleatorio con distribución T (Nu)
puts "Vector aleatorio con distribución T Nu: #{GradosLibertad} = #{T_vector}"


# Distribuciones de probabilidad discretas
# Distribución Binomial
N = 10 # Cantidad de intentos
Prop = 0.25 # Probabilidad de éxito
binomial = Rubystats::BinomialDistribution.new(N, Prop).rng # Valor aleatorio con distribución Binomial (N, Pi)
puts "Valor aleatorio con distribución Binomial Intentos: #{N} Probabilidad: #{Prop} = #{binomial}"

binomial = Rubystats::BinomialDistribution.new(N, Prop).rng(10) # Vector aleatorio con distribución binomial (N, Pi)
puts "Vector aleatorio con distribución Binomial Intentos: #{N} Probabilidad: #{Prop} = #{binomial}"