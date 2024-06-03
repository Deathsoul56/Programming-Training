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


