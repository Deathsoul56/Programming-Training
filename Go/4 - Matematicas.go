//go:build ignore

/*
CLASE 4: MATEMÁTICAS EN GO

Esta clase cubre las operaciones y funciones matemáticas en Go:
1. Números Especiales (Pi, E, Infinito, NaN)
2. Operaciones Aritméticas (Básicas, complejas, potencias, etc.)
3. Funciones Matemáticas (Exponenciales, Logaritmos, redondeos)
4. Funciones Trigonométricas (Sen, Cos, Tan y sus recíprocas)
5. Funciones Trigonométricas Inversas y Transformación de Ángulos
6. Funciones Hiperbólicas y sus Inversas (Seno hiperbólico, etc.)
*/

package main

import (
	"fmt"
	"math"
	"math/cmplx"
	"strings"
)

func main() {

	fmt.Println("=== CLASE 4: MATEMÁTICAS EN GO ===")

	// =============================================================================
	// 1. CONSTANTES Y NÚMEROS ESPECIALES
	// =============================================================================

	fmt.Println("1. CONSTANTES Y NÚMEROS ESPECIALES")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Numeros especiales (Paquete math) ---")
	Pi := math.Pi          // Valor de pi 3.141592653589793
	e := math.E            // Valor de e 2.718281828459045
	inf := math.Inf(1)     // Infinito Positivo
	minf := math.Inf(-1)   // Infinito Negativo
	noNumero := math.NaN() // No es un numero (Not a number)

	fmt.Printf("Valor de Pi: %v\n", Pi)
	fmt.Printf("Valor de e: %v\n", e)
	fmt.Printf("Infinito positivo: %v\n", inf)
	fmt.Printf("Infinito negativo: %v\n", minf)
	fmt.Printf("No es un número (NaN): %v\n", noNumero)

	// =============================================================================
	// 2. OPERACIONES ARITMÉTICAS BÁSICAS Y COMPLEJAS
	// =============================================================================

	fmt.Println("\n2. OPERACIONES ARITMÉTICAS BÁSICAS Y COMPLEJAS")
	fmt.Println(strings.Repeat("=", 40))

	// Definir algunos valores
	x := 24.0
	y := 17.4
	z := complex(3, 4)

	fmt.Println("\n--- Operaciones Aritmeticas Elementales ---")
	fmt.Printf("Valores base -> x: %v, y: %v, z: %v\n\n", x, y, z)
	fmt.Printf("Suma: %v + %v = %v\n", x, y, x+y)              // Suma
	fmt.Printf("Resta: %v - %v = %v\n", x, y, x-y)             // Resta
	fmt.Printf("Multiplicación: %v * %v = %v\n", x, y, x*y)    // Multiplicación
	fmt.Printf("División: %v / %v = %v\n", x, y, x/y)          // División
	fmt.Printf("División entera: %v // 9 = %v\n", x, int(x)/9) // División entera
	fmt.Printf("Módulo: %v %% 9 = %v\n", x, int(x)%9)          // Módulo

	fmt.Println("\n--- Raíces, Potencias y Absoluto ---")
	fmt.Printf("Raíz cuadrada: √%v = %v\n", x, math.Sqrt(float64(x)))    // Raíz cuadrada
	fmt.Printf("Potencia: %v^3 = %v\n", x, int(math.Pow(float64(x), 3))) // Potencia
	fmt.Printf("Valor absoluto: |-%v| = %v\n", y, math.Abs(-y))          // Valor absoluto

	fmt.Println("\n--- Operaciones con Números Complejos ---")
	fmt.Printf("Parte Real: Re(%v) = %v\n", z, real(z))               // Parte Real
	fmt.Printf("Parte Imaginaria: Im(%v) = %v\n", z, imag(z))         // Parte Imaginaria
	fmt.Printf("Modulo (Magnitud): |%v| = %v\n", z, cmplx.Abs(z))     // Modulo Numero complejo
	fmt.Printf("Argumento (Fase): Arg(%v) = %v\n", z, cmplx.Phase(z)) // Argumento de un complejo
	fmt.Printf("Conjugado: %v* = %v\n", z, cmplx.Conj(z))             // Conjugado

	// =============================================================================
	// 3. FUNCIONES MATEMÁTICAS AVANZADAS
	// =============================================================================

	fmt.Println("\n3. FUNCIONES MATEMÁTICAS AVANZADAS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Exponenciales y Logaritmos ---")
	fmt.Printf("e^2 = %v\n", math.Exp(2))       // Funciones Exponenciales
	fmt.Printf("Ln(%v) = %v\n", x, math.Log(x)) // Logaritmo Natural
	base := 7.0
	// Go no tiene Log con base X nativo, se usa cambio de base ln(x)/ln(base)
	fmt.Printf("Log_%v(%v) = %v\n", base, x, math.Log(x)/math.Log(base)) // Logaritmo cualquier base

	fmt.Println("\n--- Redondeos y Geometría Básica ---")
	fmt.Printf("Función Piso: floor(%v) = %v\n", y, math.Floor(y))                         // Función Piso
	fmt.Printf("Función Cielo: Ceil(%v) = %v\n", y, math.Ceil(y))                          // Función Cielo
	fmt.Printf("Teorema de Pitágoras: √(5^2+12^2) = %v (Hipotenusa)\n", math.Hypot(5, 12)) // Hipotenusa

	// =============================================================================
	// 4. FUNCIONES TRIGONOMÉTRICAS
	// =============================================================================

	fmt.Println("\n4. FUNCIONES TRIGONOMÉTRICAS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Funciones Principales ---")
	fmt.Printf("Seno: sin(π/6) = %v\n", math.Sin(Pi/6))    // Funcion Seno
	fmt.Printf("Coseno: cos(π/6) = %v\n", math.Cos(Pi/6))  // Funcion Coseno
	fmt.Printf("Tangente: tg(π/6) = %v\n", math.Tan(Pi/6)) // Funcion Tangente

	fmt.Println("\n--- Funciones Recíprocas ---")
	secante := 1 / math.Cos(Pi/6)
	fmt.Printf("Secante: sec(π/6) = %v\n", secante) // Funcion Secante

	cosecante := 1 / math.Sin(Pi/6)
	fmt.Printf("Cosecante: csc(π/6) = %v\n", cosecante) // Funcion Cosecante

	cotangente := 1 / math.Tan(Pi/6)
	fmt.Printf("Cotangente: cotg(π/6) = %v\n", cotangente) // Funcion Cotangente

	// =============================================================================
	// 5. TRIGONOMETRÍA INVERSA Y TRANSFORMACIONES
	// =============================================================================

	fmt.Println("\n5. TRIGONOMETRÍA INVERSA Y TRANSFORMACIONES")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Funciones Trigonometricas Inversas ---")
	// Se multiplica por 180 / Pi para pasarlo a grados
	fmt.Printf("Arcoseno: Arcosen(1/2) = %v grados\n", math.Asin(1.0/2)*180/Pi)     // Arcoseno
	fmt.Printf("Arcocoseno: Arcocosen(1/2) = %v grados\n", math.Acos(1.0/2)*180/Pi) // Arcocoseno
	fmt.Printf("Arcotangente: Arcotg(1) = %v grados\n", math.Atan(1.0)*180/Pi)      // Arcotangente

	fmt.Println("\n--- Transformaciones de Ángulos ---")
	fmt.Printf("180° en radianes es: %v\n", math.Pi)    // 180 grados en radianes
	fmt.Printf("π/4 en grados es: %v\n", (Pi/4)*180/Pi) // π/4 en grados

	// =============================================================================
	// 6. FUNCIONES HIPERBÓLICAS Y SUS INVERSAS
	// =============================================================================

	fmt.Println("\n6. FUNCIONES HIPERBÓLICAS Y SUS INVERSAS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Funciones Hiperbolicas ---")
	fmt.Printf("sinh(3) = %f\n", math.Sinh(3))       // Función Seno Hiperbólico
	fmt.Printf("cosh(3) = %f\n", math.Cosh(3))       // Función Coseno Hiperbólico
	fmt.Printf("tanh(3) = %f\n", math.Tanh(3))       // Función Tangente Hiperbólica
	fmt.Printf("sech(3) = %f\n", 1.0/math.Cosh(3))   // Función Secante Hiperbólica
	fmt.Printf("csch(3) = %f\n", 1.0/math.Sinh(3))   // Función Cosecante Hiperbólica
	fmt.Printf("cotanh(3) = %f\n", 1.0/math.Tanh(3)) // Función Cotangente Hiperbólica

	fmt.Println("\n--- Funciones Hiperbolicas Inversas ---")
	fmt.Printf("Arcosinh(5) = %f\n", math.Asinh(5))     // Función ArcoSeno Hiperbólico
	fmt.Printf("Arcocosh(5) = %f\n", math.Acosh(5))     // Función ArcoCoseno Hiperbólico
	fmt.Printf("Arcotanh(1/2) = %f\n", math.Atanh(0.5)) // Función ArcoTangente Hiperbólico

	fmt.Println("\n--- Funciones Inversas Restantes Derivadas ---")
	/*
	   Demostración matemática auxiliar para las inversas:
	   θ = arcsec(x)
	   sec(θ) = x
	   1 / cos(θ) = x
	   cos(θ) = 1 / x
	   θ = arccos(1/x)
	*/
	fmt.Printf("Arcsec(5) = %f\n", math.Acos(1.0/5))         // Función ArcoSecante
	fmt.Printf("Arccsc(5) = %f\n", math.Asin(1.0/5))         // Función ArcoCosecante
	fmt.Printf("Arccotg(5) = %f\n", math.Atan(1.0/5))        // Función ArcoCotangente
	fmt.Printf("Arcsech(1/2) = %f\n", math.Acosh(1/(1.0/2))) // Función ArcoSecante Hiperbólico
	fmt.Printf("Arccsch(5) = %f\n", math.Asinh(1.0/5))       // Función ArcoCosecante Hiperbólico
	fmt.Printf("Arccotanh(5) = %f\n", math.Atanh(1.0/5))     // Función ArcoCotangente Hiperbólico

	// =============================================================================
	// CONCLUSIONES
	// =============================================================================

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("CONCLUSIONES SOBRE MATEMÁTICAS EN GO")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Println("\n1. IMPORTANCIA DEL PAQUETE MATH Y CMPLX:")
	fmt.Println("   • El paquete `math` provee de casi el 100% de la funcionalidad de cálculo de Go, trabajando por defecto con `float64`.")
	fmt.Println("   • Para complejos se requiere obligatoriamente importar de manera separada el paquete `math/cmplx` para manejar magnitudes, fases y escalares.")

	fmt.Println("\n2. HOMOLOGACIÓN DE FORMULAS:")
	fmt.Println("   • A la hora de programar recíprocas ausentes por defecto en librerías estándar (como la sec, csc y cotg) conviene saber su derivación directa con fracciones, tal cual se demostró al final de archivo para construir Arcsec.")

	fmt.Println("\n=== FIN DE LA CLASE 4 ===")

}
