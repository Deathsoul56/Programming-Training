#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Función para imprimir un arreglo de enteros
void print_int_array(int arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

// Función para imprimir un arreglo de floats
void print_float_array(float arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%.4f", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

// Función para imprimir un arreglo de strings
void print_string_array(char *arr[], int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("\"%s\"", arr[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");
}

// Función para ordenar un arreglo de enteros (usando Bubble Sort)
void sort_int_array(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Función para ordenar un arreglo de strings (usando Bubble Sort)
void sort_string_array(char *arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (strcmp(arr[j], arr[j + 1]) > 0) {
                char *temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Función para buscar un elemento en un arreglo de enteros
int search_int_array(int arr[], int size, int value) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == value) return 1;
    }
    return 0;
}

// Función para convertir strings a mayúsculas
void to_upper_string_array(char *arr[], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; arr[i][j]; j++) {
            arr[i][j] = toupper(arr[i][j]);
        }
    }
}

// Función para imprimir una matriz de enteros
void print_int_matrix(int rows, int cols, int matrix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        printf("[");
        for (int j = 0; j < cols; j++) {
            printf("%d", matrix[i][j]);
            if (j < cols - 1) printf(", ");
        }
        printf("]\n");
    }
}

// Función para imprimir una matriz de strings
void print_string_matrix(int rows, int cols, char *matrix[rows][cols]) {
    for (int i = 0; i < rows; i++) {
        printf("[");
        for (int j = 0; j < cols; j++) {
            printf("\"%s\"", matrix[i][j]);
            if (j < cols - 1) printf(", ");
        }
        printf("]\n");
    }
}

int main() {
    printf("Los arreglos son estructuras de datos que permiten almacenar múltiples valores del mismo tipo.\n");

    // Creación de arreglos
    printf("\n--- Creacion de arreglos ---\n");
    
    int numerico[] = {3, 6, 8, 3, 13, 63, 17, 56, 234, 21, 73, 13, 8, 37, 64, 10, 15};
    int numerico_size = sizeof(numerico) / sizeof(numerico[0]);
    printf("Arreglo numerico: ");
    print_int_array(numerico, numerico_size);

    float flotante[] = {3.1415, 2.7154, 8.2326};
    int flotante_size = sizeof(flotante) / sizeof(flotante[0]);
    printf("Arreglo flotante: ");
    print_float_array(flotante, flotante_size);

    char *string[] = {"Rojo", "Verde", "Azul", "Negro", "Blanco", "Cafe"};
    int string_size = sizeof(string) / sizeof(string[0]);
    printf("Arreglo de strings: ");
    print_string_array(string, string_size);

    // En C no podemos mezclar tipos en un arreglo como en Python
    printf("\nNota: En C no podemos mezclar tipos en un arreglo como en Python\n");

    // Otras formas de crear arreglos
    printf("\n--- Otras formas de crear arreglos ---\n");
    
    float zeros[5] = {0};
    printf("Arreglo de ceros: ");
    print_float_array(zeros, 5);

    float ones[5];
    for (int i = 0; i < 5; i++) ones[i] = 1.0;
    printf("Arreglo de unos: ");
    print_float_array(ones, 5);

    int full[5];
    for (int i = 0; i < 5; i++) full[i] = 7;
    printf("Arreglo lleno de 7 con 5 elementos: ");
    print_int_array(full, 5);

    // Ordenar arreglos
    printf("\n--- Ordenar arreglos ---\n");
    
    printf("Arreglo original: ");
    print_int_array(numerico, numerico_size);
    sort_int_array(numerico, numerico_size);
    printf("Arreglo ordenado: ");
    print_int_array(numerico, numerico_size);

    printf("Arreglo de cadenas original: ");
    print_string_array(string, string_size);
    sort_string_array(string, string_size);
    printf("Arreglo de cadenas ordenado: ");
    print_string_array(string, string_size);

    // Indexación y slicing
    printf("\n--- Indexación y slicing ---\n");
    
    printf("Elemento en la posición 2: %d\n", numerico[2]);

    printf("Subarreglo de la posición 2 a la 6: [");
    for (int i = 2; i < 6 && i < numerico_size; i++) {
        printf("%d", numerico[i]);
        if (i < 5) printf(", ");
    }
    printf("]\n");

    // Agregar y quitar datos (en C los arreglos tienen tamaño fijo)
    printf("\nNota: En C los arreglos tienen tamaño fijo, no se pueden agregar/quitar elementos dinámicamente\n");

    // Convertir array de chars a string
    printf("\n--- Convertir array de chars a string ---\n");
    char saludo[] = {'h', 'o', 'l', 'a', '\0'};
    printf("Cadena concatenada: %s\n", saludo);

    // Buscar un elemento en el arreglo
    printf("\n--- Buscar un elemento en el arreglo ---\n");
    if (search_int_array(numerico, numerico_size, 13)) {
        printf("El número 13 está en el arreglo.\n");
    } else {
        printf("El número 13 no está en el arreglo.\n");
    }

    // Convertir a mayúsculas
    printf("\n--- Convertir a mayúsculas ---\n");
    printf("Arreglo de cadenas original: ");
    print_string_array(string, string_size);
    to_upper_string_array(string, string_size);
    printf("Arreglo de cadenas en mayúsculas: ");
    print_string_array(string, string_size);

    // Operaciones matemáticas
    printf("\n--- Operaciones matemáticas ---\n");
    int a[] = {10, 3, 11, 2, 5};
    int b[] = {3, 8, 6, 2, 7};
    int size = sizeof(a) / sizeof(a[0]);
    
    printf("Suma de arreglos: [");
    for (int i = 0; i < size; i++) {
        printf("%d", a[i] + b[i]);
        if (i < size - 1) printf(", ");
    }
    printf("]\n");

    // Funciones estadísticas básicas
    printf("\n--- Funciones estadísticas ---\n");
    int sum = 0;
    for (int i = 0; i < numerico_size; i++) sum += numerico[i];
    printf("Suma de los elementos del arreglo: %d\n", sum);

    // Matrices
    printf("\n--- Introducción a las matrices ---\n");
    printf("Una matriz es una estructura de datos bidimensional que contiene elementos organizados en filas y columnas.\n");

    // Creación de matrices numéricas
    printf("\n--- Creación de matrices numéricas ---\n");
    int matriz_numerica[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    printf("Matriz numérica:\n");
    print_int_matrix(3, 3, matriz_numerica);

    // Creación de matrices de cadenas
    printf("\n--- Creación de matrices de cadenas ---\n");
    char *matriz_cadenas[3][3] = {
        {"Rojo", "Verde", "Azul"},
        {"Negro", "Blanco", "Cafe"},
        {"Amarillo", "Morado", "Rosa"}
    };
    printf("Matriz de cadenas:\n");
    print_string_matrix(3, 3, matriz_cadenas);

    // Acceso a elementos de una matriz
    printf("\n--- Acceso a elementos de una matriz ---\n");
    printf("Elemento en la fila 1, columna 2 de la matriz numérica: %d\n", matriz_numerica[1][2]);
    printf("Elemento en la fila 0, columna 1 de la matriz de cadenas: %s\n", matriz_cadenas[0][1]);

    return 0;
}