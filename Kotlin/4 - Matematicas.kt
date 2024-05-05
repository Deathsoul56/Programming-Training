package Kotlin

import kotlin.math.*
class Complex(internal var real: Double, internal var imag: Double)

fun main() {
    val pi = Math.PI         // Valor de pi 3.141592653589793
    val e = Math.E           // Valor de e 2.718281828459045
    val inf = Double.POSITIVE_INFINITY   // Infinito Positivo
    val minf = Double.NEGATIVE_INFINITY  // Infinito Negativo
    val noNumero = Double.NaN            // No es un número (Not a number)
    println("Valor de Pi: $pi, Valor de e: $e")
    println("Infinito positivo: $inf, infinito negativo: $minf")
    println("No es un número: $noNumero")

    // Definir algunos valores
    val x = 24
    val y = 17.4
    val z = Complex(3.0, 4.0)

            // Operaciones
            println("$x + $y = ${x + y}")          // Suma
    println("$x - $y = ${x - y}")          // Resta
    println("$x * $y = ${x * y}")          // Multiplicación
    println("$x / $y = ${x / y}")          // División
    println("$x div 9 = ${x / 9}")         // División entera
    println("$x % 9 = ${x % 9}")           // Módulo
    println("√$x = ${sqrt(x.toDouble())}") // Raíz Cuadrada
    println("$x^3 = ${x.toDouble().pow(3)}") // Potencia
    println("$x^3 = ${x.toDouble().pow(3)}") // Potencia con Kotlin
    println("3√$x = ${x.toDouble().pow(1.0/3.0)}") // Raíz N-ésima con Kotlin
    println("|-$y| = ${y.absoluteValue}") // Valor absoluto
    println("Re($z) = ${z.real}")         // Parte Real
    /*
    println("Im($z) = ${z.imaginary}")    // Parte Imaginaria
    println("|$z| = ${z.absoluteValue}")  // Módulo Número complejo
    println("Arg($z) = ${z.arg}")         // Argumento de un complejo
    println("$z* = ${z.conjugate}")       // Conjugado

     */
}
