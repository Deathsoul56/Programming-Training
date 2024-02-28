//go:build ignore
// +build ignore

package main

import (
	"fmt"
	"reflect"
)

// variable global
var y int = 0

func main() {

	x := -3

	// En Go solo existe los ciclos for
	// Ciclo tipo While
	for x <= 10 {
		fmt.Printf("Valor de x = %d \n", x)
		x++
	}
	fmt.Println("Fin del Ciclo While")

	for {
		y++
		if y == 5 {
			fmt.Println("Se rompio el ciclo")
			break // Romper el Ciclo
		} else {
			fmt.Println("Ciclo infinito")
		}
	}

	// Ciclo for
	for i := 0; i < 5; i++ {
		// Código a ejecutar en cada iteración
		fmt.Println("Valor de i = ", i)
	}
	fmt.Println("Fin del Ciclo For")

	list := []interface{}{"a", "c", 7, 3.1415, true, "lamda"}
	for index, value := range list {
		fmt.Printf("En elemento %d de la lista es = %v de tipo = %v\n", index, value, reflect.TypeOf(value))
	}

	// Ciclos Anidados
	numeros := []int{1, 2, 3}
	letras := []string{"a", "b", "c"}

	for _, numero := range numeros {
		for _, letra := range letras {
			fmt.Println(numero, letra)
		}
	}

	matriz := [][]int{{4, 7, 9, 3}, {2, 4, 6, 1}}
	fmt.Printf("La matriz original: %v\n", matriz)
	for i, row := range matriz {
		fmt.Printf("Valor %d es: %v\n", i, row)
		for j, val := range row {
			fmt.Printf("El valor en la posición [%d][%d] es: %d\n", i, j, val)
		}
	}

}
