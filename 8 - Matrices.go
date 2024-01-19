package main

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
)

func main() {

	// Inicializar una matriz de tamaño 3x3
	matriz := mat.NewDense(3, 3, []float64{
		1, 2, 4,
		2, 1, -4,
		0, 0, 3,
	})

	// Imprimir la matriz
	fmt.Println(mat.Formatted(matriz))

	// Imprimir la transpuesta
	fmt.Println("Transpuesta:")
	fmt.Println(mat.Formatted(matriz.T()))

	//Multiplicacion de matriz
	resultado := mat.NewDense(3, 3, nil)
	resultado.Mul(matriz, matriz)
	fmt.Println("A^2")
	fmt.Println(mat.Formatted(resultado))

	// Calcular el determinante
	det := mat.Det(matriz)
	fmt.Printf("Determinante de la matriz:\n%.2f\n", det)

}
