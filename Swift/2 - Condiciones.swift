import Swift
import Foundation

let x = 13

// If simple
if x % 2 == 0 {
    print("El numero \(x) es par")
} else {
    print("El numero \(x) es impar")
}

// Forma alternativa
print(x % 2 == 0 ? "\(x) es par" : "\(x) es impar")

// Mas de 1 condicion
if x % 3 == 0 {
    print("El valor \(x) es equivalente a 0 en modulo 3")
} else if x % 3 == 1 {
    print("El valor \(x) es equivalente a 1 en modulo 3")
} else {
    print("El valor \(x) es equivalente a 2 en modulo 3")
}

// If anidados
let y = 5
if x > y {
    print("x es mayor que y")
    if x % 2 == 0 {
        print("x es par")
    } else {
        print("x es impar")
    }
} else {
    print("x es menor o igual que y")
}

// If con operadores lógicos
let z = 15
if x > y && x < z {
    print("x es mayor que y pero menor que z")
} else if x > y && x > z {
    print("x es mayor que z e y")
} else if x < y && x < z {
    print("x es menor que z e y")
} else {
    print("ninguna condición se cumple")
}


// Condicion de Intentar
let n1 = 10
let n2 = 3

print("La división entre \(n1) y \(n2)")

do {
    let resultado = try n1 / n2
    if Double(resultado) == Double(Int(resultado)) {
        print("La división da un número entero", resultado)
    } else {
        print("La división da un número decimal", resultado)
    }
} catch {
    print("No se pueden dividir números por cero")
} 
