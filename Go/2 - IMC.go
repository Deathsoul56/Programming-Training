package main

import (
	"fmt"
	"math"
)

/*
funcion IndiceIMC calcula el índice de masa corporal de una persona y con base en el resultado indica si tiene un peso normal,
inferior o superior al normal u obesidad.
*/
func main() {
	var masa float64 = 91                          // Masa en kilogramos
	var estatura float64 = 1.77                    // Estatura en metros
	var IMC float64 = masa / math.Pow(estatura, 2) // Calcular el índice de masa corporal
	fmt.Println("La persona tiene una masa = ", masa, "kilogramos y estatura = ", estatura, "metros")
	/* Mediante
	   varios if-else anidados se evalúan diferentes rangos del IMC */
	if IMC < 16 {
		fmt.Println("La persona tiene delgadez severa.")
	} else if IMC < 17 {
		fmt.Println("La persona tiene delgadez moderada.")
	} else if IMC < 18.5 {
		fmt.Println("La persona tiene delgadez leve.")
	} else if IMC < 25 {
		fmt.Println("La persona tiene peso normal.")
	} else if IMC < 30 {
		fmt.Println("La persona tiene sobrepeso.")
	} else if IMC < 35 {
		fmt.Println("La persona tiene obesidad leve.")
	} else if IMC < 40 {
		fmt.Println("La persona tiene obesidad media.")
	} else {
		fmt.Println("La persona tiene obesidad mórbida.")
	}
}
