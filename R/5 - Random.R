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
cat("Vector aleatorio con distribución normal media:", mu, "desviación estándar:", sigma, "=", toString(normal))

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

# Distribución Weibull
Alpha <- 2
Weibull <- rweibull(n = 1, shape = Alpha) # Valor aleatorio con distribución Weibull (Lambda = 1, Alpha)
cat(sprintf("Valor aleatorio con distribución Weibull Lamda: 1 Alpha: %d = %f\n", Alpha, Weibull))

Weibull <- rweibull(n = 10, shape = Alpha) # Vector aleatorio con distribución Weibull (Lambda = 1, Alpha)
cat(sprintf("Vector aleatorio con distribución Weibull Lamda: 1 Alpha: %d = %s\n", Alpha, toString(Weibull)))

# Distribución Laplace (Esta distribucion no esta por defecto en R, hay que usar VGAM)
Mu <- 2 # Parámetro de localización 
b <- 4 # Parámetro de escala
Laplace <- rlaplace(n = 1, location = Mu, scale = b) # Valor aleatorio con distribución Laplace (Mu, b)
cat(sprintf("Valor aleatorio con distribución Laplace Mu: %d b: %d = %f\n", Mu, b, Laplace))

Laplace <- rlaplace(n = 10, location = Mu, scale = b) # Vector aleatorio con distribución Laplace (Mu, b)
cat(sprintf("Vector aleatorio con distribución Laplace Mu: %d b: %d = %s\n", Mu, b, toString(Laplace)))

# Distribución Logística
Mu <- 2 # Parámetro de localización 
s <- 4 # Parámetro de escala
Logistic <- rlogis(n = 1, location = Mu, scale = s) # Valor aleatorio con distribución Logística (Mu, s)
cat(sprintf("Valor aleatorio con distribución Logística Mu: %d s: %d = %f\n", Mu, s, Logistic))

Logistic <- rlogis(n = 10, location = Mu, scale = s) # Vector aleatorio con distribución Logística (Mu, s)
cat(sprintf("Vector aleatorio con distribución Logística Mu: %d s: %d = %s\n", Mu, s, toString(Logistic)))

# Distribución Beta
alpha <- 1 # Parámetro de forma
beta <- 5 # Parámetro de forma
Beta <- rbeta(n = 1, shape1 = alpha, shape2 = beta) # Valor aleatorio con distribución Beta (alpha, beta)
cat(sprintf("Valor aleatorio con distribución Beta Alpha: %d Beta: %d = %f\n", alpha, beta, Beta))

Beta <- rbeta(n = 10, shape1 = alpha, shape2 = beta) # Vector aleatorio con distribución Beta (alpha, beta)
cat(sprintf("Vector aleatorio con distribución Beta Alpha: %d Beta: %d = %s\n", alpha, beta, toString(Beta)))

# Distribución Cauchy
x_0 <- -2 # Parámetro de localización 
gamma <- 3 # Parámetro de escala
Cauchy <- rcauchy(n = 1, location = x_0, scale = gamma) # Valor aleatorio con distribución Cauchy (x_0, gamma)
cat(sprintf("Valor aleatorio con distribución Cauchy Estándar = %f\n", Cauchy))

Cauchy <- rcauchy(n = 10, location = x_0, scale = gamma) # Vector aleatorio con distribución Cauchy (x_0, gamma)
cat(sprintf("Vector aleatorio con distribución Cauchy Estándar = %s\n", toString(Cauchy)))

# Distribución T de Student
GradosLibertad <- 10
T_Student <- rt(n = 1, df = GradosLibertad) # Valor aleatorio con distribución T (Nu)
cat(sprintf("Valor aleatorio con distribución T Nu: %d = %f\n", GradosLibertad, T_Student))

T_Student <- rt(n = 10, df = GradosLibertad) # Vector aleatorio con distribución T (Nu)
cat(sprintf("Vector aleatorio con distribución T Nu: %d = %s\n", GradosLibertad, toString(T_Student)))

# Distribución Chi Cuadrado
GradosLibertad <- 10
Chi_Cuadrado <- rchisq(n = 1, df = GradosLibertad) # Valor aleatorio con distribución Chi Cuadrado (Nu)
cat(sprintf("Valor aleatorio con distribución Chi Cuadrado Nu: %d = %f\n", GradosLibertad, Chi_Cuadrado))

