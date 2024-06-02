import Swift
import Foundation

print("Alola mundo Swft")

/*
Los comentarios en bloque 
se hacen abriendo con slash *
y cerradn con * slash
*/


// Tipos de datos, con el signo = asignamos el valor a una variable
var x: Int = 23                                                                 // Int
var y: Double = 2.434                                                           // Double
var A: String = "Cadena 3"                                                      // String
var b: Bool = true                                                              // Bool
var list: [Any] = [1, 2, 3, "a", "b"]                                           // Array<Any> (Los arrays en Swift son genéricos, puedes usar Any para almacenar elementos de diferentes tipos)
var tuple: (Int, Int, Int, String, String) = (1, 2, 3, "a", "b")                // Tuple (Tuplas en Swift son similares a las de Python)
var dictionary: [String: Any] = ["Nombre": "Bob Esponja",
                                 "Edad": 25,
                                 "Cursos": ["Calculo", "Algebra", "Ingles"]]    // Diccionario

print("Esto es un entero:", x, type(of: x))
print("Esto es un flotante:", y, type(of: y))
print("Esto es un String: " + A, type(of: A))         // en este caso el signo + se usa para concatenas 2 string
print("Esto es un Booleano:", b, type(of: b))
print("Esto es una lista:", list, type(of: list))
print("Esto es una tupla:", tuple, type(of: tuple))
print("Esto es un diccionario:", dictionary, type(of: tuple))


// Una variable NO puede cambiar de tipo (tipado estatico)
// x = 1.35 daria un error

// Las constantes no pueden cambiar su valor
let cons = 5
var vari = 3.12 // No es neecesario especificar el tipo de variable pero si se recomienda hacerlo

// cons = 6 esto es un error
vari = 1.54
print("Variable", vari)
print("Constante:", cons)

// Función para saber si una variable pertenece a cierto tipo
print("A es un float: \(A is Float)")
print("A es un String: \(A is String)")

// Swift es Case Sensitive, diferencia mayúsculas de minúsculas
var X: String = "73"  //Variable tipo string
print("esto es x:" , x, "Esto es X: " + X)

// Forma alternativa para imprimir y/o insertar un valor numérico dentro de un string
let nombre = "Bob Esponja"
let edad = 25
print("El alumno \(nombre) tiene \(edad) años")
print("El alumno " + nombre + " tiene " + String(edad) + " años")

// Representación de miles
let millonada: Double = 6_325_412.32563215
let numberFormatter = NumberFormatter()
numberFormatter.numberStyle = .decimal
if let millonadaFormateado = numberFormatter.string(from: NSNumber(value: millonada)) {
    print("Número con separador de miles: \(millonadaFormateado)")
}

// Suma
print(6 + 5)
print(x + 33)

// Resta
print(6 - 5)
print(x - 33)

// Multiplicación
print(2.8 * 1.4)
print(y * 1.4)

// División
print(5 / 6, type(of: 5 / 6))   // Division entera
print(x / 33, type(of: x / 33))
print(2.8 / 1.4, type(of: 2.8 / 1.4)) // Division flotante
print(y / 1.4)

// Módulo
print(5 % 6, type(of: 5 % 6))
print(x % 33, type(of: x % 33))

// Como vimos el signo + cambio su función según los parámetros que entreguen
print("1 + 2 = \(1 + 2) Suma de adición")
print("'1' + '2' = \("1" + "2") Suma de concatenar")

// Operaciones Comparación
let Op1 = 23
let Op2 = 57

print("Operadores de Comparación")
print("Es \(Op1) > \(Op2)", Op1 > Op2, "Mayor estricto")
print("Es \(Op1) < \(Op2)", Op1 < Op2, "Menor estricto")
print("Es \(Op1) >= 23", Op1 >= 23, "Mayor o igual")
print("Es 44 <= \(Op2)", 44 <= Op2, "Mayor o igual")
print("Es \(Op1) == \(Op2)", Op1 == Op2, "igual a")
print("Es \(Op2) == 57", Op2 == 57)
print("Es \(Op1) != \(Op2)", Op1 != Op2, "Distinto a")
print("Es \(Op1) es entero", type(of: Op1) == Int.self, "Es: ")
print("Es \(Op1) no es entero", type(of: Op1) != Int.self, "No es: ")

// Algebra Booleana
let t = true
let f = false
let t2 = true

print("Operaciones Lógicas")
print("Valor de t", t)
print("Valor de vt", !t)             // Negación Lógica (!)
print("Valor de t ∧ f", t && f)      // Conjunción Lógica (&&)
print("Valor de t ∧ t2", t && t2)
print("Valor de t ∨ f", t || f)     // Disyunción Lógica (||)


