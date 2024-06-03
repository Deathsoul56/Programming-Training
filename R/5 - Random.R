# Número aleatorio entre 0 y 1
aleatorio <- runif(1)
cat("Número aleatorio entre 0 y 1:", aleatorio)

# Número aleatorio entre -10 y 10
aleatorio <- sample(-10:10, 1, replace = TRUE)
cat("Número aleatorio:", aleatorio)

# Vector de 10 números aleatorios entre -10 y 10
aleatorio <- sample(-10:10, 10, replace = TRUE)
cat("Vector aleatorio:", toString(aleatorio))

# Muestra de 5 valores aleatorios entre 0 y 1
aleatorio <- runif(5)
cat("Muestra aleatoria:", toString(aleatorio))

# Bytes aleatorios
aleatorio <- as.raw(sample(0:255, 12, replace = TRUE))
cat("Bytes aleatorios:", toString(aleatorio))

# Matriz 4x3 de números aleatorios entre -10 y 10
aleatorio <- matrix(sample(-10:10, 4*3, replace = TRUE), nrow = 4, ncol = 3)
cat("Matriz aleatoria:") 
aleatorio

# Matriz 2x2 de números aleatorios entre 0 y 1
aleatorio <- matrix(runif(2*2), nrow = 2, ncol = 2)
cat("Matriz aleatoria entre 0 y 1:")
aleatorio

# Seleccionar un valor aleatorio del vector
vector <- c(7, -4, -3,  7,  9,  7,  0, -5,  3,  3)
v <- sample(vector, 1)
print(paste("El vector se escoge al azar un valor:", v))

# Permutaciones
lista <- c("rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro")
print(paste("Lista Original =", toString(lista)))
lista_permutada <- sample(lista, length(lista)) # Funciones para revolver un array
print(paste("Lista revuelta =", toString(lista_permutada)))

secuencia <- 1:10 # Vector de secuencia
print(paste("Secuencia original:", toString(secuencia)))
permutacion <- sample(secuencia) # Permutar el vector
print(paste("Permutación aleatoria:", toString(permutacion)))

# Distribuciones de probabilidad continuas
# Distribución Normal
mu <- 5  # Media
sigma <- 8  # Desviación estándar

normal <- rnorm(n = 1, mean = mu, sd = sigma) # Valor aleatorio con distribución normal
cat("Valor aleatorio con distribución normal media:", mu, "desviación estándar:", sigma, "=", normal)

normal <- rnorm(n = 10, mean = mu, sd = sigma) # Vector aleatorio con distribución normal
print(paste("Vector aleatorio con distribución normal media:", mu, "desviación estándar:", sigma, "=", toString(normal)))

# Distribución Log-Normal
mu_x <- 1 # Parámetro de localización
sd_x <- 2 # Parámetro de forma

lognormal <- rlnorm(n = 1, meanlog = mu_x, sdlog = sd_x) # Valor aleatorio con distribución log-normal
cat(sprintf('Valor aleatorio con distribución log-normal localización: %f forma: %f = %f\n', mu_x, sd_x, lognormal))

lognormal <- rlnorm(n = 10, meanlog = mu_x, sdlog = sd_x) # Vector aleatorio con distribución log-normal
cat(sprintf('Vector aleatorio con distribución log-normal localización: %f forma: %f = %s\n', mu_x, sd_x, paste(lognormal, collapse = ", ")))

# Distribución Uniforme
Inferior <- 2 # Límite Inferior
Superior <- 5 # Límite Superior

Uniforme <- runif(n = 1, min = Inferior, max = Superior) # Valor aleatorio con distribución Uniforme
cat(sprintf('Valor aleatorio con distribución Uniforme a: %f b: %f = %f\n', Inferior, Superior, Uniforme))

Uniforme <- runif(n = 10, min = Inferior, max = Superior) # Vector aleatorio con distribución Uniforme
cat(sprintf('Vector aleatorio con distribución Uniforme a: %f b: %f = %s\n', Inferior, Superior, paste(Uniforme, collapse = ", ")))

# Distribución Triangular (Esta distribucion no esta por defecto en R)
library(triangle)
Inferior <- 2 # Límite Inferior
Moda <- 7
Superior <- 10 # Límite Superior

triangular <- rtriangle(n = 1, a = Inferior, b = Superior, c = Moda) # Valor aleatorio con distribución Triangular
cat(sprintf('Valor aleatorio con distribución Triangular l: %f m: %f u: %f = %f\n', Inferior, Moda, Superior, triangular))

triangular <- rtriangle(n = 10, a = Inferior, b = Superior, c = Moda) # Vector aleatorio con distribución Triangular
cat(sprintf('Vector aleatorio con distribución Triangular l: %f m: %f u: %f = %s\n', Inferior, Moda, Superior, paste(triangular, collapse = ", ")))

# Distribución Potencia
alpha <- 3

Potencia <- rbeta(n = 1, 1, alpha) # Valor aleatorio con distribución Potencia
cat(sprintf('Valor aleatorio con distribución Potencia alpha: %f = %f\n', alpha, Potencia))

Potencia <- rbeta(n = 10, 1, alpha) # Vector aleatorio con distribución Potencia
cat(sprintf('Vector aleatorio con distribución Potencia alpha: %f = %s\n', alpha, paste(Potencia, collapse = ", ")))

