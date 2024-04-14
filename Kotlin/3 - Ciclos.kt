package Kotlin

fun main() {
    // Ciclo While
    var x = -3
    while (x <= 10) {
        println("Valor de x = $x")
        x++
    }

    var y = 0
    while (true) {
        y++
        if (y == 5) {
            println("Se rompio el ciclo")
            break
        } else {
            println("Ciclo infinito")
        }
    }

    // Ciclo For
    for (i in 0..5) {
        println("Valor de i = $i")
    }

    for (j in -5 until 7) {
        println("Valor de j = $j")
    }

    // Avanzar por una lista
    val lista = listOf('a', 'c', 7, 3.1415, true, "lambda")
    for ((index, valor) in lista.withIndex()) {
        println("En el elemento $index de la lista es = $valor de tipo = ${valor::class.simpleName}")
    }

    // Ciclos Anidados
    val numeros = listOf(1, 2, 3)
    val letras = listOf('a', 'b', 'c')

    for (numero in numeros) {
        for (letra in letras) {
            println("$numero $letra")
        }
    }

    // Recorrer una matriz
    val matriz = arrayOf(intArrayOf(4, 7, 9, 3), intArrayOf(2, 4, 6, 1))
    println("La matriz original: ${matriz.contentDeepToString()}")
    for ((index, array) in matriz.withIndex()) {
        println("Valor $index es: ${array.contentToString()}")
        for (element in array) {
            println("Su valor es: $element")
        }
    }
}
