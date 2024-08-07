//go:build ignore
// +build ignore

package main

import "fmt"

func main() {

	// Si condicional
	x := 13
	if x%2 == 0 { // Si Condicion a cumplir
		fmt.Printf("El numero %d es par\n", x) // Valor si es verdadero
	} else { // En caso contrario
		fmt.Printf("El numero %d es impar\n", x) // Calor si es falso
	}

	// Mas de 1 condicion
	if x%3 == 0 { // Si condicion a cumplir
		fmt.Printf("El valor %d es equivalente a 0 en modulo 3\n", x) // Valor si es verdadero
	} else if x%3 == 1 { // Pero si segunda condicion
		fmt.Printf("El valor %d es equivalente a 1 en modulo 3\n", x) // Valor si segunda condicion es verdadera
	} else { // En caso contrario
		fmt.Printf("El valor %d es equivalente a 2 en modulo 3\n", x) // Valor si no cumple ninguna condicion
	}

	x = 10
	y := 5

	if x > y {
		fmt.Println("x es mayor que y")
		if x%2 == 0 {
			fmt.Println("x es par")
		} else {
			fmt.Println("x es impar")
		}
	} else {
		fmt.Println("x es menor o igual que y")
	}

	// If con operadores logicos
	x = 10
	y = 5
	z := 15

	if x > y && x < z {
		fmt.Println("x es mayor que y pero menor que z")
	} else if x > y && x > z {
		fmt.Println("x es mayor que z e y")
	} else if x < y && x < z {
		fmt.Println("x es menor que z e y")
	} else {
		fmt.Println("ninguna condición se cumple")
	}

	// Condicion tipo Case

	day := 3

	switch day {
	case 1:
		fmt.Println("Lunes")
	case 2:
		fmt.Println("Martes")
	case 3:
		fmt.Println("Miércoles")
	case 4:
		fmt.Println("Jueves")
	case 5:
		fmt.Println("Viernes")
	case 6:
		fmt.Println("Sábado")
	case 7:
		fmt.Println("Domingo")
	default:
		fmt.Println("Día inválido")
	}
}
