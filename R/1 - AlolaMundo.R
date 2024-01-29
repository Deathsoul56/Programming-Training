print("Alola Mundo R") #Imrpimier un mensaje, print en R solo recibe 1 argumento

#Los comentarios en R se una linea se hacen con el signo de gato #

"Los comentarios largos de varias lineas no existen en R
puede crear un string sin asignarlo a una variable
o con el comando Ctrl+Shift+C puede comentar las linas seleccionadas"

#Tipos de datos en R
#con el signo <- asignamos el valor a una variable que esta a la izquierda
#con el signo -> asignamos el valor a una variable que esta a la derecha
var1 <- 22
37 -> var1

x <- 23 # Numeric Tanto enteros
y <- 2.434 # Numeric como decimales
A <- "Cadena 3" # Character 
b <- TRUE # Logical para los boleanos
x1 <- as.integer(24) # Integer exclusivos para enterios
z <- 2 +3i # Complex para numeros complejos
f <- as.Date("2024-01-28") #Date para las fechas


#Cat es como print pero puede recibir varios argumentos
cat("Esto es un Numeric Entero:", x, class(x))
cat("Esto es un Numeric Decimal:", y, class(y))
cat("Esto es un Character:", A, class(A))
cat("Esto es un Logical:", b, class(b))
cat("Esto es un Integer:", x1, class(x1))
cat("Esto es un Complex:", z, class(z))
cat("Esto es un Date:", format(f, "%Y-%m-%d"), class(f))

