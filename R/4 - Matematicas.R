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

cat(x, "+", y, "=", x + y)       # Suma
cat(x, "-", y, "=", x - y)       # Resta
cat(x, "*", y, "=", x * y)       # Multiplicaci�n
cat(x, "/", y, "=", x / y)       # Divisi�n
cat(x, "%/%", "9", "=", x %/% 9) # Divisi�n entera
cat(x, "%%", "9", "=", x %% 9)   # M�dulo
cat("???", x, "=", sqrt(x))      # Ra�z cuadrada
cat(x, "^", "3", "=", x^3)       # Potencia
cat("3???", x, "=", x^(1/3))     # Ra�z c�bica (N-�sima)
cat("|-", y, "|", "=", abs(-y))  # Valor absoluto
cat("Re(", z, ")", "=", Re(z))   # Parte real
cat("Im(", z, ")", "=", Im(z))   # Parte imaginaria
cat("|", z, "|", "=", Mod(z))    # M�dulo de un n�mero complejo
cat("Arg(", z, ")", "=", Arg(z)) # Argumento de un complejo
cat(z, "*", "=", Conj(z))        # Conjugado de un n�mero complejo

# Funciones matem�ticas
cat(sprintf("e^2 = %f\n", exp(2)))                # Funci�n exponencial
cat(sprintf("Ln(%f) = %f\n", x, log(x)))          # Logaritmo natural
cat(sprintf("Log_7(%f) = %f\n", x, log(x, base = 7)))  # Logaritmo de cualquier base
cat(sprintf("floor(%f) = %f\n", y, floor(y)))     # Funci�n piso
cat(sprintf("Ceil(%f) = %f\n", y, ceiling(y)))    # Funci�n techo
cat(sprintf("???(5^2+12^2) = %f\n", sqrt(5^2 + 12^2))) # Hipotenusa

# Funciones Trigonom�tricas en R (Por defecto est�n en Radianes)
cat(sprintf("sin(??/6) = %f\n", sin(pi/6)))         # Funci�n Seno
cat(sprintf("cos(??/6) = %f\n", cos(pi/6)))         # Funci�n Coseno
cat(sprintf("tg(??/6) = %f\n", tan(pi/6)))          # Funci�n Tangente
cat(sprintf("sec(??/6) = %f\n", 1 / cos(pi/6)))     # Funci�n Secante
cat(sprintf("csc(??/6) = %f\n", 1 / sin(pi/6)))     # Funci�n Cosecante
cat(sprintf("cotg(??/6) = %f\n", 1 / tan(pi/6)))    # Funci�n Cotangente

#Funciones Trigonom�tricas Inversas
cat("Arcosen(1/2) =", asin(1/2), "\n")   # Arcoseno
cat("Arcocosen(1/2) =", acos(1/2), "\n") # Arcocoseno
cat("Arcotg(1/2) =", atan(1/2), "\n")    # Arcotangente

library(pracma)
# Cambios de Angulos
cat("180� en radianes es:", deg2rad(180), "\n")    # De deg a radianes
cat("??/4 en grados es:", rad2deg(pi/4), "\n")      # De radianes a deg

# Funciones Hiperb�licas
cat("sinh(3) =", sinh(3))        # Funci�n Seno Hiperb�lico
cat("cosh(3) =", cosh(3))        # Funci�n Coseno Hiperb�lico
cat("tanh(3) =", tanh(3))        # Funci�n Tangente Hiperb�lico
cat("sech(3) =", 1 / cosh(3))    # Funci�n Secante Hiperb�lico
cat("csch(3) =", 1 / sinh(3))    # Funci�n Cosecante Hiperb�lico
cat("cotanh(3) =", 1 / tanh(3))  # Funci�n Cotangente Hiperb�lico

# Funciones Hiperb�licas Inversas
cat("Arcosinh(5) =", asinh(5))        # Funci�n ArcoSeno Hiperb�lico
cat("Arcocosh(5) =", acosh(5))        # Funci�n ArcoCoseno Hiperb�lico
cat("Arcotanh(1/2) =", atanh(1/2))    # Funci�n ArcoTangente Hiperb�lico

# Funciones inversas restante
"
?? = arcsec(x)
sec(??) = x
1 / cos(??) = x
cos(??) = 1 / x
?? = arccos(1/x)
"
cat("Arcsec(5) =", acos(1 / 5))          # Funci�n ArcoSecante
cat("Arccsc(5) =", asin(1 / 5))          # Funci�n ArcoCosecante
cat("Arccotg(5) =", atan(1 / 5))         # Funci�n ArcoCotangente
cat("Arcsech(1/2) =", acosh(1 / (1/2)))  # Funci�n ArcoSecante Hiperb�lico
cat("Arccsch(5) =", asinh(1 / 5))        # Funci�n ArcoCosecante Hiperb�lico
cat("Arccotanh(5) =", atanh(1 / 5))      # Funci�n ArcoCotangente Hiperb�lico

# Grafico de una funcion f(x)
x <- seq(-5, 5, length.out = 50) # Crear un vector x que va de -5 a 5 con 50 elementos
y <- exp(x) # Calcular la funcion

# Crear el gr�fico
plot(x, y, 
     type = "l", 
     col = "blue", 
     xlab = "x", 
     ylab = "y", 
     main = "Gr�fica de y = x^2"
)

# R tambien cuenta con una libreria para hacer graficar con mejor estilo
library(ggplot2)
data <- data.frame(x = x, y = y) # Crear un data frame con los datos
ggplot(data, aes(x = x, y = y)) +
  geom_line(color = "#ff00a2") +           # L�nea rosado
  labs(x = "x", y = "Funci�n: exp(x)",     # Etiquetas de los ejes
       title = "Funci�n Exponencial") +    # T�tulo del gr�fico
  xlim(-6, 6) +                            # L�mites del eje x
  ylim(-1, 20) +                           # L�mites del eje y
  theme_minimal()                          # Tema del gr�fico


# Grafico de puntos
x <- sample(-100:100, 50, replace = TRUE)
y <- sample(-100:100, 50, replace = TRUE)

# Graficar los datos
plot(x, y, 
     type = "p",  # Tipo de gr�fico: puntos
     col = "#ff00a2",  # Color de los puntos
     xlab = "Valor x", ylab = "Valor y",  # Etiquetas de los ejes
     main = "Scatterplot",  # T�tulo del gr�fico
     xlim = c(-105, 105), ylim = c(-105, 105)  # L�mites de los ejes
)
grid()  # Agregar cuadr�cula


# Grafico de Barras
categorias <- c('Rojo', 'Azul', 'Verde', 'Amarillo', 'Blanco')
valores <- c(23, 45, 56, 78, 33)
colores_hex <- c('#FF5733', '#00FF00', '#0000FF', '#FFA500', '#800080')

# Crear el gr�fico de barras
barplot(valores, names.arg = categorias, col = colores_hex,
        xlab = 'Categor�as', ylab = 'Valores', main = 'Gr�fico de barras',
        legend.text = 'Preferencias', args.legend = list(x = 'topright'))

# Histograma
datos <- rnorm(1000)  # 1000 puntos de datos distribuidos normalmente

# Crear el histograma
hist(datos, breaks = 30, col = 'skyblue', border = 'black',
     xlab = 'Valor', ylab = 'Frecuencia', main = 'Histograma de datos aleatorios')



