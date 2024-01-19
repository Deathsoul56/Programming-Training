package main

import "fmt"

func factorial(n int) int {
	if n == 0 || n == 1 {
		return 1
	} else {
		return n * factorial(n-1)
	}
}

func main() {
	var n int
	fmt.Print("Ingrese el valor aqui: ")
	fmt.Scan(&n)
	fmt.Print(factorial(n))
}
