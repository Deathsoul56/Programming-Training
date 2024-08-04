//go:build ignore
// +build ignore

package main

import (
	"fmt"

	"github.com/gonum/matrix/mat64"
	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/spatial/r3"
)

func main() {
	// Definir matrices y vectores
	vector2d := []float64{3, 4}
	vector3d := []float64{7, 4, 6}
	vector4d := []float64{8, 14, 7, 11}

	fmt.Println("vector en 2 dimensiones: ", vector2d)
	fmt.Println("vector en 3 dimensiones: ", vector3d)
	fmt.Println("vector en 4 dimensiones: ", vector4d)

	data := []float64{
		2, 4,
		3, 7,
	}
	matrix := mat.NewDense(2, 2, data)

	data1 := []float64{
		6, 8,
		12, 9,
	}
	matrix1 := mat.NewDense(2, 2, data1)

	fmt.Println(matrix, "Matriz de prueba")
	fmt.Println(matrix1, "Matriz de prueba")

	// Operaciones de Vectores
	v1 := r3.Vec{X: 7, Y: 4, Z: 6}
	v2 := r3.Vec{X: 5, Y: 9, Z: 8}

	// Producto punto
	productoPunto := v1.X*v2.X + v1.Y*v2.Y + v1.Z*v2.Z
	fmt.Printf("El producto punto entre %v y %v es: %.2f\n", v1, v2, productoPunto)

	// Producto cruz
	productoCruz := r3.Cross(v1, v2)
	fmt.Printf("El producto cruz entre %v y %v es: %v\n", v1, v2, productoCruz)

	// Operaciones de Matrices
	data2 := []float64{
		11, 5, 13, 9,
		6, 9, 14, 11,
		9, 4, 5, 3,
	}
	matriz1 := mat.NewDense(3, 4, data2)

	data3 := []float64{
		5, 3,
		9, 4,
		10, 3,
		13, 5,
	}
	matriz2 := mat.NewDense(4, 2, data3)

	var resultado mat.Dense
	resultado.Mul(matriz1, matriz2)

	fmt.Println("El resultado de la multiplicación de las matrices:")
	fmt.Println(mat.Formatted(&resultado, mat.Prefix(""), mat.Excerpt(0)))

	preview()
	matr()
}

func preview() {
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

func matr() {
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
