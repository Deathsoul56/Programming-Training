import numpy as np

# Números Pseudo-Aleatorios
aleatorio = np.random.random() # Numero aleatorio entre 0 y 1
print(f'Número aleatorio entre 0 y 1: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1) # Numero aleatorio entre -10 y 10, el intervalo es cerrado-abierto [)
print(f'Número aleatorio: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = 10) # Vector 10 números aleatorios entre 0 y 1
print(f'Vector aletario: {aleatorio}')

aleatorio = np.random.sample(5) # Muestra de 5 valores aleatorios 
print(f'Muestra aleatorio: {aleatorio}')

aleatorio = np.random.bytes(12) # Bytes aleatorios 
print(f'Bytes Aleatorios: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = (4, 3)) # Matriz 2x3 aleatorios
print(f'Matriz aletario: {aleatorio}')

aleatorio = np.random.rand(2, 2)  # Genera una matriz de 2x2 con números aleatorios entre 0 y 1.
print(f'Matris aletario entre 0 y 1: {aleatorio}')

vector = np.array([7, -4, -3,  7,  9,  7,  0, -5,  3,  3])
v = np.random.choice(vector)
print(f'El vector v = {vector} se escoge al azar un valor {v}')

# Permutaciones
lista = np.array(["rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"])
print(f'Lista Original = {lista}')
np.random.shuffle(lista) # Funciones para revolver un array
print(f'Lista revuelta = {lista}')

secuencia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Secuencia original: {secuencia}")
permutacion = np.random.permutation(secuencia) # Generamos una permutación aleatoria de la secuencia
print(f"Permutación aleatoria: {permutacion}")

# Distribuciones de probabilidad continuas
# Distribución Normal
mu = 5 # Media
sd = 8 # Desviación Estándar
normal = np.random.normal(loc = mu, scale = sd) # Valor aleatorio con distribución normal (media, Sx)
print(f'Valor aleatorio con distribución Normal media: {mu} desviación estándar: {sd} = {normal}')

normal = np.random.normal(loc = mu, scale = sd, size = 10) # Vector aleatorio con distribución normal (media, Sx)
print(f'Vector aleatorio con distribución Normal media: {mu} desviación estándar: {sd} = {normal}')

# Distribución Normal Estándar
normalS = np.random.standard_normal() # Valor aleatorio con distribución normal (media = 0, Sx = 1)
print(f'Valor aleatorio con distribución Normal Estándar = {normalS}')

normalS = np.random.standard_normal(10) # Vector aleatorio con distribución normal (media = 0, Sx = 1)
print(f'Vector aleatorio con distribución Normal Estándar = {normalS}')

# Distribución Log-Normal
mu_x = 1 # Parámetro localización
sd_x = 2 # Parámetro Forma
lognormal = np.random.lognormal(mean = mu, sigma = sd) # Valor aleatorio con distribcion Log-normal (Mu, Sigma)
print(f'Valor aleatorio con distribución log-normal localización: {mu_x} forma: {sd_x} = {lognormal}')

lognormal = np.random.lognormal(mean = mu, sigma = sd, size = 10) # Vector aleatorio con distribución Log-normal (Mu, Sigma)
print(f'Vector aleatorio con distribución log-normal localización: {mu_x} forma: {sd_x} = {lognormal}')

# Distribución Uniforme
Inferior = 2 # Límite Inferior
Superior = 5 # Límite Superior
Uniforme = np.random.uniform(low = Inferior, high = Superior) # Valor aleatorio con distribución Uniforme (a, b)
print(f'Valor aleatorio con distribución Uniforme a: {Inferior} b: {Superior} = {Uniforme}')

Uniforme = np.random.uniform(low = Inferior, high = Superior, size = 10) # Vector aleatorio con distribución Uniforme (a, b)
print(f'Vector aleatorio con distribución Uniforme a: {Inferior} b: {Superior} = {Uniforme}')

# Distribución Triangular
Inferior = 2 # Límite Inferior
Moda = 7
Superior = 10 # Limite Superior
triangular = np.random.triangular(left = Inferior,mode = Moda, right = Superior) # Valor aleatorio con distribución Triangular (l, m, u)
print(f'Valor aleatorio con distribución Triangular l: {Inferior} m: {Moda} u: {Superior} = {triangular}')

triangular = np.random.triangular(left = Inferior,mode = Moda, right = Superior, size = 10) # Vector aleatorio con distribución Triangular (l, m, u)
print(f'Vector aleatorio con distribución Triangular l: {Inferior} m: {Moda} u: {Superior} = {triangular}')

# Distribución Potencia
alpha = 3
Potencia = np.random.power(a = alpha) # Valor aleatorio con distribución Potencia (alpha)
print(f'Valor aleatorio con distribución Potencia alpha: {alpha} = {Potencia}')

Potencia = np.random.power(a = alpha, size = 10) # Vector aleatorio con distribución Potencia (alpha)
print(f'Vector aleatorio con distribución Potencia alpha: {alpha} = {Potencia}')

# Distribución Exponencial
Lambda = 3
Exponencial = np.random.exponential(scale = Lambda) # Valor aleatorio con distribución Exponencial (Lambda)
print(f'Valor aleatorio con distribución Exponencial Lambda: {Lambda} = {Exponencial}')

Exponencial = np.random.exponential(scale = Lambda, size = 10) # Vector aleatorio con distribución Exponencial (Lambda)
print(f'Vector aleatorio con distribución Exponencial Lambda: {Lambda} = {Exponencial}')

# Distribución Exponencial Estándar
ExponencialS = np.random.standard_exponential() # Valor aleatorio con distribución Exponencial (Lambda = 1)
print(f'Valor aleatorio con distribución Exponencial Lambda: {1} = {ExponencialS}')

ExponencialS = np.random.standard_exponential(size = 10) # Vector aleatorio con distribución Exponencial (Lambda = 1)
print(f'Vector aleatorio con distribución Exponencial Lambda: {1} = {ExponencialS}')

# Distribución Rayleigh 
Sigma = 2.5
Rayleigh = np.random.rayleigh(scale = Sigma) # Valor aleatorio con distribución Rayleigh (Sigma)
print(f'Valor aleatorio con distribución Rayleigh Lambda: {Sigma} = {Rayleigh}')

Rayleigh = np.random.rayleigh(scale = Sigma, size = 10) # Vector aleatorio con distribución Rayleigh (Sigma)
print(f'Vector aleatorio con distribución Rayleigh Lambda: {Sigma} = {Rayleigh}')

# Distribucion Weibull
Alpha = 2
Weibull = np.random.weibull(a = Alpha) # Valor aleatorio con distribución Weibull (Lambda = 1, Alpha)
print(f'Valor aleatorio con distribución Weibull Lamda: 1 Alpha: {Lambda} = {Weibull}')

Weibull = np.random.weibull(a = Alpha, size = 10) # Vector aleatorio con distribución Weibull (Lambda = 1, Alpha)
print(f'Vector aleatorio con distribución Weibull Lamda: 1 Alpha: {Lambda} = {Weibull}')

# Distribución Laplace
Mu = 2 # Parámetro de localización 
b = 4 # Parámetro de escala
Laplace = np.random.laplace(loc = Mu, scale = b) # Valor aleatorio con distribución Laplace (Mu, b)
print(f'Valor aleatorio con distribución Laplace Mu: {Mu} b: {b} = {Laplace}')

Laplace = np.random.laplace(loc = Mu, scale = b, size = 10) # Vector aleatorio con distribución Laplace (Mu, b)
print(f'Vector aleatorio con distribución Laplace Mu: {Mu} b: {b} = {Laplace}')

# Distribución Logistic
Mu = 2 # Parámetro de localización 
s = 4 # Parámetro de escala
Logistic = np.random.logistic(loc = Mu, scale = s) # Valor aleatorio con distribución Logistic (Mu, s)
print(f'Valor aleatorio con distribución Logistica Mu: {Mu} s: {s} = {Logistic}')

Logistic = np.random.logistic(loc = Mu, scale = s, size = 10) # Vector aleatorio con distribución Logistic (Mu, s)
print(f'Vector aleatorio con distribución Logistica Mu: {Mu} s: {s} = {Logistic}')

# Distribución Beta
alpha = 1 # Parámetro de forma
beta = 5 # Parámetro de forma
Logistic = np.random.beta(a = alpha, b = beta) # Valor aleatorio con distribución Beta (alpha, beta)
print(f'Valor aleatorio con distribución Beta Alpha: {alpha} Beta: {beta} = {Logistic}')

Logistic = np.random.beta(a = alpha, b = beta, size = 10) # Vector aleatorio con distribución Beta (alpha, beta)
print(f'Vector aleatorio con distribución Beta Alpha: {alpha} Beta: {beta} = {Logistic}')

# Distribución Cauchy Estándar
Cauchy = np.random.standard_cauchy() # Valor aleatorio con distribución Cauchy Estándar (x_0 = 0, gamma = 1)
print(f'Valor aleatorio con distribución Cauchy Estándar = {Cauchy}')

Cauchy = np.random.standard_cauchy(size = 10) # Vector aleatorio con distribución Cauchy Estándar (x_0 = 0, gamma = 1)
print(f'Vector aleatorio con distribución Cauchy Estándar = {Cauchy}')

# Distribución T de Student
GradosLibertad = 10
T_Student = np.random.standard_t(df = GradosLibertad) # Valor aleatorio con distribcion T (Nu)
print(f'Valor aleatorio con distribución T Nu: {GradosLibertad} = {T_Student}')

T_Student = np.random.standard_t(df = GradosLibertad, size = 10) # Vector aleatorio con distribución T (Nu)
print(f'Vector aleatorio con distribución T Nu: {GradosLibertad} = {T_Student}')

# Distribución Chi Cuadrado
GradosLibertad = 10
Chi_Cuadrado = np.random.chisquare(df = GradosLibertad) # Valor aleatorio con distribución Chi Cuadrado (Nu)
print(f'Valor aleatorio con distribución Chi Cuadrado Nu: {GradosLibertad} = {Chi_Cuadrado}')

Chi_Cuadrado = np.random.chisquare(df = GradosLibertad, size = 10) # Vector aleatorio con distribcion Chi Cuadrado (Nu)
print(f'Vector aleatorio con distribución Chi Cuadrado Nu: {GradosLibertad} = {Chi_Cuadrado}')

# Distribución F de Fisher
GradosLibertad1 = 12
GradosLibertad2 = 17
F_Fisher = np.random.f(dfnum = GradosLibertad1, dfden = GradosLibertad2) # Valor aleatorio con distribución F de Fisher (Nu_1m Nu_2)
print(f'Valor aleatorio con distribución F de Fisher Nu_1: {GradosLibertad1} Nu_2: {GradosLibertad2} = {F_Fisher}')

F_Fisher = np.random.f(dfnum = GradosLibertad1, dfden = GradosLibertad2, size = 10) # Vector aleatorio con distribución F de Fisher (Nu_1, Nu_2)
print(f'Vector aleatorio con distribución F de Fisher Nu_1: {GradosLibertad1} Nu_2: {GradosLibertad2} = {F_Fisher}')

# Distribución Gamma
alpha = 12
Lambda = 17
Gamma = np.random.gamma(shape = alpha, scale = Lambda) # Valor aleatorio con distribución Gamma (Alpha, Lambda)
print(f'Valor aleatorio con distribución Gamma Alpha: {alpha} Lambda: {Lambda} = {Gamma}')

Gamma = np.random.gamma(shape = alpha, scale = Lambda, size = 10) # Vector aleatorio con distribución Gamma (Alpha, Lambda)
print(f'Vector aleatorio con distribución Gamma Alpha: {alpha} Lambda: {Lambda} = {Gamma}')

# Distribución Gamma Estándar
alpha = 12
Gamma = np.random.standard_gamma(shape = alpha) # Valor aleatorio con distribución Gamma Estándar (Alpha, Lambda = 1)
print(f'Valor aleatorio con distribución Gamma Estándar Alpha: {alpha} Lambda: {1} = {Gamma}')

Gamma = np.random.standard_gamma(shape = alpha, size = 10) # Vector aleatorio con distribución Gamma Estándar (Alpha, Lambda = 1)
print(f'Vector aleatorio con distribución Gamma Estándar Alpha: {alpha} Lambda: {1} = {Gamma}')

# Distribución Gumbel
mu = 12
beta = 17
Gumbel = np.random.gumbel(loc = mu, scale = beta) # Valor aleatorio con distribución Gumbel (Mu, Beta)
print(f'Valor aleatorio con distribución Gamma Mu: {mu} Beta: {beta} = {Gumbel}')

Gumbel = np.random.gumbel(loc = mu, scale = beta, size = 10) # Vector aleatorio con distribución Gumbel (Mu, Beta)
print(f'Vector aleatorio con distribución Gamma Mu: {mu} Beta: {beta} = {Gumbel}')

# Distribución Wald
media = 12 # Promedio (Parámetro de localización)
Lambda = 17 # Parámetro de escala
Wald = np.random.wald(mean = media, scale = Lambda) # Valor aleatorio con distribución Wald (Mu, Lambda)
print(f'Valor aleatorio con distribución Wald Media: {media} Lambda: {Lambda} = {Wald}')

Wald = np.random.wald(mean = media, scale = Lambda, size = 10) # Vector aleatorio con distribución Wald (Mu, Lambda)
print(f'Vector aleatorio con distribución Wald Media: {media} Lambda: {Lambda} = {Wald}')

# Distribución von Mises
Mu = -2 # Parámetro de localización
Kappa = 3 # Parámetro de escala
vonMises = np.random.vonmises(mu = Mu, kappa = Kappa) # Valor aleatorio con distribución von Mises (Mu, Kappa)
print(f'Valor aleatorio con distribución von Mises Mu: {Mu} Kappa: {Kappa} = {vonMises}')

vonMises = np.random.vonmises(mu = Mu, kappa = Kappa, size = 10) # Vector aleatorio con distribución von Mises (Mu, Kappa)
print(f'Vector aleatorio con distribución von Mises Mu: {Mu} Kappa: {Kappa} = {vonMises}')

# Distribuciones de probabilidad discretas
# Distribución Binomial
N = 10 # Cantidad de intentos
Prop = 0.25 # Probabilidad de existo
binomial = np.random.binomial(n = N, p = Prop) # Valor aleatorio con distribución Binomial (N, Pi)
print(f'Valor aleatorio con distribución Binomial Intentos: {N} Probabilidad: {Prop} = {binomial}')

binomial = np.random.binomial(n = N, p = Prop, size = 10) # Vector aleatorio con distribución binomial (N, Pi)
print(f'Vector aleatorio con distribución Binomial Intentos: {N} Probabilidad: {Prop} = {binomial}')

# Distribucion Poisson
Lambda = 6
Poisson = np.random.poisson(lam = Lambda) # Valor aleatorio con distribución Poisson (Lambda)
print(f'Valor aleatorio con distribución Poisson Lambda: {Lambda} = {Poisson}')

Poisson = np.random.poisson(lam = Lambda, size = 10) # Vector aleatorio con distribución Poisson (Lambda)
print(f'Vector aleatorio con distribución Poisson Lambda: {Lambda} = {Poisson}')

# Distribución Geométrica
Prop = 0.25 # Probabilidad de existo
Geometrica = np.random.geometric(p = Prop) # Valor aleatorio con distribución Geométrica (Pi)
print(f'Valor aleatorio con distribución Geométrica Probabilidad: {Prop} = {Geometrica}')

Geometrica = np.random.geometric(p = Prop, size = 10) # Vector aleatorio con distribución Geométrica (Pi)
print(f'Vector aleatorio con distribución Geométrica Probabilidad: {Prop} = {Geometrica}')

# Distribución Binomial Negativa
N = 10 # Cantidad de intentos
Prop = 0.25 # Probabilidad de existo
Nbinomial = np.random.negative_binomial(n = N, p = Prop) # Valor aleatorio con distribución Binomial Negativa (N, Pi)
print(f'Valor aleatorio con distribución Binomial Negativa Intentos: {N} Probabilidad: {Prop} = {binomial}')

Nbinomial = np.random.negative_binomial(n = N, p = Prop, size = 10) # Vector aleatorio con distribución Binomial Negativa (N, Pi)
print(f'Vector aleatorio con distribución Binomial Negativa Intentos: {N} Probabilidad: {Prop} = {binomial}')

# Distribución Hyper-Geométrica
Poblacion = 20 # N
Categoria = 9 # K
muestra = 4 # n

# Valor aleatorio con distribución Hyper-Geométrica (N, K, n)
HiperGeo = np.random.hypergeometric(ngood = Poblacion, nbad = Categoria, nsample = muestra) 
print(f'Valor aleatorio con distribución Hyper-Geométrica Población: { Poblacion } Categoría: {Categoria} muestra: {muestra} = {HiperGeo}')

# Vector aleatorio con distribución Hyper-Geométrica (N, K, n)
HiperGeo = np.random.hypergeometric(ngood = Poblacion, nbad = Categoria, nsample = muestra, size = 10) 
print(f'Vector aleatorio con distribución Hyper-Geométrica Poblacion: {Poblacion} Categoria: {Categoria} muestra: {muestra} = {HiperGeo}')

# Distribución Logarítmica
p = 0.5
logaritmica = np.random.logseries(p = p) # Valor aleatorio con distribución Logarítmica (p)
print(f'Valor aleatorio con distribución Logarítmica p: {p} = {logaritmica}')

logaritmica = np.random.logseries(p = p, size = 10) # Vector aleatorio con distribución Logarítmica (p)
print(f'Vector aleatorio con distribución Logarítmica p: {p} = {logaritmica}')
