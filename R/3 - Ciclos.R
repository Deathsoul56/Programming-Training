cat("\n--- Ciclo While ---")
# Tipo While
x <- -3 
while (x <= 10) { # Ciclo while que imprime valores de x desde -3 hasta 10
    cat(sprintf("Valor de x = %d\n", x))
    x <- x + 1
}

y <- 0
while (TRUE) { # while infinito
    y <- y + 1
    if (y == 5) {
        cat("Se rompió el ciclo\n")
        break # Romper el ciclo
    } else {
        cat("Ciclo infinito\n")
    }
}

cat("\n--- Ciclo For ---")
# Ciclos for

# Avanzar por un rango
for (i in 0:5) { # Ciclo for imprime de 0 hasta n
    cat(sprintf("Valor de i = %02d\n", i))  # Formatea el número con dos dígitos
}

for (j in -5:6) { # Imprime de -5 hasta 6
    cat(sprintf("Valor de j = %d\n", j))
}

# Avanzar por una lista
mi_lista <- list('a', 'c', 7, 3.1415, TRUE, 'lambda')
for (i in seq_along(mi_lista)) {
    cat(sprintf("El elemento %d de la lista es = %s de tipo = %s\n", 
                i, mi_lista[[i]], typeof(mi_lista[[i]])))
}

# Verificar múltiples valores en una lista
numeros <- c(10, 15, 20, 25, 30)
for (num in numeros) {
    if (num %% 2 == 0) {
        cat(sprintf("%d es par\n", num))
    } else {
        cat(sprintf("%d es impar\n", num))
    }
}

# ciclos con next (equivalente a continue en Python)
for (i in 0:9) {
    if (i %% 2 == 0) {
        next  # Saltar números pares
    }
    cat(sprintf("Número impar: %d\n", i))
}

# Ciclos con manejo de errores
for (i in -1:4) {
    tryCatch({
        cat(sprintf("10 / %d: %f\n", i, 10/i))
    }, error = function(e) {
        cat(sprintf("Error: No se puede dividir 10 entre %d (división por cero).\n", i))
    })
}

cat("\n--- Ciclos Anidados ---")
# Ciclos Anidados
numeros <- 1:3
letras <- c('a', 'b', 'c')

for (numero in numeros) {
    for (letra in letras) {
        cat(numero, letra, "\n")
    }
}

# En R podemos usar mapply como alternativa a zip
mapply(function(n, l) cat(n, l, "\n"), numeros, letras)

# Recorrer una matriz
matriz <- matrix(c(4, 7, 9, 3, 2, 4, 6, 1), nrow = 2, byrow = TRUE)
cat(sprintf("La matriz original:\n"))
print(matriz)

# Manera básica
for (i in 1:nrow(matriz)) {
    cat(sprintf("Fila %d: %s\n", i-1, paste(matriz[i,], collapse = " ")))
    for (j in 1:ncol(matriz)) {
        cat(sprintf("  Columna %d: %d\n", j-1, matriz[i,j]))
    }
}

# De manera más R-ística usando apply
cat("\nUsando apply (más idiomático en R):\n")
apply(matriz, 1, function(fila) {
    cat(sprintf("Fila: %s\n", paste(fila, collapse = " ")))
})