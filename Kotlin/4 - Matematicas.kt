package Kotlin

import kotlin.math.*

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
    val x = 24.0
    val y = 17.4

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

    // Funciones matematicas
    println("e^2 = ${exp(2.0)}")                     // Función exponencial
    println("Ln($x) = ${ln(x)}")                    // Logaritmo Natural
    println("Log_7($x) = ${log(x, 7.0)}")           // Logaritmo cualquier base (argumento, base)
    println("floor($y) = ${floor(y)}")              // Función Piso
    println("Ceil($y) = ${ceil(y)}")                // Función Techo
    println("√(5^2+12^2) = ${hypot(5.0, 12.0)}")    // Hipotenusa

    // Funciones Trigonométricas (Por defecto están en Radianes)
    println("sin(π/6) = ${sin(pi / 6)}")       // Función Seno
    println("cos(π/6) = ${cos(pi / 6)}")       // Función Coseno
    println("tg(π/6) = ${tan(pi / 6)}")        // Función Tangente
    println("sec(π/6) = ${1 / cos(pi / 6)}")   // Función Secante
    println("csc(π/6) = ${1 / sin(pi / 6)}")   // Función Cosecante
    println("cotg(π/6) = ${1 / tan(pi / 6)}")  // Función Cotangente

    // Funciones Trigonométricas Inversas
    println("Arcosen(1/2) = ${asin(1.0 / 2.0)}")    // Arcoseno
    println("Arcocosen(1/2) = ${acos(1.0 / 2.0)}")  // Arcocoseno
    println("Arcotg(1/2) = ${atan(1.0 / 2.0)}")     // Arcotangente


    // Cambios de Angulos
    val degrees = 180.0
    val radians = PI / 4

    println("180° en radianes es: ${Math.toRadians(degrees)}") // Conversión de grados a radianes
    println("π/4 en grados es: ${Math.toDegrees(radians)}") // Conversión de radianes a grados

    // Funciones Hiperbólicas
    println("sinh(3) = ${sinh(x)}")           // Función Seno Hiperbólico
    println("cosh(3) = ${cosh(x)}")           // Función Coseno Hiperbólico
    println("tanh(3) = ${tanh(x)}")           // Función Tangente Hiperbólico
    println("sech(3) = ${1 / cosh(x)}")       // Función Secante Hiperbólico
    println("csch(3) = ${1 / sinh(x)}")       // Función Cosecante Hiperbólico
    println("cotanh(3) = ${1 / tanh(x)}")     // Función Cotangente Hiperbólico

    // Funciones Hiperbólicas Inversas
    println("Arcosinh(5) = ${asinh(5.0)}")        // Función ArcoSeno Hiperbólico
    println("Arcocosh(5) = ${acosh(5.0)}")        // Función ArcoCoseno Hiperbólico
    println("Arcotanh(1/2) = ${atanh(1.0/2.0)}")  // Función ArcoTangente Hiperbólico

    // Funciones inversas restante
    /*
    θ = arcsec(x)
    sec(θ) = x
    1 / cos(θ) = x
    cos(θ) = 1 / x
    θ = arccos(1/x)
    */

    // Funciones Trigonométricas Inversas Adicionales
    println("Arcsec(5) = ${acos(1.0 / 5)}")             // Función ArcoSecante
    println("Arccsc(5) = ${asin(1.0 / 5)}")             // Función ArcoCosecante
    println("Arccotg(5) = ${atan(1.0 / 5)}")            // Función ArcoCotangente
    println("Arcsech(1/2) = ${acosh(1.0 / (1.0/2.0))}") // Función ArcoSecante Hiperbólico
    println("Arccsch(5) = ${asinh(1.0 / 5)}")           // Función ArcoCosecante Hiperbólico
    println("Arccotanh(5) = ${atanh(1.0 / 5)}")         // Función ArcoCotangente Hiperbólico
}
