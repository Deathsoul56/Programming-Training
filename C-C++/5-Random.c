#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Inicializar el generador de números aleatorios con una semilla
    srand(time(NULL)); // Usar el tiempo actual como semilla para la aleatoriedad

    // Número aleatorio entre 0 y 1
    double aleatorio = (double)rand() / RAND_MAX;
    printf("Número aleatorio entre 0 y 1: %f\n", aleatorio);

    // Número aleatorio entre -10 y 10 (intervalo cerrado-abierto)
    int min = -10;
    int max = 10;
    int aleatorio_int = min + rand() % (max - min + 1);
    printf("Número aleatorio entre -10 y 10: %d\n", aleatorio_int);

    // Vector de 10 números aleatorios entre -10 y 10
    int size = 10;
    int aleatorio_vector[size];
    printf("Vector aleatorio: ");
    for (int i = 0; i < size; i++) {
        aleatorio_vector[i] = min + rand() % (max - min + 1);
        printf("%d ", aleatorio_vector[i]);
    }
    printf("\n");

    return 0;
}
