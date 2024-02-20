//go:build ignore
// +build ignore

package main

// Importar las librerias
import (
	"fmt"     // Libreria con metodos escenciales
	"reflect" // Libreria para comprar el tipo de dato
	"strings" // Librerias para metodos de string
)

//Los comentarios en Go se una linea se hacen con doble Slash

/*
Los comentarios largos de varias lineas
se hacen abriendo con slash *
y cerradn con * slash
*/

func main() {

	//Imprimir un mensaje
	fmt.Println("Alola Mundo Go!")

	// Tipos de Datos en Go (Fuertemente Tipado) Las variable deben ser usadas o el programa no compilara
	// Para definir una variable se debe indicar con var y despues el tipo de esta
	var x int // Int por defecto es de 32 bits, puede ser de 8, 16, 32 y 64 bits
	x = 14    // Se asigna el valor de esta con el signo =

	// Se puede declar y asigna valor al mismo tiempo
	var y1 float32 = 2.3                          // Float de 32 bits
	var y2 float64 = 6.651981213516               // Float de 64 bits
	var z1 complex64 = complex(3.7, 4)            // Complejo de 64 bits
	var z2 complex128 = complex(2.2165, 6.126541) // Complejo de 128 bits
	var b bool = true                             // Boleano
	var s string = "Esto es un string"            // String
	var v byte = 'Ñ'                              // Byte

	// Imprimir los datos
	fmt.Println(x, "De tipo Entero")
	fmt.Println(y1, "Dato tipo float")
	fmt.Println(y2, "Dato tipo float64")
	fmt.Println(z1, "Dato tipo complex 32 bits")
	fmt.Println(z2, "Dato tipo complex 64 bits")
	fmt.Println(b, "Dato tipo booleano")
	fmt.Println(s, "Dato tipo string")
	fmt.Println(v, "Dato tipo byte") // Imprime el carácter correspondiente al valor ASCII

	// Array, todos los elementos de un array deben ser de un mismo tipo y no puede modicarse su tamaño
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

	// Las variables se pueden definir sin especificar (inferiere tipo de dato) el tipo con :=
	Entero := 3                   //int
	Flotante := 6.515434          //float32
	Complejo := complex(5, 6)     //complejo
	Booleano := false             //boolean
	Cadena := "cadena"            //string
	Arreglo := [3]int{12, 27, 81} //aray
	Corte := []int{1, 2, 3}       //slice
	Estructura := Persona{        //struct
		Nombre: "María",
		Edad:   25,
		Altura: 1.68,
	}

	fmt.Println(Entero, Flotante, Complejo, Booleano, Cadena, Arreglo, Corte, Estructura)

	var x8 int8 = -8 // Entero de 8 bits
	var ux8 uint = 8 // Entero positivo, los otros datos numericos tambien pueden ser solo positivo

	// Forma alternativa de imprimir
	fmt.Println("Entero pequeño:", x8, "entero no negativo:", ux8)      // Puede imprimir separando los elemetos con comas
	fmt.Printf("Entero pequeño: %d entero no negativo: %d \n", x8, ux8) // puedo imprimir escribiendo todo el texto y especificando el tipo de variable

	// Varialbe tipo Mapa
	mapa := make(map[string]int) // Crear un mapa vacio

	// Asignar valores al mapa
	mapa["Primer Valor"] = 10
	mapa["Segundo Valor"] = 27
	mapa["Tercer Valor"] = 13

	fmt.Println("Mapa completo:", mapa) // Imprimir el mapa completo

	// Una variable NO puede cambiar de tipo (tipado estatido)
	// Go es Case Sensitive, distinge entre mayusculas y minusculas
	m := 133
	M := "Alola 654"
	fmt.Printf("Valor de m = %d distinto al el valor de M = %s\n", m, M)

	// Constante, son variable que no puede cambiar su valor, estas puede no ser usada y el programa aun asi funcionara
	const C = "Valor de una constante"
	const Pi = 3.141592

	// Función para saber si una variable pertenece a cierto tipo
	A := 3.14
	fmt.Println("A es un float:", reflect.TypeOf(A).Kind() == reflect.Float64)
	fmt.Println("A es un string:", reflect.TypeOf(A).Kind() == reflect.String)

	// Operaciones en Go
	/* Si se operan variable de distinto bits el resultado tendra la cantidad de bits mayor (int8 + int16 = int16)
	No se puede operar variables de distinto tipo, para eso deberemos transformarlas para que tengan el mismo tipo
	*/

	fmt.Println("Operaciones Aritmeticas")
	entero1 := 23
	entero2 := 14

	fmt.Printf("Suma: %d + %d = %d\n", entero1, entero2, entero1+entero2)           // Suma
	fmt.Printf("Resta: %d - %d = %d\n", entero1, entero2, entero1-entero2)          // Resta
	fmt.Printf("Multiplicacion: %d * %d = %d\n", entero1, entero2, entero1*entero2) // Multiplicacion
	fmt.Printf("Divison Entera: %d / %d = %d\n", entero1, entero2, entero1/entero2) // Division, Como el resultado es entero la division no muestra todo el resultado

	flotante1 := float32(entero1)
	flotante2 := float32(entero2)
	fmt.Printf("Division: %f / %f = %f\n", float32(entero1), float32(entero2), flotante1/flotante2) // Para tener todo el resultado debemos transformas a float

	fmt.Printf("Modulo: %d %% %d = %d\n", entero1, entero2, entero1%entero2) // Modulo (Para imrpimir % en printf se hace con %%)

	// Operadores de Comparación
	Op1 := 23
	Op2 := 57

	fmt.Println("Operadores de Comparación")
	fmt.Printf("¿Es %d > %d? %t Mayor estricto\n", Op1, Op2, Op1 > Op2)
	fmt.Printf("¿Es %d < %d? %t Menor estricto\n", Op1, Op2, Op1 < Op2)
	fmt.Printf("¿Es %d >= 23? %t Mayor o igual\n", Op1, Op1 >= 23)
	fmt.Printf("¿Es 44 <= %d? %t Menor o igual\n", Op2, 44 <= Op2)
	fmt.Printf("¿Es %d == %d? %t Igual a\n", Op1, Op2, Op1 == Op2)
	fmt.Printf("¿Es %d == 57? %t\n", Op2, Op2 == 57)
	fmt.Printf("¿Es %d != %d? %t Distinto a\n", Op1, Op2, Op1 != Op2)

	// Operaciones Lógicas
	fmt.Println("Algebra Booleano")
	t := true
	f := false
	t2 := true

	fmt.Println("Operaciones Lógicas")
	fmt.Println("Valor de t:", t)
	fmt.Println("Valor de ~t:", !t)        // Negación Lógica (!)
	fmt.Println("Valor de t ∧ f:", t && f) // Conjunción Lógica (y)
	fmt.Println("Valor de t ∧ t2:", t && t2)
	fmt.Println("Valor de t ∨ f:", t || f) // Disyunción Lógica (o)

	// Atajo de operaciones
	x1 := 14
	x1 = x + 2 // se asigna el mismo valor + 2
	x1 += 2    // Atajo de la operaciones anterior
	fmt.Println(x1)

	// Todas las operaciones basicas tienen su atajo
	x1 -= 2
	x1 *= 3
	x1 /= 3
	x1 %= 20

	x++ // Incremento en 1
	x-- // decremento en 1

	// Transformacion de Variable (Casting), como Go es fuertemente tipado para cambiar el tipo de variable debe ser en una nueva variable
	EntradaInt := 195
	EntradaFloat := 3.56

	SalidaFloat := float32(EntradaInt) // Conversion de entero a flotante
	SalidaInt := int(EntradaFloat)     // Conversion de flotante a entero

	fmt.Printf("viaje variable entera: %d Nueva variable flotante: %f\n", EntradaInt, SalidaFloat)
	fmt.Printf("viaje variable flotante: %f Nueva variable entera: %d\n", EntradaFloat, SalidaInt) // Se pierde toda la parte decimal

	// Punteros a memoria
	var punterox *int = &x // Declarar un puntero con * antes del tipo de variable
	PunteroX := &x         // Declarar un puntero con la inferencia de tipo
	fmt.Printf("Valor de x: %d valor del puntero de x: %p\n", x, PunteroX)
	fmt.Println(punterox)

	// Agregar un valor manualmente
	var nombre string
	var edad int
	fmt.Print("Ingrese su nombre: ") // Go tiene problema leyendo espacios
	fmt.Scan(&nombre)
	fmt.Print("Ingrese su edad: ")
	fmt.Scan(&edad)
	fmt.Printf("Hola %s su edad es %d años", nombre, edad)

	// Metodos para Strings
	miString := "cazuEla"
	fmt.Println(len(miString), "Largo de mi string")
	fmt.Println(strings.Index(miString, "z"), "Posición de la z en mi string, si se repiten se devuelve la menor posición")
	fmt.Println(strings.ToUpper(miString), "Todo el string en mayúsculas")
	fmt.Println(strings.ToLower(miString), "Todo el string en minúsculas")
	fmt.Println(strings.Contains(miString, "5"), "Devuelve verdadero si es un número, falso en caso contrario")
	fmt.Println(strings.Count(miString, "a"), "Cuenta todas las 'a' que contiene")
	fmt.Println(strings.Replace(miString, "z", "ss", -1), "Reemplaza todas las 'z' por 'ss'")
	fmt.Println(strings.Repeat(miString, 3), "Se imprime el string 3 veces")

	linea1 := "**********************"
	linea2 := "*                    *"
	linea3 := "*       Adios!       *"
	fmt.Println(linea1)
	fmt.Println(linea2)
	fmt.Println(linea3)
	fmt.Println(linea2)
	fmt.Println(strings.Repeat("*", 22))

}
