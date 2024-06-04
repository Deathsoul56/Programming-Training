#include <stdio.h>

int main() {
    int x = 13;

    // Si condicional
    if (x % 2 == 0) {
        printf("El numero %d es par\n", x);
    } else {
        printf("El numero %d es impar\n", x);
    }

    // Forma alternativa
    printf("%d es par\n", x % 2 == 0 ? x : x);

    // Más de 1 condición
    if (x % 3 == 0) {
        printf("El valor %d es equivalente a 0 en modulo 3\n", x);
    } else if (x % 3 == 1) {
        printf("El valor %d es equivalente a 1 en modulo 3\n", x);
    } else {
        printf("El valor %d es equivalente a 2 en modulo 3\n", x);
    }

    // If anidados
    x = 10;
    int y = 5;

    if (x > y) {
        printf("x es mayor que y\n");
        if (x % 2 == 0) {
            printf("x es par\n");
        } else {
            printf("x es impar\n");
        }
    } else {
        printf("x es menor o igual que y\n");
    }

    // If con operadores logicos
    x = 10;
    y = 5;
    int z = 15;

    if (x > y && x < z) {
        printf("x es mayor que y y menor que z\n");
    } else if (x < y || x < z) {
        printf("x es menor que o menor que z\n");
    } else {
        printf("ninguna condición se cumple\n");
    }

    int mes;

    printf("Ingresa un numero de mes (1-12): ");
    scanf("%d", &mes);

    switch (mes) {
        case 1:
            printf("Enero\n");
            break;
        case 2:
            printf("Febrero\n");
            break;
        case 3:
            printf("Marzo\n");
            break;
        case 4:
            printf("Abril\n");
            break;
        case 5:
            printf("Mayo\n");
            break;
        case 6:
            printf("Junio\n");
            break;
        case 7:
            printf("Julio\n");
            break;
        case 8:
            printf("Agosto\n");
            break;
        case 9:
            printf("Septiembre\n");
            break;
        case 10:
            printf("Octubre\n");
            break;
        case 11:
            printf("Noviembre\n");
            break;
        case 12:
            printf("Diciembre\n");
            break;
        default:
            printf("Numero de mes invalido\n");
            break;
    }

    return 0;
}