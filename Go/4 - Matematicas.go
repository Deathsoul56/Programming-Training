//go:build ignore
// +build ignore

package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

func main() {

	// Constantes especiales
	Pi := math.Pi          // Valor de pi 3.141592653589793
	e := math.E            // Valor de e 2.718281828459045
	inf := math.Inf(1)     // Infinito Positivo
	minf := math.Inf(-1)   // Infinito Negativo
	noNumero := math.NaN() // No es un numero (Not a number)

	fmt.Printf("Valor de Pi: %v, Valor de e: %v\n", Pi, e)
	fmt.Printf("Infinito positivo: %v, infinito negativo: %v\n", inf, minf)
	fmt.Printf("No es un número: %v\n", noNumero)

	// Definir algunos valores
	x := 24.0
	y := 17.4
	z := complex(3, 4)

	fmt.Printf("x: %v, y: %v, z: %v\n", x, y, z)
	fmt.Printf("%v + %v = %v\n", x, y, x+y)                    // Suma
	fmt.Printf("%v - %v = %v\n", x, y, x-y)                    // Resta
	fmt.Printf("%v * %v = %v\n", x, y, x*y)                    // Multiplicación
	fmt.Printf("%v / %v = %v\n", x, y, x/y)                    // División
	fmt.Printf("%v // 9 = %v\n", x, int(x)/9)                  // División entera
	fmt.Printf("%v %% 9 = %v\n", x, int(x)%9)                  // Módulo
	fmt.Printf("√%v = %v\n", x, math.Sqrt(float64(x)))         // Raíz cuadrada
	fmt.Printf("%v^3 = %v\n", x, int(math.Pow(float64(x), 3))) // Potencia
	fmt.Printf("|-%v| = %v\n", y, math.Abs(-y))                // Valor absoluto
	fmt.Printf("Re(%v) = %v\n", z, real(z))                    // Parte Real
	fmt.Printf("Im(%v) = %v\n", z, imag(z))                    // Parte Imaginaria
	fmt.Printf("|%v| = %v\n", z, cmplx.Abs(z))                 // Modulo Numero complejo
	fmt.Printf("Arg(%v) = %v\n", z, cmplx.Phase(z))            // Argumento de un complejo
	fmt.Printf("%v* = %v\n", z, cmplx.Conj(z))                 // Conjugado

	// Funciones matematicas
	fmt.Printf("e^2 = %v\n", math.Exp(2))            // Funciones Exponenciales
	fmt.Printf("Ln(%v) = %v\n", x, math.Log(x))      // Logaritmo Natural
	fmt.Printf("floor(%v) = %v\n", y, math.Floor(y)) // Función Piso
	fmt.Printf("Ceil(%v) = %v\n", y, math.Ceil(y))   // Función Cielo

	// Funciones Trigonometricas (Por defecto estan en Radianes)
	fmt.Printf("sin(π/6) = %v\n", math.Sin(Pi/6)) // Funcion Seno
	fmt.Printf("cos(π/6) = %v\n", math.Cos(Pi/6)) // Funcion Coseno
	fmt.Printf("tg(π/6) = %v\n", math.Tan(Pi/6))  // Funcion Tangente

	secante := 1 / math.Cos(Pi/6)
	fmt.Printf("sec(π/6) = %v\n", secante) // Funcion Secante

	cosecante := 1 / math.Sin(Pi/6)
	fmt.Printf("csc(π/6) = %v\n", cosecante) // Funcion Cosecante

	cotangente := 1 / math.Tan(Pi/6)
	fmt.Printf("cotg(π/6) = %v\n", cotangente) // Funcion Cotangente

	// Funciones Trigonometricas Inversas
	fmt.Printf("Arcosen(1/2) = %v\n", math.Asin(1.0/2))   // Arcoseno
	fmt.Printf("Arcocosen(1/2) = %v\n", math.Acos(1.0/2)) // Arcocoseno
	fmt.Printf("Arcotg(1/2) = %v\n", math.Atan(1.0/2))    // Arcotangente

	// Funciones Hiporbolicas
	fmt.Printf("sinh(3) = %f\n", math.Sinh(3))       // Función Seno Hiperbólico
	fmt.Printf("cosh(3) = %f\n", math.Cosh(3))       // Función Coseno Hiperbólico
	fmt.Printf("tanh(3) = %f\n", math.Tanh(3))       // Función Tangente Hiperbólica
	fmt.Printf("sech(3) = %f\n", 1.0/math.Cosh(3))   // Función Secante Hiperbólica
	fmt.Printf("csch(3) = %f\n", 1.0/math.Sinh(3))   // Función Cosecante Hiperbólica
	fmt.Printf("cotanh(3) = %f\n", 1.0/math.Tanh(3)) // Función Cotangente Hiperbólica

	// Funciones Hiporbolicas Inversas
	fmt.Printf("Arcosinh(5) = %f\n", math.Asinh(5))     // Función ArcoSeno Hiperbólico
	fmt.Printf("Arcocosh(5) = %f\n", math.Acosh(5))     // Función ArcoCoseno Hiperbólico
	fmt.Printf("Arcotanh(1/2) = %f\n", math.Atanh(0.5)) // Función ArcoTangente Hiperbólico

	// Funciones inversas restante
	/*
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
}
