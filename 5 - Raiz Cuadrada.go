package main

import (
	"fmt"
)

func main() {

	//Definicion de las variables
	var x float64
	var y float64

	//Ingresar los valores
	fmt.Print("Ingrese el primer valor de X aqui: ")
	fmt.Scan(&x)
	fmt.Print("Ingrese el segundo valor de Y aqui: ")
	fmt.Scan(&y)

	fmt.Println(x - float64(int(x)))
	fmt.Println(y - float64(int(y)))

	c := [5]int{}
	fmt.Println(c, "Dato tipo Array")

}
