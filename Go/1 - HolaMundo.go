//go:build ignore

/*
CLASE 1: HOLA MUNDO GO

Esta clase cubre los conceptos fundamentales en Go (Golang):
1. Características del lenguaje y variables
2. Tipos de datos básicos y estructuras compuestas
3. Operaciones aritméticas y lógicas
4. Punteros y transformación de variables (Casting)
5. Entrada de usuario (fmt.Scan)
6. Métodos útiles del paquete strings
*/

package main

// Importar las librerias
import (
	"fmt"     // Libreria con metodos escenciales
	"reflect" // Libreria para comparar el tipo de dato
	"strings" // Librerias para metodos de string
)

func main() {

	fmt.Println("=== CLASE 1: HOLA MUNDO GO ===")

	// =============================================================================
	// 1. CARACTERÍSTICAS DEL LENGUAJE Y COMENTARIOS
	// =============================================================================
	fmt.Println("1. CARACTERÍSTICAS DEL LENGUAJE Y COMENTARIOS")
	fmt.Println(strings.Repeat("=", 40))

	// Imprimir un mensaje inicial
	fmt.Println("\n--- Hola Mundo ---")
	fmt.Println("Alola Mundo Go!")

	fmt.Println("\n--- Tipos de Impresión en Consola ---")
	// Diferencia entre Print, Println y Printf en el paquete fmt:
	fmt.Print("1. fmt.Print: Imprime en consola SIN salto de línea final. ")
	fmt.Print("(Queda en la misma línea)\n")

	fmt.Println("2. fmt.Println: Imprime en consola agregando un salto de línea automático al final.")

	age_ejemplo := 21
	fmt.Printf("3. fmt.Printf: Permite formatear (Format) el texto para inyectar variables usando verbos como %%d (int), %%s (string), %%f (float), etc. Edad: %d\n", age_ejemplo)

	fmt.Println("\n--- Comentarios en Go ---")
	// Los comentarios de una linea se hacen con doble Slash
	fmt.Println("Los comentarios de una línea usan //")

	/*
		Los comentarios largos de varias lineas
		se hacen abriendo con slash *
		y cerrando con * slash
	*/
	fmt.Println("Los comentarios multilínea usan /* */")

	// =============================================================================
	// 2. VARIABLES Y TIPOS DE DATOS
	// =============================================================================
	fmt.Println("\n2. VARIABLES Y TIPOS DE DATOS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Declaración de tipos básicos ---")
	// Tipos de Datos en Go (Fuertemente Tipado) Las variables deben ser usadas o el programa no compilará
	// Para definir una variable se debe indicar con var y despues el tipo de esta
	var x int // Int por defecto es de 32 bits, puede ser de 8, 16, 32 y 64 bits
	x = 14    // Se asigna el valor de esta con el signo =

	// Se puede declarar y asignar valor al mismo tiempo
	var y1 float32 = 2.3                          // Float de 32 bits
	var y2 float64 = 6.651981213516               // Float de 64 bits
	var z1 complex64 = complex(3.7, 4)            // Complejo de 64 bits
	var z2 complex128 = complex(2.2165, 6.126541) // Complejo de 128 bits
	var b bool = true                             // Boleano
	var s string = "Esto es un string"            // String
	var v byte = 'Ñ'                              // Byte

	var x8 int8 = -8 // Entero de 8 bits
	var ux8 uint = 8 // Entero positivo, los otros datos numericos tambien pueden ser solo positivo

	// Imprimir los datos
	fmt.Println(x, "De tipo Entero")
	fmt.Println(y1, "Dato tipo float")
	fmt.Println(y2, "Dato tipo float64")
	fmt.Println(z1, "Dato tipo complex 32 bits")
	fmt.Println(z2, "Dato tipo complex 64 bits")
	fmt.Println(b, "Dato tipo booleano")
	fmt.Println(s, "Dato tipo string")
	fmt.Println(v, "Dato tipo byte") // Imprime el valor ASCII

	// Forma alternativa de imprimir
	fmt.Println("Entero pequeño:", x8, "entero no negativo:", ux8)      // Separando con comas
	fmt.Printf("Entero pequeño: %d entero no negativo: %d \n", x8, ux8) // Especificando con Printf y formato

	fmt.Println("\n--- Colecciones y Estructuras Compuestas ---")
	// Array, todos los elementos de un array deben ser de un mismo tipo y no puede modificarse su tamaño
	var arreglo [5]int = [5]int{10, 25, 15, 32, 51}
	fmt.Println(arreglo, "Dato tipo Array")

	// Slice, es similar a un array, pero su tamaño puede ser modificado dinámicamente.
	var loncha []int = []int{1, 2, 3, 4, 5}
	fmt.Println(loncha, "Dato tipo slice")
	loncha = append(loncha, 6) // Con append se agregan los datos a un Slice
	fmt.Println(loncha, "se agrega un valor")

	// Struct, representa un conjunto de campos con diferentes tipos de datos.
	type Persona struct {
		Nombre string
		Edad   int
		Altura float32
	}
	var persona1 Persona
	persona1.Nombre = "Juan"
	persona1.Edad = 23
	persona1.Altura = 1.73
	fmt.Println(persona1, "Dato tipo struct")

	// Variable tipo Mapa
	mapa := make(map[string]int) // Crear un mapa vacio

	// Asignar valores al mapa
	mapa["Primer Valor"] = 10
	mapa["Segundo Valor"] = 27
	mapa["Tercer Valor"] = 13
	fmt.Println("Mapa completo:", mapa)

	fmt.Println("\n--- Inferencia de tipo y Constantes ---")
	// Las variables se pueden definir sin especificar el tipo (infiriendo el tipo de dato) usando :=
	Entero := 3                   // int
	Flotante := 6.515434          // float64
	Complejo := complex(5, 6)     // complex
	Booleano := false             // boolean
	Cadena := "cadena"            // string
	Arreglo := [3]int{12, 27, 81} // array
	Corte := []int{1, 2, 3}       // slice
	Estructura := Persona{        // struct
		Nombre: "María",
		Edad:   25,
		Altura: 1.68,
	}

	fmt.Println(Entero, Flotante, Complejo, Booleano, Cadena, Arreglo, Corte, Estructura)

	// Una variable NO puede cambiar de tipo (tipado estático)
	// Go es Case Sensitive, distingue entre mayúsculas y minúsculas
	m := 133
	M := "Alola 654"
	fmt.Printf("Valor de m = %d distinto al el valor de M = %s\n", m, M)

	// Constante, son variables que no pueden cambiar su valor, pueden no ser usadas y el programa aún así funcionará
	const C = "Valor de una constante"
	const Pi = 3.141592

	// Función para saber si una variable pertenece a cierto tipo
	A := 3.14
	fmt.Println("A es un float64:", reflect.TypeOf(A).Kind() == reflect.Float64)
	fmt.Println("A es un string:", reflect.TypeOf(A).Kind() == reflect.String)

	// =============================================================================
	// 3. OPERACIONES ARITMÉTICAS Y LÓGICAS
	// =============================================================================
	fmt.Println("\n3. OPERACIONES ARITMÉTICAS Y LÓGICAS")
	fmt.Println(strings.Repeat("=", 40))

	// Operaciones en Go
	/* Si se operan variables de distintos bits el resultado tendrá la cantidad de bits mayor (int8 + int16 = int16)
	No se puede operar variables de distinto tipo, para eso deberemos transformarlas para que tengan el mismo tipo
	*/

	fmt.Println("\n--- Operaciones Aritméticas ---")
	entero1 := 23
	entero2 := 14

	fmt.Printf("Suma: %d + %d = %d\n", entero1, entero2, entero1+entero2)           // Suma
	fmt.Printf("Resta: %d - %d = %d\n", entero1, entero2, entero1-entero2)          // Resta
	fmt.Printf("Multiplicacion: %d * %d = %d\n", entero1, entero2, entero1*entero2) // Multiplicacion
	fmt.Printf("Divison Entera: %d / %d = %d\n", entero1, entero2, entero1/entero2) // Division Entera

	flotante1 := float32(entero1)
	flotante2 := float32(entero2)
	fmt.Printf("Division: %f / %f = %f\n", flotante1, flotante2, flotante1/flotante2) // Se requiere float para ver decimales
	fmt.Printf("Modulo: %d %% %d = %d\n", entero1, entero2, entero1%entero2)          // Modulo (%%)

	fmt.Println("\n--- Operadores de Comparación ---")
	Op1 := 23
	Op2 := 57

	fmt.Printf("¿Es %d > %d? %t Mayor estricto\n", Op1, Op2, Op1 > Op2)
	fmt.Printf("¿Es %d < %d? %t Menor estricto\n", Op1, Op2, Op1 < Op2)
	fmt.Printf("¿Es %d >= 23? %t Mayor o igual\n", Op1, Op1 >= 23)
	fmt.Printf("¿Es 44 <= %d? %t Menor o igual\n", Op2, 44 <= Op2)
	fmt.Printf("¿Es %d == %d? %t Igual a\n", Op1, Op2, Op1 == Op2)
	fmt.Printf("¿Es %d == 57? %t\n", Op2, Op2 == 57)
	fmt.Printf("¿Es %d != %d? %t Distinto a\n", Op1, Op2, Op1 != Op2)

	fmt.Println("\n--- Algebra Booleana y Lógica ---")
	t := true
	f := false
	t2 := true

	fmt.Println("Valor de t:", t)
	fmt.Println("Valor de ~t:", !t)        // Negación Lógica (!)
	fmt.Println("Valor de t ∧ f:", t && f) // Conjunción Lógica AND (&&)
	fmt.Println("Valor de t ∧ t2:", t && t2)
	fmt.Println("Valor de t ∨ f:", t || f) // Disyunción Lógica OR (||)

	// =============================================================================
	// 4. TRANSFORMACIÓN DE VARIABLES Y PUNTEROS
	// =============================================================================
	fmt.Println("\n4. TRANSFORMACIÓN DE VARIABLES Y PUNTEROS")
	fmt.Println(strings.Repeat("=", 40))

	fmt.Println("\n--- Operaciones de Asignación ---")
	x1 := 14
	x1 = x + 2 // se asigna el mismo valor + 2
	x1 += 2    // Atajo de la operaciones anterior
	fmt.Println("Uso de +=:", x1)

	// Todas las operaciones básicas tienen su atajo
	x1 -= 2
	x1 *= 3
	x1 /= 3
	x1 %= 20

	x++ // Incremento en 1
	x-- // decremento en 1

	fmt.Println("\n--- Casting (Conversión de tipos) ---")
	// Transformación de Variable (Casting): en Go, debemos convertir manualmente para mantener los tipos seguros
	EntradaInt := 195
	EntradaFloat := 3.56

	SalidaFloat := float32(EntradaInt) // Conversión de entero a flotante
	SalidaInt := int(EntradaFloat)     // Conversión de flotante a entero

	fmt.Printf("viaje variable entera: %d Nueva variable flotante: %f\n", EntradaInt, SalidaFloat)
	fmt.Printf("viaje variable flotante: %f Nueva variable entera: %d\n", EntradaFloat, SalidaInt) // Se pierde la parte decimal

	fmt.Println("\n--- Direcciones y Punteros ---")
	// Punteros a memoria
	var punterox *int = &x // Declarar un puntero con * antes del tipo de variable
	PunteroX := &x         // Declarar un puntero con la inferencia de tipo
	fmt.Printf("Valor de x: %d valor del puntero de x: %p\n", x, PunteroX)
	fmt.Println("El puntero apunta a:", punterox)

	// =============================================================================
	// 5. ENTRADA DE DATOS (SCAN)
	// =============================================================================
	fmt.Println("\n5. ENTRADA DE DATOS (SCAN)")
	fmt.Println(strings.Repeat("=", 40))

	// Agregar un valor manualmente guardándolo en la dirección de memoria de la variable (&)
	var nombre string
	var edad int
	fmt.Print("\nIngrese su nombre (sin espacios): ")
	fmt.Scan(&nombre) // fmt.Scan detiene la lectura al encontrar un espacio
	fmt.Print("Ingrese su edad: ")
	fmt.Scan(&edad)
	fmt.Printf("Hola %s, su edad es %d años.\n", nombre, edad)

	// =============================================================================
	// 6. MÉTODOS ÚTILES PARA STRINGS
	// =============================================================================
	fmt.Println("\n6. MÉTODOS ÚTILES PARA STRINGS")
	fmt.Println(strings.Repeat("=", 40))

	miString := "cazuEla"
	fmt.Printf("\nString de ejemplo: '%s'\n", miString)
	fmt.Println("len():", len(miString), "-> Largo de mi string (en bytes)")
	fmt.Println("strings.Index():", strings.Index(miString, "z"), "-> Posición de la 'z'")
	fmt.Println("strings.ToUpper():", strings.ToUpper(miString), "-> En mayúsculas")
	fmt.Println("strings.ToLower():", strings.ToLower(miString), "-> En minúsculas")
	fmt.Println("strings.Contains():", strings.Contains(miString, "5"), "-> (Contiene el '5'?)")
	fmt.Println("strings.Count():", strings.Count(miString, "a"), "-> Veces que figura la 'a'")
	fmt.Println("strings.Replace():", strings.Replace(miString, "z", "ss", -1), "-> Reemplaza todas las 'z' por 'ss'")
	fmt.Println("strings.Repeat():", strings.Repeat(miString, 3), "-> Se repite el string 3 veces")

	fmt.Println("\n--- Despedida ---")
	linea1 := "**********************"
	linea2 := "*                    *"
	linea3 := "*       Adios!       *"
	fmt.Println(linea1)
	fmt.Println(linea2)
	fmt.Println(linea3)
	fmt.Println(linea2)
	fmt.Println(strings.Repeat("*", 22))

	// =============================================================================
	// CONCLUSIONES
	// =============================================================================
	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("CONCLUSIONES SOBRE GO BÁSICO")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Println("\n1. TIPADO ESTATICO ESTRICTO:")
	fmt.Println("   • Las variables deben declararse y no pueden cambiar de tipo.")
	fmt.Println("   • Si se declaran, DEBEN usarse, si no el código no compila.")

	fmt.Println("\n2. COLECCIONES:")
	fmt.Println("   • Arrays: Largo fijo, imposible cambiar.")
	fmt.Println("   • Slices: Tamaño dinámico, se utiliza append() para expandirlo.")
	fmt.Println("   • Structs y Maps para datos complejos y pares clave-valor respetivamente.")

	fmt.Println("\n3. PUNTEROS Y CONVERSIONES:")
	fmt.Println("   • Al pedir variables (como en fmt.Scan) se les otorga la dirección de memoria usando &.")
	fmt.Println("   • Para convertir (Casting) necesitas usar funciones directas como int() o float32(), Go no asume conversiones automáticas.")

	fmt.Println("\n=== FIN DE LA CLASE 1 ===")
}
