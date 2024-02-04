package Kotlin

//Los comentarios en Kotlin se una linea se hacen con doble Slash

/*
Los comentarios largos de varias lineas
se hacen abriendo con slash *
y cerradn con * slash
*/

fun main() {
    println("¡Alola, Kotlin!") // Imprimir un mensaje

    // Tipos de datos, declaramos con Val para constante y Var para variables, despues su tipo de datos y se asigna el valor con =
    val NumeroB: Byte = 1                                                                            // Byte 8 bits, rango de -128 a 127
    val NumeroS: Short = 129                                                                         // Short 16 bits, rango de -32768 a 32767
    val NumeroI: Int = 40565                                                                         // Int 32 bits, rango de -2^31 a 2^31-1
    val NumeroL: Long = 19513219851                                                                  // Long  64 bits, rango de -2^63 a 2^63-1.
    val NumeroF: Float = 2.434F                                                                      // Float
    val NumeroD: Double = 81841459855846598.516148591                                                // Double 64 bits de precisión de punto flotante.
    val caracter: Char = 'K'                                                                         // Char Almacena 1 Caracter
    val cadena: String = "Cadena 3"                                                                  // String Almacena una cadena de caracteres
    val bool: Boolean = true                                                                         // Boolean
    val list: List<Any> = listOf(1, 2, 3, 'a', 'b')                                                  // Lista
    val tuple: Pair<Int, Any> = Pair(1, 'a')                                                         // Tupla
    val set: Set<Any> = setOf(1, 2, 23, NumeroI, 3, 3, 4, NumeroF, cadena, 'A', 'A', 'A', "cadena")  // Conjunto (No se repiten los valores)
    val dict: Map<String, Any> = mapOf(
        "Nombre" to "Bob Esponja",
        "Edad" to 25,
        "Cursos" to listOf("Calculo", "Algebra", "Inges")
    )                                                                                                // Diccionario
    val nulo: Nothing? = null                                                                        // Valor nulo

    // Para imprimir una variable dentro del string se puede hacer con $Variable
    println("Esto es un entero de 1 Byte: $NumeroB, Tipo: ${NumeroB::class.simpleName}")
    println("Esto es un entero Corto: $NumeroS, Tipo: ${NumeroS::class.simpleName}")
    println("Esto es un entero: $NumeroI, Tipo: ${NumeroI::class.simpleName}")
    println("Esto es un entero Largo: $NumeroL, Tipo: ${NumeroL::class.simpleName}")
    println("Esto es un Flotante: $NumeroF, Tipo: ${NumeroF::class.simpleName}")
    println("Esto es un Flotante Doble: $NumeroD, Tipo: ${NumeroD::class.simpleName}")
    println("Esto es un Char: $caracter, Tipo: ${caracter::class.simpleName}")
    println("Esto es un String: $cadena, Tipo: ${cadena::class.simpleName}")
    println("Esto es un Boleano: $bool, Tipo: ${bool::class.simpleName}")
    println("Esto es una lista: $list, Tipo: ${list::class.simpleName}")
    println("Esto es una tupla: $tuple, Tipo: ${tuple::class.simpleName}")
    println("Esto es un conjunto: $set, Tipo: ${set::class.simpleName}")
    println("Esto es un diccionario: $dict, Tipo: ${dict::class.simpleName}")
    println("Esto es un nulo: $nulo")

    // Otra forma de imprimir las variables junto con texto con concatenando con +
    println("La letra: " + caracter + " El numero: " + NumeroI + " El diccionario: " + dict)

    // Las variables y constantes de Koltin NO pueden cambiar de tipo (tipado estatico)
    // Para asignar cualquier dato a una variable se puede usar Any
    val cualquiera1: Any = 42.5F
    val cualquiera2: Any = "Noether"

    println("Es valor $cualquiera1 es un String: " + "${cualquiera1 is String}")
    println("Es valor $cualquiera1 es un Float: " + "${cualquiera1 is Float}")
    println(cualquiera2) // Imprimir una variable

    // Kotlin es Case Sensitive, diferencia mayusculas de minusculas
    val x = 23    // Variable Int Inferido
    val X = "73"  // Variable string Inferido

    println("esto es $x: Esto es X: " + X)
    println("x es de tipo: ${x::class.simpleName} X es de tipo ${X::class.simpleName}")

    // Operaciones Basicas
    println("Operaciones Bascias")
    var x1 = 14
    val y1 = 2.5
    println("14 + 2.5 = ${x1 + y1}") // Suma
    println("14 - 2.5 = ${x1 - y1}") // Resta
    println("14 * 2.5 = ${x1 * y1}") // Multiplicacion
    println("14 / 2.5 = ${x1 / y1}") // Division

    x1 = 25
    val y2 = 6
    println("25 % 6 = ${x1 % y2}") // Modulo

    // Operaciones Entre Variables
    println("Operaciones Entre tipos de variables")

    // Las operaciones aritméticas entre enteros devuelven un valor entero, incluso si el resultado podría tener una fracción.
    val resultado1: Int = 5 / 2
    println("5 / 2 = $resultado1 de tipo ${resultado1::class.simpleName}")

    // Las operaciones aritméticas entre decimales devuelven un valor decimal.
    val resultado2: Double = 5.0 / 2.0
    println("5.0 / 2.0 = $resultado2 de tipo ${resultado2::class.simpleName}")

    // Si mezclas enteros y decimales en una operación, el resultado será un decimal.
    val resultado3: Double = 5 / 2.0
    println("5 / 2.0 = $resultado3 de tipo ${resultado3::class.simpleName}")

    // Operaciones Logicas
    println("Operadores Lógicos")
    val op1 = 23
    val op2 = 57

    println("Es $op1 > $op2: ${op1 > op2} (Mayor estricto)")
    println("Es $op1 < $op2: ${op1 < op2} (Menor estricto)")
    println("Es $op1 >= 23: ${op1 >= 23} (Mayor o igual)")
    println("Es 44 <= $op2: ${44 <= op2} (Mayor o igual)")
    println("Es $op1 Igual a $op2: ${op1 == op2}") // Igual a
    println("Es $op2 Igual a 57: ${op2 == 57}")
    println("Es $op1 distinto a $op2: ${op1 != op2}") // Distinto a

    println("Algebra Booleana")
    val t = true
    val f = false
    val t2 = true

    println("Valor de t: $t")
    println("Valor de !t: ${!t}")
    println("Valor de t ∧ f: ${t && f}")
    println("Valor de t ∧ t2: ${t && t2}")
    println("Valor de t ∨ f: ${t || f}")

    // Cambio de tipo de variable (Type Cast)

    // Transformar a Int
    val numeroComoString = "123"                      // Variable de tipo String
    val numeroComoInt = numeroComoString.toInt()      // Convertir String a Int
    val numeroComoDouble = 123.55                     // Valor de tipo Double
    val DoubleComoInt = numeroComoDouble.toInt()      // Convertir Float a Int

    // Imprimir el resultado
    println("$numeroComoString" + " de Tipo ${numeroComoString::class.simpleName}")
    println("$numeroComoInt" + " de Tipo ${numeroComoInt::class.simpleName}")
    println("$numeroComoDouble" + " de Tipo ${numeroComoDouble::class.simpleName}")
    println("$DoubleComoInt" + " de Tipo ${DoubleComoInt::class.simpleName}")       // Se pierde la parte decimal
}
