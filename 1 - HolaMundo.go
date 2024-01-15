package main

import "fmt"

//Funcion que imprime un mensaje
func alola() string {
	return "Alola Mundo"
}

func main() {

	//Invocar la funcion
	fmt.Println(alola())

	//definir una variable tipo entero
	var x int
	fmt.Print("Ingrese el valor aqui: ")
	//Ingresar valor de forma manual
	//fmt.Scan(&x)
	x = 3

	// Condiciones
	if x%3 == 0 {
		fmt.Println("El valor es", x, "es equivalente a 0 en modulo 3")
	} else if x%3 == 1 {
		fmt.Println("El valor es", x, "es equivalente a 1 en modulo 3")
	} else if x%3 == 2 {
		fmt.Println("El valor es", x, "es equivalente a 2 en modulo 3")
	}

	//Dato tipo booleano
	var y bool = true
	fmt.Println(y, "Dato tipo booleano")

	//Dato tipo complex (puede ser 64 o 128)
	var z complex64 = complex(3.7, 4)
	fmt.Println(z, "Dato tipo complex")

	//Dato tipo float
	var a float32 = 2.3
	fmt.Println(a, "Dato tipo float")

	//Dato tipo folat64
	var b float64 = 6.651981213516
	fmt.Println(b, "Dato tipo float64")

	//Dato tipo string
	var c string = "Esto es un string"
	fmt.Println(c, "Dato tipo string")

	//Dato tipo array, todos los elementos de un array deben ser de un mismo tipo y no puede modicarse su tamaño
	var d [5]int = [5]int{10, 25, 15, 32, 51}
	fmt.Println(d, "Dato tipo Array")

	//Dato tipo slice, es similar a un array, pero su tamaño puede ser modificado dinámicamente.
	var e []int = []int{1, 2, 3, 4, 5}
	fmt.Println(e, "Dato tipo slice")
	e = append(e, 6)
	fmt.Println(e, "se agrega un valor")

	//Dato tipo Struct, representa un conjunto de campos con diferentes tipos de datos.
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

	//crear variables sin definirlas antes
	x1 := 3                  //int
	y1 := false              //boolean
	z1 := complex(5, 6)      //complejo
	a1 := 6.5                //float32
	b1 := 8.221165156        //float64
	c1 := "cadena"           //string
	d1 := [3]int{12, 27, 81} //aray
	e1 := []int{1, 2, 3}     //slice
	p2 := Persona{           //struct
		Nombre: "María",
		Edad:   25,
		Altura: 1.68,
	}

	fmt.Print(x1, y1, z1, a1, b1, c1, d1, e1, p2)

}
