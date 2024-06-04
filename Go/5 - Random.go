//go:build ignore
// +build ignore

package main

import (
	"fmt"
	"math/rand"

	"gonum.org/v1/gonum/stat/distuv"
)

func main() {
	// Números Pseudo-Aleatorios
	aleatorio := rand.Float64() // Genera un número aleatorio entre 0 y 1
	fmt.Printf("Número aleatorio entre 0 y 1: %f\n", aleatorio)

	aleatorio2 := rand.Intn(21) - 10 // Genera un número entre 0 y 20 [0, 21)
	fmt.Printf("Número aleatorio entre -10 y 10: %d\n", aleatorio2)

	aleatorio2 = rand.Intn(20+1) - 10 // Genera un número entre 0 y 20, luego resta 10 para obtener entre -10 y 10 [-10, 11)
	fmt.Printf("Número aleatorio entre -10 y 10: %d\n", aleatorio2)

	vector := make([]int, 10)
	for i := range vector {
		vector[i] = rand.Intn(21) - 10 // Vector de 10 números aleatorios entre -10 y 10
	}
	fmt.Printf("Vector aleatorio: %v\n", vector)

	muestra := make([]float64, 5)
	for i := range muestra {
		muestra[i] = rand.Float64() // Vector de 10 números aleatorios entre 0 y 1
	}
	fmt.Printf("Muestra aleatoria: %v\n", muestra)

	bytesAleatorios := make([]byte, 12) // Bytes Aleatorios
	_, err := rand.Read(bytesAleatorios)
	if err != nil {
		fmt.Println("Error al generar bytes aleatorios:", err)
		return
	}
	fmt.Printf("Bytes aleatorios: %x\n", bytesAleatorios)

	// Matriz aleatoria
	matriz := make([][]int, 4) // 4 filas
	for i := range matriz {
		matriz[i] = make([]int, 3) // 3 Columnas
		for j := range matriz[i] {
			matriz[i][j] = rand.Intn(21) - 10 // números entre -10 y 10 [-10, 11)
		}
	}
	fmt.Printf("Matriz aleatoria: %v\n", matriz)

	// Matriz aleatoria entre 0 y 1 (0, 1)
	matriz2 := make([][]float64, 2) // 2 filas
	for i := range matriz2 {
		matriz2[i] = make([]float64, 2) // 2 columnas
		for j := range matriz2[i] {
			matriz2[i][j] = rand.Float64() // números entre 0 y 1
		}
	}
	fmt.Printf("Matriz aleatoria entre 0 y 1: %v\n", matriz2)

	// Distribuciones de probabilidad continuas
	// Distribución Normal
	mu := 5.0 // Media
	sd := 8.0 // Desviación Estándar

	// Inicializar la Distribución Normal
	normalDist := distuv.Normal{
		Mu:    mu,
		Sigma: sd,
	}
	// Valor aleatorio con distribución normal
	normalValue := normalDist.Rand()
	fmt.Printf("Valor aleatorio con distribución Normal media: %.2f desviación estándar: %.2f = %.2f\n", mu, sd, normalValue)

	// Vector aleatorio con distribución normal
	size := 10
	normalVector := make([]float64, size)
	for i := range normalVector {
		normalVector[i] = normalDist.Rand()
	}
	fmt.Printf("Vector aleatorio con distribución Normal media: %.2f desviación estándar: %.2f = %v\n", mu, sd, normalVector)

	// Distribución Exponencial
	Lambda := 3.0 // Parámetro Lambda (es el inverso de la escala en gonum)

	// Inicializar la Distribución Exponencial
	exponencial := distuv.Exponential{
		Rate: 1 / Lambda, // La tasa es el inverso de Lambda
		Src:  nil,
	}

	// Generar un valor aleatorio con distribución exponencial
	valorexpo := exponencial.Rand()
	fmt.Printf("Valor aleatorio con distribución Exponencial Lambda: %v = %v\n", Lambda, valorexpo)

	// Generar un vector aleatorio con distribución exponencial
	vectorexpo := make([]float64, 10)
	for i := 0; i < 10; i++ {
		vectorexpo[i] = exponencial.Rand()
	}
	fmt.Printf("Vector aleatorio con distribución Exponencial Lambda: %v = %v\n", Lambda, vectorexpo)

	// Distribuciones de probabilidad discretas
	// Distribución Binomial
	N := 10      // Cantidad de intentos
	Prop := 0.25 // Probabilidad de éxito

	// Inicializar la Distribución Binomial
	binomial := distuv.Binomial{
		N:   float64(N),
		P:   Prop,
		Src: nil,
	}

	// Generar un valor aleatorio con distribución binomial
	valorAleatorio := binomial.Rand()
	fmt.Printf("Valor aleatorio con distribución Binomial Intentos: %v Probabilidad: %v = %v\n", N, Prop, valorAleatorio)

	// Generar un vector aleatorio con distribución binomial
	vectorAleatorio := make([]float64, 10)
	for i := 0; i < 10; i++ {
		vectorAleatorio[i] = binomial.Rand()
	}
	fmt.Printf("Vector aleatorio con distribución Binomial Intentos: %v Probabilidad: %v = %v\n", N, Prop, vectorAleatorio)

	// Distribucion Poisson
	Lambda = 6.0 // Parámetro Lambda

	// Generar un valor aleatorio con distribución Poisson
	poisson := distuv.Poisson{
		Lambda: Lambda,
		Src:    nil,
	}

	valorpois := poisson.Rand()
	fmt.Printf("Valor aleatorio con distribución Poisson Lambda: %v = %v\n", Lambda, valorpois)

	// Generar un vector aleatorio con distribución Poisson
	vectorpois := make([]float64, 10)
	for i := 0; i < 10; i++ {
		vectorpois[i] = poisson.Rand()
	}
	fmt.Printf("Vector aleatorio con distribución Poisson Lambda: %v = %v\n", Lambda, vectorpois)
}
