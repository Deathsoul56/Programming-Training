#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Función para revolver un array
void shuffle(char *array[], int n) {
    for(int i = n-1; i > 0; i--) {
        int j = rand() % (i + 1);
        char *temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

// Función para generar una permutación aleatoria
void permute(int *array, int n) {
    for(int i = n-1; i > 0; i--) {
        int j = rand() % (i + 1);
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

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

    // Bytes aleatorios 
    unsigned char aleatorio_byte[12]; // Crear un array para almacenar los bytes aleatorios

    for(int i = 0; i < 12; i++) {     // Generar 12 bytes aleatorios
        aleatorio_byte[i] = rand() % 256; // Genera un byte aleatorio (0-255)
    }

    printf("Bytes Aleatorios: "); // Imprimir los bytes aleatorios en formato hexadecimal
    for(int i = 0; i < 12; i++) {
        printf("%02x ", aleatorio_byte[i]);
    }
    printf("\n");

    // Matriz 2x3 aleatorios
    // Definir el tamaño de la matriz
    int filas = 4;
    int columnas = 3;

    int aleatorio_m[4][3]; // Crear la matriz para almacenar los valores aleatorios

    for(int i = 0; i < filas; i++) { // Generar valores aleatorios entre -10 y 10 para una matriz 4x3
        for(int j = 0; j < columnas; j++) {
            aleatorio_m[i][j] = (rand() % 21) - 10; // Genera un número entre -10 y 10
        }
    }

    // Imprimir la matriz aleatoria
    printf("Matriz aleatoria:\n");
    for(int i = 0; i < filas; i++) {
        for(int j = 0; j < columnas; j++) {
            printf("%d ", aleatorio_m[i][j]);
        }
        printf("\n");
    }


    // Definir el vector
    int vector[] = {7, -4, -3, 7, 9, 7, 0, -5, 3, 3};
    int tamano = sizeof(vector) / sizeof(vector[0]);

    // Escoger un valor al azar del vector
    int indice_aleatorio = rand() % tamano;
    int v = vector[indice_aleatorio];

    // Imprimir el vector y el valor escogido al azar
    printf("El vector v = {");
    for(int i = 0; i < tamano; i++) {
        printf("%d", vector[i]);
        if(i < tamano - 1) printf(", ");
    }
    printf("} se escoge al azar un valor %d\n", v);


    // Definir la lista de colores
    char *lista[] = {"rojo", "verde", "azul", "amarillo", "rosa", "violeta", "blanco", "negro"};
    int tamano_lista = sizeof(lista) / sizeof(lista[0]);

    // Imprimir la lista original
    printf("Lista Original = {");
    for(int i = 0; i < tamano_lista; i++) {
        printf("%s", lista[i]);
        if(i < tamano_lista - 1) printf(", ");
    }
    printf("}\n");

    // Revolver la lista
    shuffle(lista, tamano_lista);

    // Imprimir la lista revuelta
    printf("Lista revuelta = {");
    for(int i = 0; i < tamano_lista; i++) {
        printf("%s", lista[i]);
        if(i < tamano_lista - 1) printf(", ");
    }
    printf("}\n");

    // Definir la secuencia de números
    int secuencia[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int tamano_secuencia = sizeof(secuencia) / sizeof(secuencia[0]);

    // Imprimir la secuencia original
    printf("Secuencia original: {");
    for(int i = 0; i < tamano_secuencia; i++) {
        printf("%d", secuencia[i]);
        if(i < tamano_secuencia - 1) printf(", ");
    }
    printf("}\n");

    // Generar una permutación aleatoria
    permute(secuencia, tamano_secuencia);

    // Imprimir la permutación aleatoria
    printf("Permutación aleatoria: {");
    for(int i = 0; i < tamano_secuencia; i++) {
        printf("%d", secuencia[i]);
        if(i < tamano_secuencia - 1) printf(", ");
    }
    printf("}\n");



    return 0;
}
