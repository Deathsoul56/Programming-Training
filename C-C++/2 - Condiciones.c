#include <stdio.h>
#include <stdlib.h>

int main() {
    int x;
    
    // Validación de entrada
    printf("Ingrese un número entero: ");
    if (scanf("%d", &x) != 1) {
        printf("Por favor, ingrese un número entero válido.\n");
        exit(1); // Terminar Programa
    }

    printf("\n--- Condicional Simple ---\n");
    // Verificar si un número es par o impar
    if (x % 2 == 0) {                       // Si Condicion a cumplir
        printf("El numero %d es par\n", x);  // Valor si es verdadero
    } else {                                // En caso contrario
        printf("El numero %d es impar\n", x); // Valor si es falso
    }

    // Forma alternativa usando operador ternario
    printf(x % 2 == 0 ? "El numero %d es par\n" : "El numero %d es impar\n", x);

    printf("\n--- Condicional Múltiple ---\n");
    // Verificar múltiples condiciones
    if (x % 3 == 0) {                                              // Si condicion a cumplir
        printf("El valor %d es equivalente a 0 en modulo 3\n", x); // Valor si es verdadero
    } else if (x % 3 == 1) {                                      // Pero si segunda condicion
        printf("El valor %d es equivalente a 1 en modulo 3\n", x); // Valor si segunda condicion es verdadera
    } else {                                                      // En caso contrario
        printf("El valor %d es equivalente a 2 en modulo 3\n", x); // Valor si no cumple ninguna condicion
    }

    printf("\n--- Switch-Case ---\n");
    // Forma alternativa usando switch (similar a match-case en Python)
    switch (x % 3) {
        case 0:
            printf("El valor %d es equivalente a 0 en modulo 3\n", x);
            break;
        case 1:
            printf("El valor %d es equivalente a 1 en modulo 3\n", x);
            break;
        case 2:
            printf("El valor %d es equivalente a 2 en modulo 3\n", x);
            break;
    }

    printf("\n--- Condicionales Anidados ---\n");
    // If anidados
    int y = 5;

    if (x > y) {
        if (x % 2 == 0) {
            printf("x es mayor que y ademas de que x es par\n");
        } else {
            printf("x es mayor que y ademas de que x es impar\n");
        }
    } else {
        printf("x es menor o igual que y\n");
    }

    printf("\n--- Operadores Lógicos ---\n");
    // If con operadores logicos
    int z = 15;
    if (x > y && x < z) {
        printf("x es mayor que y pero menor que z\n");
    } else if (x > y && x > z) {
        printf("x es mayor que z e y\n");
    } else if (x < y && x < z) {
        printf("x es menor que z e y\n");
    } else {
        printf("ninguna condición se cumple\n");
    }

    if (x > y || x > z) {
        printf("x es mayor que y o mayor que z\n");
    }

    if (x != y) {
        printf("x no es igual a y\n");
    }

    printf("\n--- Manejo de Errores ---\n");
    // Manejo de división por cero
    int n1 = 10;
    int n2 = 3;

    printf("La división entre %d y %d\n", n1, n2);

    if (n2 != 0) {
        float resultado = (float)n1 / n2;
        if (resultado == (int)resultado) {
            printf("La division da un numero entero %.0f\n", resultado);
        } else {
            printf("La division da un numero decimal %.2f\n", resultado);
        }
        printf("No se ejecutó ningún error\n");
    } else {
        printf("No se pueden dividir números por cero\n");
    }
    
    printf("Terminó la ejecución de la secuencia\n");

    return 0;
}