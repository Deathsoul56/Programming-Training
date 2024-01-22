package main

import (
	"fmt"
)

// variable global
var y int = 0

func main() {

	var x int
	fmt.Print("Ingrese el valor aqui: ")
	fmt.Scan(&x)

	//Ciclo tipo While
	for y <= x {
		fmt.Println(y)
		y++
	}
	fmt.Println("Fin del Ciclo While")

	//Ciclo for
	for i := 0; i < y; i++ {
		// Código a ejecutar en cada iteración
		fmt.Println(i)
	}
	fmt.Println("Fin del Ciclo For")

}
