package Kotlin


fun main() {
    var x = 13

    // Si condicional
    if (x % 2 == 0) {                           // Si Condicion a cumplir
        println("El numero $x es par")          // Valor si es verdadero
    } else {                                    // En caso contrario
        println("El numero $x es impar")        // Calor si es falso
    }

    // Forma alternativa
    println(if (x % 2 == 0) "$x es par" else "$x es impar")

    // Mas de 1 condicion
    when {
        x % 3 == 0 -> println("El valor $x es equivalente a 0 en modulo 3")  // Si condicion a cumplir
        x % 3 == 1 -> println("El valor $x es equivalente a 1 en modulo 3")  // Pero si segunda condicion
        else -> println("El valor $x es equivalente a 2 en modulo 3")        // En caso contrario
    }

    x = 10
    val y = 5
    val z = 15

    // If anidados
    if (x > y) {
        println("x es mayor que y")
        if (x % 2 == 0) {
            println("x es par")
        } else {
            println("x es impar")
        }
    } else {
        println("x es menor o igual que y")
    }

    // If con operadores logicos
    if (x > y && x < z) {
        println("x es mayor que y pero menor que z")
    } else if (x > y && x > z) {
        println("x es mayor que z e y")
    } else if (x < y && x < z) {
        println("x es menor que z e y")
    } else {
        println("ninguna condición se cumple")
    }

    val n1 = 10
    val n2 = 3

    println("La división entre $n1 y $n2")

    try {
        val resultado = n1.toDouble() / n2.toDouble()
        if (resultado == resultado.toInt().toDouble()) {
            println("La división da un número entero $resultado")
        } else {
            println("La división da un número decimal $resultado")
        }
    } catch (e: ArithmeticException) {
        println("No se pueden dividir números por cero")
    } finally {
        println("Terminó la ejecución del bloque Try")
    }
}