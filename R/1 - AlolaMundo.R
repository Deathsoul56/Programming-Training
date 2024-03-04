print("Alola Mundo R") # Imprimir  un mensaje, print en R solo recibe 1 argumento

# Los comentarios en R de una línea se hacen con el signo de gato #

"Los comentarios largos de varias líneas no existen en R
puede crear un string sin asignarlo a una variable
o con el comando Ctrl+Shift+C puede comentar las líneas seleccionadas en R-Studio"

# Tipos de datos en R
# con el signo <- asignamos el valor a una variable que está a la izquierda
# con el signo -> asignamos el valor a una variable que está a la derecha
var1 <- 22
37 -> var1

x <- 23 # Numeric Tanto enteros
y <- 2.434 # Numeric como decimales
z <- 2 +3i # Complex para números complejos
A <- "Cadena 3" # Character 
b <- TRUE # Logical para los booleanos
f <- as.Date("2024-01-28") # Date para las fechas
v <- c(5, 23, 73, 21, 3.14) # Vector
lista <- list(1, "dos", 3, "cuatro", 5) # Array para arreglos
infinito <- Inf # Infinito
infinitom <- -Inf # Infinito Negativo
Nonumero <- NaN

# Cat es como print pero puede recibir varios argumentos
cat("Esto es un Numeric Entero:", x, class(x), typeof(x))
cat("Esto es un Numeric Decimal:", y, class(y), typeof(y))
cat("Esto es un Complex:", z, class(z), typeof(z))
cat("Esto es un Character:", A, class(A), typeof(A))
cat("Esto es un Logical:", b, class(b), typeof(b))
cat("Esto es un Vector:", v, class(v), typeof(v))
cat("Esto es un Date:", format(f, "%Y-%m-%d"), class(f), typeof(f))
cat("Esto es un Array:", paste(lista, collapse = ", "), class(lista), typeof(lista))
cat("Esto es un Numeric Entero:", infinito, class(infinito), typeof(infinito))
cat("Esto es un Numeric Entero:", Nonumero, class(Nonumero), typeof(Nonumero))

# En R un valor individual se puede imprimir simplemente escribiéndolo
x

# Una variable puede cambiar de tipo (tipado dinámico)
A <- 2.27
cat(A, typeof(A))

# Función para saber si una variable pertenece a cierto tipo
A <- 2.27
cat("A es un floar", class(A) == "numeric")
cat("A es un String", class(A) == "character")

# R es Case Sensitive, diferencia mayúsculas de minúsculas
X <- "73"  # Variable tipo string
cat("esto es x:", x, "Esto es X:", X, "\n")

# Forma alternativa para imprimir y/o insertar un valor numérico dentro de un string
nombre <- 'Bob Esponja'
Edad <- 25
cat("El alumno", nombre, "tiene", Edad, "años")
cat(sprintf("El alumno %s tiene %d años\n", nombre, Edad))

# En R existe una funciï¿½n para concatenar valores
valor1 <- "Alola"
valor2 <- "mundo"
valorc <- paste(valor1, valor2)
valorc  # Salida: "Hola mundo"
valorc <- paste(valor1, valor2, sep = "-")
valorc  # Salida: "Hola-mundo"
valorc <- paste(valor1, valor2, sep = "")
valorc  # Salida: "Holamundo"

# Operaciones Básicas
# Suma
x + y
10 + 3

# Resta
x - y
10 - 3

# Multiplicación
x * y
10 * 3

# División
x / y
10 / 3

# División Entera
x %/% y
10 %/% 3

# Modulo
x %% y
10 %% 3

# Operaciones de Comparación
Op1 <- 23
Op2 <- 57

