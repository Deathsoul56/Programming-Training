//go:build ignore
// +build ignore

package main

import (
	"fmt"
	"time"
)

// Función factorial en Go
func factorial(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	return n * factorial(n-1)
}

// Función fibonacci en Go
func fibonacci(n int) int {
	if n == 1 || n == 2 {
		return 1
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func fibonacciDinamico(f int) int {
	seq := make([]int, f)
	seq[0] = 1
	seq[1] = 1
	for i := 2; i <= f-1; i++ {
		seq[i] = seq[i-1] + seq[i-2]
	}
	//fmt.Println(seq)
	return seq[f-1]
}

func main() {
	// Imprimir factoriales del 0 al 10
	for i := 0; i <= 10; i++ {
		fmt.Printf("%d! = %d\n", i, factorial(i))
	}

	// Imprimir los primeros 10 números de Fibonacci
	for i := 1; i <= 10; i++ {
		fmt.Printf("fibonacci_%d = %d\n", i, fibonacci(i))
	}

	var x int
	fmt.Print("Ingreser valor aqui: ")
	fmt.Scan(&x)
	Ti := time.Now()

	if x > 1 {
		fmt.Print("Con el metodo Dinamico: ", fibonacciDinamico(x), " ")
		Tf := time.Now()
		duracion := Tf.Sub(Ti)
		fmt.Println("La ejecución tomó: ", duracion)
	}

	fmt.Print("Con el metodo recursivo: ", fibonacci(x), " ")
	Tf := time.Now()
	duracion := Tf.Sub(Ti)
	fmt.Println("La ejecución tomó: ", duracion)
}
