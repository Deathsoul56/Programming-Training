package main

import (
	"fmt"
	"time"
)

func fibonacci(f int) int {
	if f == 1 || f == 2 {
		return 1
	} else {
		return fibonacci(f-1) + fibonacci(f-2)
	}
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