cat("Operadores de Comparaciï¿½n\n")
cat(sprintf("Es %d > %d: %s Mayor estricto\n", Op1, Op2, Op1 > Op2))
cat(sprintf("Es %d < %d: %s Menor estricto\n", Op1, Op2, Op1 < Op2))
cat(sprintf("Es %d >= 23: %s Mayor o igual\n", Op1, Op1 >= 23))
cat(sprintf("Es 44 <= %d: %s Mayor o igual\n", Op2, 44 <= Op2))
cat(sprintf("Es %d == %d: %s igual a\n", Op1, Op2, Op1 == Op2))
cat(sprintf("Es %d == 57: %s\n", Op2, Op2 == 57))
cat(sprintf("Es %d != %d: %s Distinto a\n", Op1, Op2, Op1 != Op2))
cat(sprintf("Es %d es entero: %s\n", Op1, class(Op1) == "integer"))
cat(sprintf("Es %d no es entero: %s\n", Op1, class(Op1) != "integer"))

# Algebra Booleana
t <- TRUE
f <- FALSE
t2 <- TRUE

cat("Operaciones Lógicas\n")
cat("Valor de t:", t, "\n")
cat("Valor de !t:", !t, "\n")            # Negación Lógica (!)
cat("Valor de t & f:", t & f, "\n")      # Conjunción Lógica (y)
cat("Valor de t & t2:", t & t2, "\n")
cat("Valor de t | f:", t | f, "\n")      # Disyunción Lógica (o)

# Cambio de tipo de variable (Type Cast)
# Transformar una variable a Int
cat("Transformar a Int\n")
cat("La variable era:", X, "y su tipo:", class(X), "\n")
X <- as.integer(X)
cat("La variable es:", X, "y su tipo:", class(X), "\n")  # Cuando se aplica a un número que estaba como string se conserva

cat("La variable era:", y, "y su tipo:", class(y), "\n")
cat("La variable es:", as.integer(y), "y su tipo:", class(as.integer(y)), "\n") # Cuando se aplica a un float solo se toma la parte entera

# Transformar a String
cat("Transformar a String\n")
cat("La variable es:", y, "y su tipo:", class(y), "\n")
y <- as.character(y)
cat("La variable es:", y, "y su tipo:", class(y), "\n")

# Transformar a Float
cat("Transformar a Float\n")
cat("La variable es:", X, "y su tipo:", class(X), "\n")
X <- as.double(X)
cat("La variable es:", X, "y su tipo:", class(X), "\n")

# Ingresar un valor de forma manual
valor <- readline("Ingrese su valor aquï¿½: ")
cat(sprintf("El valor es: %s y es de tipo %s\n", valor, class(valor)))

# Funciones para string
mi_string <- 'cazuEla'
cat(nchar(mi_string), "Largo de mi string\n") # Longitud del string
cat(regexpr('z', mi_string)[1], "Posiciï¿½n de la z en mi string\n") # Encontrar posición de un substring
cat(toupper(substr(mi_string, 1, 1)), substr(mi_string, 2, nchar(mi_string)), "\n") # Capitalizar la primera letra
cat(toupper(mi_string), "\n") # Convertir a mayúsculas
cat(tolower(mi_string), "\n") # Convertir a minúsculas
cat(grepl("^[0-9]+$", mi_string), "Devuelve verdadero si es un número\n") # Verificar si es un nï¿½mero
cat(grepl("^[A-Za-z]+$", mi_string), "Devuelve verdadero si solo contiene letras\n") # Verificar si solo contiene letras
cat(grepl("^[A-Za-z0-9]+$", mi_string), "Devuelve verdadero si solo contiene letras y números\n") # Verificar si solo contiene letras y números
cat(length(gregexpr('a', mi_string)[[1]]), "Cuenta todas las a que contiene\n") # Contar ocurrencias de un substring
cat(gsub('z', 'ss', mi_string), "Reemplaza todas las z por ss\n") # Reemplazar un substring
cat(rep(mi_string, 3), "Se imprime el string 3 veces\n") # Repetir el string

linea1 <- " **********************"
linea2 <- "*                    *"
linea3 <- "*       Adios!       *"

cat(linea1, "\n", linea2, "\n", linea3, "\n", linea2, "\n", rep("*", 12))

