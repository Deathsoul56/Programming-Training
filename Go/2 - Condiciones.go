//go:build ignore

/*
CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL EN GO

Esta clase cubre los conceptos fundamentales de condiciones en Go:
1. Entrada de datos con validación
2. Condicional simple (if-else) y múltiple (if-else if)
3. Estructura Switch y condicionales anidados
4. Operadores lógicos (&&, ||, !=)
5. Mapas como alternativa a condiciones
6. Manejo de errores en Go (defer, returns)
*/

package main

import (
	"fmt"
	"log"
	"strings"
)

func main() {

	fmt.Println("=== CLASE 2: CONDICIONES Y ESTRUCTURAS DE CONTROL ===")

	fmt.Println("\n--- ¿Qué son las condiciones? ---")
	fmt.Println("Las condiciones permiten que el programa tome decisiones")
	fmt.Println("basándose en si ciertas expresiones son verdaderas o falsas.")
	fmt.Println("Go evalúa expresiones que devuelven true o false.")

	// =============================================================================
	// 1. ENTRADA DE DATOS CON VALIDACIÓN
	// =============================================================================

	fmt.Println("\n1. ENTRADA DE DATOS CON VALIDACIÓN")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Entrada de datos con validación ---")
	fmt.Println("Antes de trabajar con condiciones, obtengamos un número del usuario:")

	// Validación de entrada
	var x int
	fmt.Print("Ingrese un número entero (o letras para forzar un error): ")
	_, err := fmt.Scan(&x)
	if err != nil {
		// log.Fatal imprime el mensaje y sale inmediatamente del programa
		log.Fatal("Error: Por favor, ingrese un número entero válido.")
	}
	fmt.Printf("Número ingresado correctamente: %d\n", x)

	// NOTA: Para no detener el programa permanentemente (en caso de pruebas rápidas), forzo la x a 13
	x = 13
	fmt.Printf("\nUsando x = %d para seguir con los siguientes ejemplos con normalidad.\n", x)

	// =============================================================================
	// 2. CONDICIONAL SIMPLE Y MÚLTIPLE
	// =============================================================================

	fmt.Println("\n2. CONDICIONAL SIMPLE Y MÚLTIPLE")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Condicional simple (if-else) ---")
	// Si condicional
	fmt.Printf("\nEvaluando si %d es par o impar:\n", x)
	if x%2 == 0 { // Si Condicion a cumplir
		fmt.Printf("✓ El numero %d es par\n", x) // Valor si es verdadero
	} else { // En caso contrario
		fmt.Printf("✓ El numero %d es impar\n", x) // Valor si es falso
	}

	fmt.Println("\n--- Condicional múltiple (if-else if-else) ---")
	// Mas de 1 condicion
	if x%3 == 0 { // Si condicion a cumplir
		fmt.Printf("✓ El valor %d es equivalente a 0 en modulo 3\n", x) // Valor si es verdadero
	} else if x%3 == 1 { // Pero si segunda condicion
		fmt.Printf("✓ El valor %d es equivalente a 1 en modulo 3\n", x) // Valor si segunda condicion es verdadera
	} else { // En caso contrario
		fmt.Printf("✓ El valor %d es equivalente a 2 en modulo 3\n", x) // Valor si no cumple ninguna condicion
	}

	// =============================================================================
	// 3. SWITCH Y CONDICIONALES ANIDADOS
	// =============================================================================

	fmt.Println("\n3. SWITCH Y CONDICIONALES ANIDADOS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Uso de switch para manejar múltiples condiciones ---")
	// Uso de switch para manejar múltiples condiciones (Mejor que múltiples if/else)
	switch x % 3 {
	case 0:
		fmt.Printf("✓ Switch: El valor %d es equivalente a 0 en modulo 3\n", x)
	case 1:
		fmt.Printf("✓ Switch: El valor %d es equivalente a 1 en modulo 3\n", x)
	case 2:
		fmt.Printf("✓ Switch: El valor %d es equivalente a 2 en modulo 3\n", x)
	}

	fmt.Println("\n--- Switch para menú o días ---")
	day := 3
	fmt.Printf("Evaluando el día %d de la semana:\n", day)

	switch day {
	case 1:
		fmt.Println("✓ Lunes")
	case 2:
		fmt.Println("✓ Martes")
	case 3:
		fmt.Println("✓ Miércoles")
	case 4:
		fmt.Println("✓ Jueves")
	case 5:
		fmt.Println("✓ Viernes")
	case 6:
		fmt.Println("✓ Sábado")
	case 7:
		fmt.Println("✓ Domingo")
	default:
		fmt.Println("✗ Día inválido")
	}

	fmt.Println("\n--- Condicionales Anidados ---")
	// If anidados
	y := 5
	fmt.Printf("Comparando x = %d con y = %d:\n", x, y)

	if x > y {
		fmt.Println("✓ x es mayor que y, ahora verificamos si x es par o impar:")
		if x%2 == 0 {
			fmt.Println("  ✓ x es par")
		} else {
			fmt.Println("  ✓ x es impar")
		}
	} else {
		fmt.Println("✓ x es menor o igual que y")
	}

	// =============================================================================
	// 4. OPERADORES LÓGICOS
	// =============================================================================

	fmt.Println("\n4. OPERADORES LÓGICOS")
	fmt.Println(strings.Repeat("=", 40))

	// If con operadores logicos
	z := 15
	fmt.Printf("\nComparando x = %d, y = %d, z = %d:\n", x, y, z)

	fmt.Println("\nUsando AND (&&) - Ambas deben cumplirse:")
	if x > y && x < z {
		fmt.Println("✓ x es mayor que y pero menor que z")
	} else if x > y && x > z {
		fmt.Println("✓ x es mayor que z e y")
	} else if x < y && x < z {
		fmt.Println("✓ x es menor que z e y")
	} else {
		fmt.Println("✗ ninguna condición de tipo AND se cumple")
	}

	fmt.Println("\nUsando OR (||) - Al menos una debe cumplirse:")
	if x > y || x > z {
		fmt.Println("✓ x es mayor que y O mayor que z")
	} else {
		fmt.Println("✗ x no es mayor que y ni mayor que z")
	}

	fmt.Println("\nUsando Distinto (!=):")
	if x != y {
		fmt.Println("✓ x no es igual a y")
	} else {
		fmt.Println("✓ x SÍ es igual a y")
	}

	// =============================================================================
	// 5. MAPAS COMO ALTERNATIVA
	// =============================================================================

	fmt.Println("\n5. MAPAS COMO ALTERNATIVA MÁS LIMPIA")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Uso de mapas para mapear condiciones ---")
	fmt.Println("A veces es más eficiente usar mapas para reemplazar switches largos")

	// Uso de mapas para mapear condiciones
	acciones := map[int]string{
		0: "El valor es equivalente a 0 en modulo 3",
		1: "El valor es equivalente a 1 en modulo 3",
		2: "El valor es equivalente a 2 en modulo 3",
	}

	// En Go podemos declarar y validar en la misma línea del IF
	if val, ok := acciones[x%3]; ok {
		fmt.Printf("✓ Resultado extraído del mapa: %s\n", val)
	} else {
		fmt.Println("✗ Valor no encontrado en el mapa")
	}

	// =============================================================================
	// 6. MANEJO DE ERRORES EN GO
	// =============================================================================

	fmt.Println("\n6. MANEJO DE ERRORES EN GO (TRY A LA GOLANG)")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Manejo de condicionales con Defer y Returns ---")
	fmt.Println("Go no tiene try-except, sino que maneja errores devolviendo variables explícitas.")

	// Condición de intentar (manejo de errores en Go)
	n1 := 10
	n2 := 3

	fmt.Printf("\nIntentando dividir %d entre %d\n", n1, n2)

	// defer se ejecuta siempre justo ANTES de que termine la función que lo contiene
	defer func() {
		fmt.Println("→ Bloque Defer finalizado (equivalente aproximado a un Finally)")
	}()

	// Evitar la división por 0 "manualmente" (manera de Go)
	if n2 == 0 {
		fmt.Println("✗ Error: No se pueden dividir números por cero")
		return // Salir de la función anticipadamente
	}

	resultado := float64(n1) / float64(n2)

	// Si el casteo a entero nos da el mismo número, entonces no tenía decimales reales.
	if resultado == float64(int(resultado)) {
		fmt.Printf("✓ La division da un numero entero %.0f\n", resultado)
	} else {
		fmt.Printf("✓ La division da un numero decimal %.3f\n", resultado)
	}

	// =============================================================================
	// CONCLUSIONES
	// =============================================================================

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("CONCLUSIONES SOBRE CONDICIONES EN GO")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Println("\n1. NO HAY PARENTESIS EN IF/SWITCH:")
	fmt.Println("   • En Go, declarar `if x == 2` no requiere el uso de paréntesis alrededor de la condición.")
	fmt.Println("   • Pasa lo mismo para el uso de Switches.")

	fmt.Println("\n2. EXPANSIÓN DEL SWITCH:")
	fmt.Println("   • Go no necesita explícitamente la palabra reservada `break` al final de cada caso del Switch como C/Java; se asume por defecto.")

	fmt.Println("\n3. LA LÓGICA DE MANEJO DE ERRORES:")
	fmt.Println("   • A diferencia de Python donde existe try-except, Go devuelve variables de error que verificas obligatoriamente (ej. `if err != nil`).")
	fmt.Println("   • El uso de sentencias `defer func()` actúa parecido a un block `finally`, asegurando que su código interior se ejecute justo cuando acabe la función que lo alberga.")

	fmt.Println("\n4. MAPAS PARA CONDICIONES MÁGICAS:")
	fmt.Println("   • En lugar de usar largos if-else, podemos preguntar a un mapa la condición mediante `if val, ok := acciones[key]; ok`.")

	fmt.Println("\n=== FIN DE LA CLASE 2 ===")

}
