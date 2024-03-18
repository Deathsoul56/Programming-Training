# Numeros especiales
Pi <- pi          # Valor de pi 3.141592653589793
e <- exp(1)       # Valor de e 2.718281828459045
inf <- Inf        # Infinito Positivo
minf <- -Inf      # Infinito Negativo
NoNumero <- NaN   # No es un numero (Not a number)

cat("Valor de Pi:", Pi, "Valor de e:", e)
cat("Infinito positivo:", inf, "infinito negativo:", minf)
cat("No es un numero:", NoNumero)

# Definir algunos valores
x <- 24
y <- 17.4
z <- 3 + 4i

print(paste(x, "+", y, "=", x + y)) # Suma
print(paste(x, "-", y, "=", x - y)) # Resta
print(paste(x, "*", y, "=", x * y)) # Multiplicación
print(paste(x, "/", y, "=", x / y)) # División
print(paste(x, "%/%", "9", "=", x %/% 9)) # División entera
print(paste(x, "%%", "9", "=", x %% 9)) # Módulo
print(paste("???", x, "=", sqrt(x))) # Raíz cuadrada
print(paste(x, "^", "3", "=", x^3)) # Potencia
print(paste("3???", x, "=", x^(1/3))) # Raíz cúbica (N-ésima)
print(paste("|-", y, "|", "=", abs(-y))) # Valor absoluto
print(paste("Re(", z, ")", "=", Re(z))) # Parte real
print(paste("Im(", z, ")", "=", Im(z))) # Parte imaginaria
print(paste("|", z, "|", "=", Mod(z))) # Módulo de un número complejo
print(paste("Arg(", z, ")", "=", Arg(z))) # Argumento de un complejo
print(paste(z, "*", "=", Conj(z))) # Conjugado de un número complejo
