# Ciclos

# Tipos While
x <- -3
while (x <= 10) {
  cat(paste("Valor de x = ", x, "\n"))
  x <- x + 1
}

y <- 0
while (TRUE) { # while infinito
  y <- y + 1
  if (y == 5) {
    cat("Se rompio el ciclo\n")
    break # Romper el ciclo
  } else {
    cat("Ciclo infinito\n")
  }
}

# Ciclos for
for (i in -3 : 7) { # Ciclo for imprime de 0 hasta n intervalor cerrado [-3, 7]
  cat(paste("Valor de i =", i, "\n"))
}

# Avanzar por una lista
lista <- c('a', 'c', 7, 3.1415, TRUE, 'lamda')
for (i in seq_along(lista)) {
  cat(paste("en elemento", i - 1, "de la lista es =", lista[i], "de tipo =", typeof(lista[i]), "\n"))
}

# Ciclos Anidados
numeros <- c(1, 2, 3)
letras <- c('a', 'b', 'c')

for (numero in numeros) {
  for (letra in letras) {
    print(paste(numero, letra))
  }
}

# Recorrer una matriz
matriz <- list(c(4, 7, 9, 3), c(2, 4, 6, 1))
print(paste("La matriz original:", matriz))

for (i in 1:length(matriz)) {
  print(paste("Valor", i, "es:", matriz[[i]]))
  for (j in 1:length(matriz[[i]])) {
    print(paste("Su valor", j, "es:", matriz[[i]][j]))
  }
}

