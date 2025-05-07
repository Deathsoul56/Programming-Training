#include <stdio.h>
#include <stdlib.h>

// Ciclos
int main() {
    printf("\n--- Ciclo While ---\n");
    // Tipo While
    int x = -3;
    while (x <= 10) { // Ciclo while que imprime valores de x desde -3 hasta 10
        printf("Valor de x = %d\n", x);
        x++;
    }

    int y = 0;
    while (1) { // while infinito
        y++;
        if (y == 5) {
            printf("Se rompio el ciclo\n");
            break; // Romper el ciclo
        } else {
            printf("Ciclo infinito\n");
        }
    }

    printf("\n--- Ciclo For ---\n");
    // Ciclos for

    // Avanzar por un rango
    for (int i = 0; i <= 5; i++) { // Ciclo for imprime de 0 hasta 5
        printf("Valor de i = %02d\n", i); // Formatea el número con dos dígitos
    }

    for (int j = -5; j < 7; j++) { // Imprime de -5 hasta 7 el intervalo es semi cerrado [-5, 7)
        printf("Valor de j = %d\n", j);
    }

    // Avanzar por una lista
    char *mi_lista[] = {"a", "c", "7", "3.1415", "True", "lambda"};
    int length = sizeof(mi_lista) / sizeof(mi_lista[0]);

    // Simulando enumerate de Python
    for (int i = 0; i < length; i++) {
        printf("El elemento %d de la lista es = %s\n", i, mi_lista[i]);
    }

    // Verificar múltiples valores en una lista
    int numeros[] = {10, 15, 20, 25, 30};
    int num_length = sizeof(numeros) / sizeof(numeros[0]);
    
    for (int i = 0; i < num_length; i++) {
        if (numeros[i] % 2 == 0) {
            printf("%d es par\n", numeros[i]);
        } else {
            printf("%d es impar\n", numeros[i]);
        }
    }

    // Ciclos con continue
    for (int i = 0; i < 10; i++) {
        if (i % 2 == 0) {
            continue; // Saltar números pares
        }
        printf("Número impar: %d\n", i);
    }

    // Ciclos con manejo de errores
    for (int i = -1; i < 5; i++) {
        if (i == 0) {
            printf("Error: No se puede dividir 10 entre %d (división por cero).\n", i);
            continue;
        }
        printf("10 / %d: %.2f\n", i, 10.0 / i);
    }

    printf("\n--- Ciclos Anidados ---\n");
    // Ciclos Anidados
    int nums[] = {1, 2, 3};
    char letras[] = {'a', 'b', 'c'};
    int nums_length = sizeof(nums) / sizeof(nums[0]);
    int letras_length = sizeof(letras) / sizeof(letras[0]);

    for (int i = 0; i < nums_length; i++) {
        for (int j = 0; j < letras_length; j++) {
            printf("%d %c\n", nums[i], letras[j]);
        }
    }

    // Recorrer una matriz
    int matriz[2][4] = {{4, 7, 9, 3}, {2, 4, 6, 1}};
    printf("\nLa matriz original:\n");
    
    // Versión más descriptiva del recorrido de matriz
    for (int fila_idx = 0; fila_idx < 2; fila_idx++) {
        printf("Fila %d: ", fila_idx);
        for (int columna_idx = 0; columna_idx < 4; columna_idx++) {
            printf("%d ", matriz[fila_idx][columna_idx]);
        }
        printf("\n");
        // Mostrar valores individuales con formato similar a Python
        for (int columna_idx = 0; columna_idx < 4; columna_idx++) {
            printf("  Columna %d: %d\n", columna_idx, matriz[fila_idx][columna_idx]);
        }
    }

    return 0;
}