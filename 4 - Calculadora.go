package main

import (
	"fmt"
	"math"
)

// crear funcion para sumar 2 numeros
func suma(sumando1, sumando2 float64) float64 {
	return sumando1 + sumando2
}

// crear funcion para restar 2 numeros
func resta(minuendo, sustraendo float64) float64 {
	return minuendo - sustraendo
}

// crear funcion para multiplicar 2 numeros
func multiplicar(factor1, factor2 float64) float64 {
	return factor1 * factor2
}

// crear funcion para dividir 2 numeros
func dividir(numerador, denominador float64) float64 {
	if denominador == 0 {
		return math.NaN()
	} else {
		return numerador / denominador
	}
}

// crear funcion para elevar un numero a otro
func power(base, exponente float64) float64 {
	return math.Pow(base, exponente)
}

// crear funcion para racionalizar
func raizN(radicando, indice float64) float64 {
	if indice == 0 {
		return math.NaN()
	} else {
		return math.Pow(radicando, 1.0/indice)
	}
}

// crear funcion para modulo
func modulo(dividendo, divisor int) int {
	if divisor == 0 {
		return int(math.NaN())
	} else {
		return dividendo % divisor
	}
}

// crear funcion para logaritmo
func logaritmo(argumento, base float64) float64 {
	return math.Log(argumento) / math.Log(base)
}

func main() {

	//Definicion de las variables
	var x float64
	var y float64

	//Ingresar los valores
	fmt.Print("Ingrese el primer valor de X aqui: ")
	fmt.Scan(&x)
	fmt.Print("Ingrese el segundo valor de Y aqui: ")
	fmt.Scan(&y)

	//Invoca funcion para sumar
	fmt.Println("La suma de los valores es: ", suma(x, y))

	//invoca funcion para restar
	fmt.Println("La resta de los valores es: ", resta(x, y))

	//invocar funcion para multiplicar
	fmt.Println("La resta de los valores es: ", multiplicar(x, y))

	//invocar funcion para dividir
	fmt.Println("La division de los valores es: ", dividir(x, y))

	//Invoca funcion para la potencia
	fmt.Println("X elevado a Y es: ", power(x, y))

	//Invoca funcion para la radicacion
	fmt.Println("La racion Y-ecima de X es: ", raizN(x, y))

	//invocar funcion modulo solo si son enteros
	if x-float64(int(x)) == 0 && y-float64(int(y)) == 0 { //condicion para restar la parte entera de los numeros
		fmt.Println("X en modulo Y es: ", modulo(int(x), int(y)))
	} else {
		fmt.Printf("Los valores no son enteros")
	}

	//invocar funcion logaritmo
	fmt.Println("El logaritmo de X en base Y es: ", logaritmo(x, y))
}
