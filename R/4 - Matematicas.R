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
print(paste(x, "*", y, "=", x * y)) # Multiplicaci�n
print(paste(x, "/", y, "=", x / y)) # Divisi�n
print(paste(x, "%/%", "9", "=", x %/% 9)) # Divisi�n entera
print(paste(x, "%%", "9", "=", x %% 9)) # M�dulo
print(paste("???", x, "=", sqrt(x))) # Ra�z cuadrada
print(paste(x, "^", "3", "=", x^3)) # Potencia
print(paste("3???", x, "=", x^(1/3))) # Ra�z c�bica (N-�sima)
print(paste("|-", y, "|", "=", abs(-y))) # Valor absoluto
print(paste("Re(", z, ")", "=", Re(z))) # Parte real
print(paste("Im(", z, ")", "=", Im(z))) # Parte imaginaria
print(paste("|", z, "|", "=", Mod(z))) # M�dulo de un n�mero complejo
print(paste("Arg(", z, ")", "=", Arg(z))) # Argumento de un complejo
print(paste(z, "*", "=", Conj(z))) # Conjugado de un n�mero complejo
