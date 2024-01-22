package main

import (
	"fmt"

	"github.com/gonum/matrix/mat64"
)

func main() {
	// Definir un vector columna
	vec := mat64.NewVector(3, []float64{1, 2, 3})

	// Imprimir el vector
	fmt.Println("Vector columna:")
	fmt.Printf("%v\n\n", mat64.Formatted(vec, mat64.Prefix("")))

	// Acceder a elementos individuales del vector
	fmt.Printf("Elemento en la posición 2: %v\n\n", vec.At(1, 0))

	// Definir un vector fila
	vecFila := mat64.NewDense(1, 3, []float64{4, 5, 6})

	// Imprimir el vector fila
	fmt.Println("Vector fila:")
	fmt.Printf("%v\n\n", mat64.Formatted(vecFila, mat64.Prefix("   ")))

	// Acceder a elementos individuales del vector fila
	fmt.Printf("Elemento en la posición 3: %v\n\n", vecFila.At(0, 2))

	// Definir dos vectores
	vec1 := mat64.NewVector(3, []float64{1, 2, 3})
	vec2 := mat64.NewVector(3, []float64{4, 5, 6})

	// Calcular el producto punto
	dotProduct := mat64.Dot(vec1, vec2)

	// Imprimir el resultado
	fmt.Println("Vector 1: ")
	fmt.Println(mat64.Formatted(vec1, mat64.Prefix("")))
	fmt.Println("Vector 2: ")
	fmt.Println(mat64.Formatted(vec2, mat64.Prefix("")))
	fmt.Printf("Producto punto entre los vectores: %v\n", dotProduct)
}