Chi_Cuadrado <- rchisq(n = 10, df = GradosLibertad) # Vector aleatorio con distribución Chi Cuadrado (Nu)
cat(sprintf("Vector aleatorio con distribución Chi Cuadrado Nu: %d = %s\n", GradosLibertad, toString(Chi_Cuadrado)))

# Distribución F de Fisher
GradosLibertad1 <- 12
GradosLibertad2 <- 17
F_Fisher <- rf(n = 1, df1 = GradosLibertad1, df2 = GradosLibertad2) # Valor aleatorio con distribución F de Fisher (Nu_1, Nu_2)
cat(sprintf("Valor aleatorio con distribución F de Fisher Nu_1: %d Nu_2: %d = %f\n", GradosLibertad1, GradosLibertad2, F_Fisher))

F_Fisher <- rf(n = 10, df1 = GradosLibertad1, df2 = GradosLibertad2) # Vector aleatorio con distribución F de Fisher (Nu_1, Nu_2)
cat(sprintf("Vector aleatorio con distribución F de Fisher Nu_1: %d Nu_2: %d = %s\n", GradosLibertad1, GradosLibertad2, toString(F_Fisher)))

# Distribución Gamma
alpha <- 12 # Parámetro de localización 
Lambda <- 17 # Parámetro de escala
Gamma <- rgamma(n = 1, shape = alpha, scale = Lambda) # Valor aleatorio con distribución Gamma (Alpha, Lambda)
cat(sprintf("Valor aleatorio con distribución Gamma Alpha: %d Lambda: %d = %f\n", alpha, Lambda, Gamma))

Gamma <- rgamma(n = 10, shape = alpha, scale = Lambda) # Vector aleatorio con distribución Gamma (Alpha, Lambda)
cat(sprintf("Vector aleatorio con distribución Gamma Alpha: %d Lambda: %d = %s\n", alpha, Lambda, toString(Gamma)))

# Distribución Gumbel (Esta distribucion no esta por defecto en R, hay que usar evd)
library(evd)
mu <- 12
beta <- 17
Gumbel <- evd::rgumbel(n = 1, loc = mu, scale = beta) # Valor aleatorio con distribución Gumbel (Mu, Beta)
cat(sprintf("Valor aleatorio con distribución Gumbel Mu: %d Beta: %d = %f\n", mu, beta, Gumbel))

Gumbel <- evd::rgumbel(n = 10, loc = mu, scale = beta) # Vector aleatorio con distribución Gumbel (Mu, Beta)
cat(sprintf("Vector aleatorio con distribución Gumbel Mu: %d Beta: %d = %s\n", mu, beta, toString(Gumbel)))

# Distribución Wald (Esta distribucion no esta por defecto en R, hay que usar statmod)
library(statmod)
media <- 12 # Promedio (Parámetro de localización)
Lambda <- 17 # Parámetro de escala
Wald <- statmod::rinvgauss(n = 1, mean = media, dispersion = 1/Lambda) # Valor aleatorio con distribución Wald (Mu, Lambda)
cat(sprintf("Valor aleatorio con distribución Wald Media: %d Lambda: %d = %f\n", media, Lambda, Wald))

Wald <- statmod::rinvgauss(n = 10, mean = media, dispersion = 1/Lambda) # Vector aleatorio con distribución Wald (Mu, Lambda)
cat(sprintf("Vector aleatorio con distribución Wald Media: %d Lambda: %d = %s\n", media, Lambda, toString(Wald)))

# Distribución von Mises (Esta distribucion no esta por defecto en R, hay que usar CircStats)
library(CircStats)
Mu <- -2 # Parámetro de localización
Kappa <- 3 # Parámetro de escala
vonMises <- CircStats::rvm(n = 1, mean = Mu, k = Kappa) # Valor aleatorio con distribución von Mises (Mu, Kappa)
cat(sprintf("Valor aleatorio con distribución von Mises Mu: %d Kappa: %d = %f\n", Mu, Kappa, vonMises))

vonMises <- CircStats::rvm(n = 10, mean = Mu, k = Kappa) # Vector aleatorio con distribución von Mises (Mu, Kappa)
cat(sprintf("Vector aleatorio con distribución von Mises Mu: %d Kappa: %d = %s\n", Mu, Kappa, toString(vonMises)))

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

