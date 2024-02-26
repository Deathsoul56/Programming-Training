# Si Condicional
x <- 13
  
if (x %% 2 == 0) {  # Si Condicion a cumplir
  cat("El numero", x, "es par") # Valor si es verdadero
} else { # En caso contrario
  cat("El numero", x, "es impar") # Calor si es falso
}

# Forma Alternativa
ifelse(x %% 2 == 0, paste(x, "es par"), paste(x, "es impar"))


# Mas de 1 condicion
if (x %% 3 == 0) {
  print(paste("El valor", x, "es equivalente a 0 en modulo 3"))
} else if (x %% 3 == 1) {
  print(paste("El valor", x, "es equivalente a 1 en modulo 3"))
} else {
  print(paste("El valor", x, "es equivalente a 2 en modulo 3"))
}


# If anidados
x <- 10
y <- 5

if (x > y) {
  print("x es mayor que y")
  if (x %% 2 == 0) {
    print("x es par")
  } else {
    print("x es impar")
  }
} else {
  print("x es menor o igual que y")
}

# If con operadores lógicos
x <- 10
y <- 5
z <- 15

if (x > y & x < z) {
  print("x es mayor que y pero menor que z")
} else if (x > y & x > z) {
  print("x es mayor que z e y")
} else if (x < y & x < z) {
  print("x es menor que z e y")
} else {
  print("ninguna condición se cumple")
}


# Condicion de Intentar
n1 <- 10
n2 <- 3

cat("La división entre", n1, "y", n2, "\n")

tryCatch({
  resultado <- n1 / n2
  if (resultado == as.integer(resultado)) {
    cat("La división da un número entero:", resultado, "\n")
  } else {
    cat("La división da un número decimal:", resultado, "\n")
  }
}, error = function(e) {
  cat("No se pueden dividir números por cero\n")
}, finally = {
  cat("Terminó la ejecución de la secuencia tryCatch\n")
})

