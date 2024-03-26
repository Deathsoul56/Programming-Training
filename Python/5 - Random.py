import numpy as np

# Numeros Pseudo-Aleatorios
aleatorio = np.random.random() # Numero aleatorio entre 0 y 1
print(f'Numero aleatorio entre 0 y 1: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1) # Numero aleatorio entre -10 y 10, el intervalor es cerrado-abierto [)
print(f'Numero aleatorio: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = 10) # Vector 10 numeros aleatorios
print(f'vector aletario: {aleatorio}')

aleatorio = np.random.sample(5) # Muestra de 5 valores aleatorios 
print(f'Muestra aleatorio: {aleatorio}')

aleatorio = np.random.bytes(12) # Bytes aleatorios 
print(f'Bytes Aleatorios: {aleatorio}')

aleatorio = np.random.randint(-10, 10+1, size = (4, 3)) # Matriz 2x3 aleatorios
print(f'Matris aletario: {aleatorio}')

aleatorio = np.random.rand(2, 2)  # Genera una matriz de 2x2 con números aleatorios entre 0 y 1.
print(f'Matris aletario entre 0 y 1: {aleatorio}')

vector = np.array([7, -4, -3,  7,  9,  7,  0, -5,  3,  3])
v = np.random.choice(vector)
print(f'El vector v = {vector} se escoge al azar un valor {v}')

# Permutations
lista = np.array(["rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"])
print(f'Lista Original = {lista}')
np.random.shuffle(lista) # Funciones para revolver un array
print(f'Lista revuelta = {lista}')

secuencia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Secuencia original: {secuencia}")
permutacion = np.random.permutation(secuencia) # Generamos una permutación aleatoria de la secuencia
print(f"Permutación aleatoria: {permutacion}")


# Distribuciones de probabilidad continuas
# Distribucion Normal
mu = 5 # Media
sd = 8 # Desviacion Estandas
normal = np.random.normal(loc = mu, scale = sd) # Valor aleatorio con distribcion normal (media, Sx)
print(f'Valor aleatorio con distribucion normal media: {mu} desviacion estandar: {sd} = {normal}')

normal = np.random.normal(loc = mu, scale = sd, size = 10) # Vector aleatorio con distribcion normal (media, Sx)
print(f'Vector aleatorio con distribucion normal media: {mu} desviacion estandar: {sd} = {normal}')

# Distribucion normal estandar
normalS = np.random.standard_normal() # Valor aleatorio con distribcion normal (media = 0, Sx = 1)
print(f'Valor aleatorio con distribucion normal estandar = {normalS}')

normalS = np.random.standard_normal(10) # Vector aleatorio con distribcion normal (media = 0, Sx = 1)
print(f'Vector aleatorio con distribucion normal estandar = {normalS}')

# Distribucion Log-Normal
mu_x = 1 # Parametro Posicion
sd_x = 2 # Parametro Forma
lognormal = np.random.lognormal(mean = mu, sigma = sd) # Valor aleatorio con distribcion Log-normal (Mu, Sigma)
print(f'Valor aleatorio con distribucion log-normal posicion: {mu_x} forma: {sd_x} = {lognormal}')

lognormal = np.random.lognormal(mean = mu, sigma = sd, size = 10) # Vector aleatorio con distribcion Log-normal (Mu, Sigma)
print(f'Vector aleatorio con distribucion log-normal posicion: {mu_x} forma: {sd_x} = {lognormal}')

# Distribucion Uniforme
Inferior = 2 # Limite Inferior
Superior = 5 # Limite Superior
Uniforme = np.random.uniform(low = Inferior, high = Superior) # Valor aleatorio con distribcion Uniforme (a, b)
print(f'Valor aleatorio con distribucion Uniforme a: {Inferior} b: {Superior} = {Uniforme}')

Uniforme = np.random.uniform(low = Inferior, high = Superior, size = 10) # Vector aleatorio con distribcion Uniforme (a, b)
print(f'Vector aleatorio con distribucion Uniforme a: {Inferior} b: {Superior} = {Uniforme}')

# Distribucion Triangular
Inferior = 2 # Limite Inferior
Moda = 7
Superior = 10 # Limite Superior
triangular = np.random.triangular(left = Inferior,mode = Moda, right = Superior) # Valor aleatorio con distribcion Triangular (l, m, u)
print(f'Valor aleatorio con distribucion Triangular l: {Inferior} m: {Moda} u: {Superior} = {triangular}')

triangular = np.random.triangular(left = Inferior,mode = Moda, right = Superior, size = 10) # Vector aleatorio con distribcion Triangular (l, m, u)
print(f'Vector aleatorio con distribucion Triangular l: {Inferior} m: {Moda} u: {Superior} = {triangular}')

# Distrivucion Exponencial
Lambda = 3
Exponencial = np.random.exponential(scale = Lambda) # Valor aleatorio con distribcion Exponencial (Lambda)
print(f'Valor aleatorio con distribucion Exponencial Lambda: {Lambda} = {Exponencial}')

Exponencial = np.random.exponential(scale = Lambda, size = 10) # Vector aleatorio con distribcion Exponencial (Lambda)
print(f'Vector aleatorio con distribucion Exponencial Lambda: {Lambda} = {Exponencial}')

# Distribucion T de Student
GradosLibertad = 10
T_Student = np.random.standard_t(df = GradosLibertad) # Valor aleatorio con distribcion T (Nu)
print(f'Valor aleatorio con distribucion T Nu: {GradosLibertad} = {T_Student}')

T_Student = np.random.standard_t(df = GradosLibertad, size = 10) # Vector aleatorio con distribcion T (Nu)
print(f'Vector aleatorio con distribucion T Nu: {GradosLibertad} = {T_Student}')

# Distribucion Chi Cuadrado
GradosLibertad = 10
Chi_Cuadrado = np.random.chisquare(df = GradosLibertad) # Valor aleatorio con distribcion Chi Cuadrado (Nu)
print(f'Valor aleatorio con distribucion Chi Cuadrado Nu: {GradosLibertad} = {Chi_Cuadrado}')

Chi_Cuadrado = np.random.chisquare(df = GradosLibertad, size = 10) # Vector aleatorio con distribcion Chi Cuadrado (Nu)
print(f'Vector aleatorio con distribucion Chi Cuadrado Nu: {GradosLibertad} = {Chi_Cuadrado}')

# Distribucion F de Fisher
GradosLibertad1 = 12
GradosLibertad2 = 17
F_Fisher = np.random.f(dfnum = GradosLibertad1, dfden = GradosLibertad2) # Valor aleatorio con distribcion F de Fisher (Nu_1m Nu_2)
print(f'Valor aleatorio con distribucion F de Fisher Nu_1: {GradosLibertad1} Nu_2: {GradosLibertad2} = {F_Fisher}')

F_Fisher = np.random.f(dfnum = GradosLibertad1, dfden = GradosLibertad2, size = 10) # Vector aleatorio con distribcion F de Fisher (Nu_1, Nu_2)
print(f'Vector aleatorio con distribucion F de Fisher Nu_1: {GradosLibertad1} Nu_2: {GradosLibertad2} = {F_Fisher}')

# Distribucion Gamma
alpha = 12
Lambda = 17
Gamma = np.random.gamma(shape = alpha, scale = Lambda) # Valor aleatorio con distribcion Gamma (Alpha, Lambda)
print(f'Valor aleatorio con distribucion Gamma Alpha: {alpha} Lambda: {Lambda} = {Gamma}')

Gamma = np.random.gamma(shape = alpha, scale = Lambda, size = 10) # Vector aleatorio con distribcion Gamma (Alpha, Lambda)
print(f'Vector aleatorio con distribucion Gamma Alpha: {alpha} Lambda: {Lambda} = {Gamma}')



# Distribuciones de probabilidad discretas
# Distribucion Binomial
N = 10 # Cantidad de intentos
Prop = 0.25 # Probabilidad de existo
binomial = np.random.binomial(n = N, p = Prop) # Valor aleatorio con distribcion Binomial (N, Pi)
print(f'Valor aleatorio con distribucion Binomial Intentos: {N} Probabilidad: {Prop} = {binomial}')

binomial = np.random.binomial(n = N, p = Prop, size = 10) # Vector aleatorio con distribcion binomial (N, Pi)
print(f'Vector aleatorio con distribucion Binomial Intentos: {N} Probabilidad: {Prop} = {binomial}')

# Distribucion Poisson
Lambda = 6
Poisson = np.random.poisson(lam = Lambda) # Valor aleatorio con distribcion Poisson (Lambda)
print(f'Valor aleatorio con distribucion Poisson Lambda: {Lambda} = {Poisson}')

Poisson = np.random.poisson(lam = Lambda, size = 10) # Vector aleatorio con distribcion Poisson (Lambda)
print(f'Vector aleatorio con distribucion Poisson Lambda: {Lambda} = {Poisson}')

# Distribucion Geometrica
Prop = 0.25 # Probabilidad de existo
Geometrica = np.random.geometric(p = Prop) # Valor aleatorio con distribcion Geometrica (Pi)
print(f'Valor aleatorio con distribucion Geometrica Probabilidad: {Prop} = {Geometrica}')

Geometrica = np.random.geometric(p = Prop, size = 10) # Vector aleatorio con distribcion Geometrica (Pi)
print(f'Vector aleatorio con distribucion Geometrica Probabilidad: {Prop} = {Geometrica}')


# Distribucion Hyper-Geometrica
Poblatcion = 20 # N
Categoria = 9 # K
muestra = 4 # n

# Valor aleatorio con distribcion Hyper-Geometrica (N, K, n)
HiperGeo = np.random.hypergeometric(ngood = Poblatcion, nbad = Categoria, nsample = muestra) 
print(f'Valor aleatorio con distribucion Hyper-Geometrica Poblacion: {Poblatcion} Categoria: {Categoria} muestra: {muestra} = {HiperGeo}')

# Vector aleatorio con distribcion Hyper-Geometrica (N, K, n)
HiperGeo = np.random.hypergeometric(ngood = Poblatcion, nbad = Categoria, nsample = muestra, size = 10) 
print(f'Vector aleatorio con distribucion Hyper-Geometrica Poblacion: {Poblatcion} Categoria: {Categoria} muestra: {muestra} = {HiperGeo}')