# Distribución Exponencial
Lambda <- 3

Exponencial <- rexp(n = 1, rate = 1/Lambda) # Valor aleatorio con distribución Exponencial
cat(sprintf('Valor aleatorio con distribución Exponencial Lambda: %f = %f\n', Lambda, Exponencial))

Exponencial <- rexp(n = 10, rate = 1/Lambda) # Vector aleatorio con distribución Exponencial
cat(sprintf('Vector aleatorio con distribución Exponencial Lambda: %f = %s\n', Lambda, paste(Exponencial, collapse = ", ")))


# Distribución Rayleigh (Esta distribucion no esta por defecto en R)
library(VGAM)
Sigma <- 2.5

#Usando Propiedades de la distribucion Rayleigh X~Exp(Lamda) --> Y = sqrt(X) ~ Rayleigh(1 / sqrt(2 * Lamda))
Rayleigh <- sqrt(rexp(n = 1, rate = 1/(2*Sigma^2))) # Valor aleatorio con distribución Rayleigh
cat(sprintf('Valor aleatorio con distribución Rayleigh Lambda: %f = %f\n', Sigma, Rayleigh))

Rayleigh <- sqrt(rexp(n = 10, rate = 1/(2*Sigma^2))) # Vector aleatorio con distribución Rayleigh
cat(sprintf('Vector aleatorio con distribución Rayleigh Lambda: %f = %s\n', Sigma, paste(Rayleigh, collapse = ", ")))

# Usando la libreria VGAM
Rayleigh <- rrayleigh(n = 1, scale = Sigma) # Valor aleatorio con distribución Rayleigh
cat(sprintf('Valor aleatorio con distribución Rayleigh Lambda: %f = %f\n', Sigma, Rayleigh))

Rayleigh <- rrayleigh(n = 10, scale = Sigma) # Vector aleatorio con distribución Rayleigh
cat(sprintf('Vector aleatorio con distribución Rayleigh Lambda: %f = %s\n', Sigma, paste(Rayleigh, collapse = ", ")))



# Distribuciones de probabilidad discretas
# Distribución Binomial
N <- 10 # Cantidad de intentos
Prop <- 0.25 # Probabilidad de éxito

binomial <- rbinom(n = 1, size = N, prob = Prop) # Valor aleatorio con distribución Binomial
cat(sprintf('Valor aleatorio con distribución Binomial Intentos: %d Probabilidad: %f = %d\n', N, Prop, binomial))

binomial <- rbinom(n = 10, size = N, prob = Prop) # Vector aleatorio con distribución Binomial
cat(sprintf('Vector aleatorio con distribución Binomial Intentos: %d Probabilidad: %f = %s\n', N, Prop, paste(binomial, collapse = ", ")))

# Distribución Poisson
Lambda <- 6

Poisson <- rpois(n = 1, lambda = Lambda) # Valor aleatorio con distribución Poisson
cat(sprintf('Valor aleatorio con distribución Poisson Lambda: %f = %d\n', Lambda, Poisson))

Poisson <- rpois(n = 10, lambda = Lambda) # Vector aleatorio con distribución Poisson
cat(sprintf('Vector aleatorio con distribución Poisson Lambda: %f = %s\n', Lambda, paste(Poisson, collapse = ", ")))

# Distribución Geométrica
Prop <- 0.25

Geometrica <- rgeom(n = 1, prob = Prop) # Valor aleatorio con distribución Geométrica
cat(sprintf('Valor aleatorio con distribución Geométrica Probabilidad: %f = %d\n', Prop, Geometrica))

Geometrica <- rgeom(n = 10, prob = Prop) # Vector aleatorio con distribución Geométrica
cat(sprintf('Vector aleatorio con distribución Geométrica Probabilidad: %f = %s\n', Prop, paste(Geometrica, collapse = ", ")))

# Distribución Hipergeométrica
Poblacion <- 20 # N
Categoria <- 9 # K
muestra <- 4 # n

HiperGeo <- rhyper(1, m = Categoria, n = Poblacion - Categoria, k = muestra) # Valor aleatorio con distribución Hipergeométrica
cat(sprintf('Valor aleatorio con distribución Hyper-Geométrica Población: %d Categoría: %d muestra: %d = %d\n', Poblacion, Categoria, muestra, HiperGeo))

HiperGeo <- rhyper(10, m = Categoria, n = Poblacion - Categoria, k = muestra) # Vector aleatorio con distribución Hipergeométrica
cat(sprintf('Vector aleatorio con distribución Hyper-Geométrica Población: %d Categoría: %d muestra: %d = %s\n', Poblacion, Categoria, muestra, paste(HiperGeo, collapse = ", ")))

# Distribución Logarítmica
p <- 0.5

logaritmica <- rlnorm(n = 1, p) # Valor aleatorio con distribución Logarítmica
cat(sprintf('Valor aleatorio con distribución Logarítmica p: %f = %d\n', p, logaritmica))

logaritmica <- rlnorm(n = 10, p) # Vector aleatorio con distribución Logarítmica
cat(sprintf('Vector aleatorio con distribución Logarítmica p: %f = %s\n', p, paste(logaritmica, collapse = ", ")))

