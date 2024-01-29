#include <stdio.h>

//Los comentarios en C y C++ se una linea se hacen con el signo de gato #

/*
Los comentarios largos de varias lineas 
se hacen abriendo con slash *
y cerradn con * slash
*/


// Funcion Principal
main()
{
    //Imprimir un mensaje
    printf("Alola Mundo en C\n");   // La expresion \n significa un salto de linea

    //Tipos de datos

    //Declarar la Variable
    char c; // Char para un caracter o enteros pequeños

    //Asignar valor a la variable
    c = 20;

    //Declarar y asignar al mismo tiempo, para un caracter debe ser con comillas simples
    char c1 = 'C';  

    printf("Esto es un Char: %d\n", c);     // Cuando se imprime un entero se hace con %d
    printf("Esto es un Char: %c\n", c1);    // Cuando se imprime un caracter unico se hace con %c

    //Modificadores de las variables
    char unsigned c2 = 237; //Si la variable solo puede tomar valores negativos (0 a 255)
    char signed c3 = -24;   //Si la variable puede tomar valores negarivos (-128 a 127)
    printf("Char unicamente positivo: %d\n", c2);
    printf("Char que puede tomar valores negativos: %d\n", c3);
    //Si no se asigna modificador el char por defecto es signed

    int x; //Para valores enteros
    // Short es para enteros no muy grandes
    int short unsigned x1 = 35;            // 0 a 65.535
    int short signed x2 = -635;            // -32.768 a 32.767
    // Long es para enteros grandes
    int long unsigned x3 = 24516521984;    // 0 a 4.294.967.295
    int long signed x4 = -35215184519;     // -2.147.483.648 a 2.147.483.647

    printf("int corto unicamente positivo: %u\n", x1);              // Para imprimir int short unsigned es con %u
    printf("int corto con valores negativos positivo: %d\n", x2);   // Para imprimir int short signed es con %d
    printf("int largo unicamente positivo: %lu\n", x3);             // Para imprimir int long unsigned es con %lu
    printf("int largo con valores negativos positivo: %ld\n", x4);  // Para imprimir int long signed es con %lu

    float y; // Para valores decimales

    y = 3.1415;
    printf("Float: %f\n", y);

    return 0;
}
