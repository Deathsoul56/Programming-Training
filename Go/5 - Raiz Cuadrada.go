//go:build ignore
// +build ignore

package main

import (
	"fmt"
	"math"
)

// Calcular funcion para calcular la raiz cuadrada por el metodo iteratiro de Heron
func main() {

	//Definicion de las variables
	var N float64
	var x float64

	//Ingresar los valores
	fmt.Print("Ingrese el primer valor de N aqui: ")
	fmt.Scan(&N)
	fmt.Print("Ingrese el valor inicial x_0: ")
	fmt.Scan(&x)
	y := math.Sqrt(N)

	e := 10.0
	tolerancia := 0.00000001
	for e > tolerancia {
		x_n := (x + N/x) / 2
		fmt.Print("Resultado aproximado: ", x_n, " ")
		e = math.Abs((x - x_n) / x_n)
		fmt.Println("El error es porcentual es: ", e)
		x = x_n
	}
	fmt.Println("Resultado Real: ", y)
	fmt.Println("El error Real es: ", y-x)
}
