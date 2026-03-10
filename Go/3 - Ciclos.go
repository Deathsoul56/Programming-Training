//go:build ignore

/*
CLASE 3: CICLOS EN GO

Esta clase cubre los conceptos fundamentales de ciclos en Go:
1. Ciclo While simulado (En Go solo existe 'for')
2. Ciclo For tradicional
3. Recorriendo arreglos, slices y listas (range)
4. Control de flujo (break, continue)
5. Ciclos anidados y simulación de Zip
6. Recorriendo matrices bidimensionales
*/

package main

import (
	"fmt"
	"reflect"
	"strings"
)

// variable global
var y int = 0

func main() {

	fmt.Println("=== CLASE 3: CICLOS EN GO ===")

	fmt.Println("Los ciclos nos permiten repetir código de manera eficiente.")
	fmt.Println("En Go, la única palabra reservada para crear ciclos es 'for'.")
	fmt.Println("No existen 'while' ni 'do-while', pero 'for' puede simularlos.")
	fmt.Println()

	// =============================================================================
	// 1. CICLO WHILE SIMULADO
	// =============================================================================

	fmt.Println("1. CICLO WHILE SIMULADO (CON FOR)")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Ciclo estilo While (en Go no existe el while como tal) ---")

	x := -3
	// For funcionando como 'while'
	for x <= 10 {
		fmt.Printf("✓ Valor de x = %d\n", x)
		x++
	}

	fmt.Println("\n--- Ciclo infinito y uso de Break ---")
	y = 0
	// For sin condición es un ciclo infinito
	for {
		y++
		if y == 5 {
			fmt.Println("→ Se rompio el ciclo (break)")
			break // Romper el ciclo
		} else {
			fmt.Println("→ Ciclo infinito")
		}
	}

	// =============================================================================
	// 2. CICLO FOR TRADICIONAL
	// =============================================================================

	fmt.Println("\n2. CICLO FOR TRADICIONAL")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Avanzar por un rango lógico ---")
	// For sintaxis clásica de C o Java
	for i := 0; i <= 5; i++ {
		fmt.Printf("✓ Valor de i = %02d\n", i)
	}

	fmt.Println("\n--- Rango con intervalo ---")
	for j := -5; j < 7; j++ {
		fmt.Printf("  • Valor de j = %d\n", j)
	}

	// =============================================================================
	// 3. RECORRIENDO ARREGLOS Y SLICES (RANGE)
	// =============================================================================

	fmt.Println("\n3. RECORRIENDO ARREGLOS Y SLICES (RANGE)")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Avanzar por una lista variada (interface{}) ---")
	miLista := []interface{}{"a", "c", 7, 3.1415, true, "lambda"}

	// Uso de range. Retorna el índice (index) y el valor (elemento) copiado.
	for index, elemento := range miLista {
		fmt.Printf("El elemento %d de la lista es = %v de tipo = %v\n", index, elemento, reflect.TypeOf(elemento))
	}

	fmt.Println("\n--- Verificar múltiples valores en una lista ---")
	numeros := []int{10, 15, 20, 25, 30}

	// Si no queremos usar el índice, lo ignoramos con _
	for _, num := range numeros {
		if num%2 == 0 {
			fmt.Printf("✓ %d es par\n", num)
		} else {
			fmt.Printf("✓ %d es impar\n", num)
		}
	}

	// =============================================================================
	// 4. CONTROL DE FLUJO (BREAK, CONTINUE Y ERRORES)
	// =============================================================================

	fmt.Println("\n4. CONTROL DE FLUJO (BREAK Y CONTINUE)")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Ciclos con continue ---")
	for i := 0; i < 10; i++ {
		if i%2 == 0 {
			continue // Saltar iteraciones bajo cierta condición
		}
		fmt.Printf("Número impar extraído: %d\n", i)
	}

	fmt.Println("\n--- Ciclos con manejo de evitar errores ---")
	for i := -1; i < 5; i++ {
		if i == 0 { // Verificación manual de la división por cero
			fmt.Printf("✗ Error: No se puede dividir 10 entre %d (división por cero).\n", i)
			continue // Continuar con la siguiente iteración
		}
		fmt.Printf("10 / %d: %f\n", i, float64(10)/float64(i))
	}

	// =============================================================================
	// 5. CICLOS ANIDADOS Y SIMULACIÓN DE ZIP
	// =============================================================================

	fmt.Println("\n5. CICLOS ANIDADOS Y SIMULACIÓN DE ZIP")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Ciclos Anidados (Multiplicativos) ---")
	nums := []int{1, 2, 3}
	letters := []string{"a", "b", "c"}
	for _, numero := range nums {
		for _, letra := range letters {
			fmt.Printf("  • Numero: %d, Letra: %s\n", numero, letra)
		}
	}

	fmt.Println("\n--- Alternativa con Zip simulado lineal ---")
	// Alternativa con zip (Go no tiene zip nativo de Python, pero se puede simular iterando un mismo índice)
	minLen := len(nums)
	if len(letters) < minLen {
		minLen = len(letters)
	}
	for i := 0; i < minLen; i++ {
		fmt.Printf("  • Pareja: %d - %s\n", nums[i], letters[i])
	}

	// =============================================================================
	// 6. RECORRIENDO MATRICES
	// =============================================================================

	fmt.Println("\n6. RECORRIENDO MATRICES")
	fmt.Println(strings.Repeat("=", 40))

	// Recorrer una matriz
	matriz := [][]int{{4, 7, 9, 3}, {2, 4, 6, 1}}
	fmt.Printf("\nLa matriz original: %v\n", matriz)

	for i, fila := range matriz {
		fmt.Printf("Fila %d: %v\n", i, fila)
		for j, valor := range fila {
			fmt.Printf("  -> Columna %d: %d\n", j, valor)
		}
	}

	// =============================================================================
	// CONCLUSIONES
	// =============================================================================

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("CONCLUSIONES SOBRE CICLOS EN GO")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Println("\n1. PREDOMINIO DE FOR:")
	fmt.Println("   • 'for' es la única instrucción para crear ciclos en Go.")
	fmt.Println("   • For infinito: for { }")
	fmt.Println("   • For while: for condicion { }")
	fmt.Println("   • For clásico: for declaracion; condicion; incremento { }")

	fmt.Println("\n2. LA MAGIA DE RANGE:")
	fmt.Println("   • Sirve para iterar sobre Arrays, Slices, Maps y Strings.")
	fmt.Println("   • Retorna siempre dos cosas: Index y Value. Usa un guión bajo '_' si no necesitas uno de ellos.")

	fmt.Println("\n3. PREVENIR ERRORES (DIV/0):")
	fmt.Println("   • Ya que en Go un panic mata el programa, los ciclos requieren verificación preventiva manual si es que se realizan operaciones aritméticas arriesgadas como dividir.")

	fmt.Println("\n=== FIN DE LA CLASE 3 ===")
}
