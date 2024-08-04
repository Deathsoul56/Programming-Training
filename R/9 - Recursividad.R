factorial <- function(n) {
  if (n == 0 || n == 1) {
    return(1)
  } else {
    return(n * factorial(n - 1))
  }
}

fibonacci <- function(n) {
  if (n == 1 || n == 2) {
    return(1)
  } else {
    return(fibonacci(n - 1) + fibonacci(n - 2))
  }
}

for (i in 0 : 10) {
  cat(paste(i, "! =", factorial(i), "\n"))
}

for (i in 1 : 30) {
  cat(paste("fibonacci_", i, "=", fibonacci(i), "\n"))
}
