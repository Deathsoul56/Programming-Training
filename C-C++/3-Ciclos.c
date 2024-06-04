#include <stdio.h>

// Ciclos
int main() {

    // Tipo While
    int x = -3;
    while (x <= 10) {
        printf("Valor de x = %d\n", x);
        x++;
    }

    int y = 0;
    while (1) {     //  while infinito
        y++;
        if (y == 5) {
            printf("Se rompio el ciclo\n");
            break; // Romper el ciclo
        } else {
            printf("Ciclo infinito\n");
        }
    }


    // Ciclos for
    // Avanzar por un rango
    for (int i = 0; i <= 5; i++) { // Imprime de 0 hasta 5 el intervalor es semi cerrado [0, 5]
        printf("Valor de i = %d\n", i);
    }

    for (int j = -5; j < 7; j++) { // Imprime de -5 hasta 7 el intervalor es semi cerrado [-5, 7)
        printf("Valor de j = %d\n", j);
    }

    // Avanzar por una lista
    // Declarar un array en C
    char *list[] = {"a", "c", "7", "3.1415", "True", "lamda"};
    int length = sizeof(list) / sizeof(list[0]);

    for (int i = 0; i < length; i++) {
        printf("en elemento %d de la lista es = %s de tipo =  %s\n", i, list[i], "char *");
    }

    //  Ciclos Anidados
    int numeros[] = {1, 2, 3};
    char letras[] = {'a', 'b', 'c'};
    int num_length = sizeof(numeros) / sizeof(numeros[0]);
    int letra_length = sizeof(letras) / sizeof(letras[0]);

    for (int i = 0; i < num_length; i++) {
        for (int j = 0; j < letra_length; j++) {
            printf("%d %c\n", numeros[i], letras[j]);
        }
    }


    // Recorrer una matriz
    int matriz[2][4] = {{4, 7, 9, 3}, {2, 4, 6, 1}};

    printf("La matriz original:\n");
    for (int i = 0; i < 2; i++) {
        printf("Valor %d es: ", i);
        for (int j = 0; j < 4; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}
