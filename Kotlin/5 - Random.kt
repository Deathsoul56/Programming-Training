package Kotlin
import kotlin.random.Random

fun main() {


    // Números Pseudo-Aleatorios
    val aleatorio = Random.nextDouble() // Número aleatorio entre 0 y 1
    println("Número aleatorio entre 0 y 1: $aleatorio")

    val aleatorio2 = Random.nextInt(-10, 11) // Número aleatorio entre -10 y 10, el intervalo es cerrado-abierto [)
    println("Número aleatorio: $aleatorio2")

    val aleatorio3 = IntArray(10) { Random.nextInt(-10, 11) } // Vector 10 números aleatorios
    println("Vector aleatorio: ${aleatorio3.contentToString()}")

    val aleatorio4 = DoubleArray(5) { Random.nextDouble() } // Muestra de 5 valores aleatorios
    println("Muestra aleatorio: ${aleatorio4.contentToString()}")

    val aleatorio5 = ByteArray(12) { Random.nextBytes(1)[0] } // Bytes aleatorios
    println("Bytes Aleatorios: ${aleatorio5.contentToString()}")

    val aleatorio6 = Array(4) { IntArray(3) { Random.nextInt(-10, 11) } } // Matriz 4x3 aleatorios
    println("Matriz aleatorio: ${aleatorio6.contentDeepToString()}")

    val aleatorio7 = Array(2) { DoubleArray(2) { Random.nextDouble() } } // Genera una matriz de 2x2 con números aleatorios entre 0 y 1.
    println("Matriz aleatorio entre 0 y 1: ${aleatorio7.contentDeepToString()}")

    val vector = intArrayOf(7, -4, -3, 7, 9, 7, 0, -5, 3, 3)
    val v = vector.random()
    println("El vector $vector se escoge al azar un valor $v")

    // Permutaciones
    val lista = arrayOf("rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro")
    println("Lista Original = ${lista.contentToString()}")
    lista.shuffle() // Función para revolver un array
    println("Lista revuelta = ${lista.contentToString()}")

}