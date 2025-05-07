#include <stdio.h>

//Los comentarios en C y C++ se una linea se hacen con doble Slash

/*
Los comentarios largos de varias lineas 
se hacen abriendo con slash *
y cerradn con * slash
*/


// Definir constantes Globales
# define val 10
# define floatVal 4.5
# define charVal 'G' // Comillas simples
# define stringVal "ABC Global" // Comillas dobles

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

    float y; // Para valores decimales usa 4 bits en memoria
    y = 3.141592; //−3.40 × 10^38 a  3.40 × 10^38
    printf("Punto flotante: %f\n", y); //  Para imprimir float es con %lu

    double d; // Para valores con muchos digitos usa 8 bits en memoria
    d = 119515613.926535; // −1.79 × 10^308 a 1.79 × 10^308
    double long d1 = 7984238451891.151619;// −1.18 × 10^4932 a 1.18 × 10^4932

    printf("Double para numeros con muchos digitos: %lf\n", d);
    printf("Double largo para mas precision: %Lf\n", d1);

    // Cadenas de caracteres
    char nombre[] = "Bob Esponja"; // Como definir un caracter pero con []
    printf("El nombre es: %s\n", nombre); // Para imprimir un string se usa %s


    // Constantes (No pueden cambiar su valor)
    // Locales, solo se pueden usar dentro de una misma funcion
    const int constanteint = 10;
    const float constantefloat = 4.5;
    const char constantechar = 'G';
    const char constantestring [10] = "ABC Local";

    printf("Constante Local entera: %d\n", constanteint);
    printf("Constante Local entera: %f\n", constantefloat);
    printf("Constante Local entera: %c\n", constantechar);
    printf("Constante Local entera: %s\n", constantestring);

    // Globales, todas las funcion tiene acceso a ellas, se definen afuera del programa
    printf("Constante Global entera: %d\n", val);
    printf("Constante Global entera: %f\n", floatVal);
    printf("Constante Global entera: %c\n", charVal);
    printf("Constante Global entera: %s\n", stringVal);


    // Operadores Logicos
    printf("Operadores Logicos");
    int Op1 = 23;
    int Op2 = 57;

    printf("Es %d > %d: %d (Mayor estricto)\n", Op1, Op2, Op1 > Op2);           // Mayor estricto
    printf("Es %d < %d: %d (Menor estricto)\n", Op1, Op2, Op1 < Op2);           // Menor estricto
    printf("Es %d >= 23: %d (Mayor o igual)\n", Op1, Op1 >= 23);                // Mayor o igual
    printf("Es 44 <= %d: %d (Mayor o igual)\n", Op2, 44 <= Op2);                // Mayor o igual
    printf("Es %d igual a %d: %d (Igual a)\n", Op1, Op2, Op1 == Op2);           // Igual a
    printf("Es %d igual a 57: %d (Igual a)\n", Op2, Op2 == 57);                 // Igual a
    printf("Es %d distinto a %d: %d (Distinto a)\n", Op1, Op2, Op1 != Op2);     // Distinto a


    // Cambio de tipo de variable 
    /*en C las varibles se definen con si tipo y no se pueden cambiar
    pero si se pueden crear otra variable con el mismo valor pero de otro tipo  */

    int entero = 42;
    float flotante = entero;  // Conversión implícita de int a float
    printf("Entero original %d flotante nuevo %f\n", entero, flotante);

    float flotante2 = 3.74;
    int entero2 = (int)flotante2;  // Conversión explícita de float a int
    printf("Flotante original %f Entero nuevo %d\n", flotante2, entero2); //Pierdo toda la parte decimal

    int numero = 424123;
    char cadena[20];  // Tamaño suficiente para almacenar el número como cadena

    // Utilizando sprintf para convertir el número a un String
    sprintf(cadena, "%d", numero);

    printf("La cadena es: %s\n", cadena); // Imprimiendo la cadena resultante

    // Operaciones Basicas
    x = 23;
    y = 2.434;

    // Suma
    printf("5 + 6 es: %d\n", 5 + 6); // Int + Int = Int
    printf("33 + %d es: %d\n", x, 33 + x);
    printf("%d + %f es: %f\n", x, y, x + y); // Int + Float = Float
    printf("2.8 + 1.4 es: %f\n", 2.8 + 1.4); // Float + Float = Float

    // Resta
    printf("5 - 6 es: %d\n", 5 - 6); // Int - Int = Int
    printf("33 - %d es: %d\n", x, 33 - x);
    printf("%d - %f es: %f\n", x, y, x - y); // Int - Float = Float
    printf("2.8 - 1.4 es: %f\n", 2.8 - 1.4); // Float - Float = Float

    // Multiplicacion
    printf("5 * 6 es: %d\n", 5 * 6); // Int * Int = Int
    printf("33 * %d es: %d\n", x, 33 * x);
    printf("%d * %f es: %f\n", x, y, x * y); // Int * Float = Float
    printf("2.8 * 1.4 es: %f\n", 2.8 * 1.4); // Float * Float = Float

    // Division
    printf("5 / 6 es: %d\n", 5 / 6); // hay que tener cuidado con las divisiones
    printf("(Int) 33 / %d es: %d\n", x, 33 / x);            // Es importante como defina el resultado
    printf("(float) 33 / %d es: %f\n", x, (float)33 / x); 
    printf("%d / %f es: %f\n", x, y, x / y); // Int / Float = Float
    printf("2.8 / 1.4 es: %f\n", 2.8 / 1.4); // Float / Float = Float

    char linea1[] = "**********************";
    char linea2[] = "*                    *";
    char linea3[] = "*       Adios!       *";
    
    printf("%s\n", linea1);
    printf("%s\n", linea2);
    printf("%s\n", linea3);
    printf("%s\n", linea2);
    printf("%s\n", linea1);

    return 0; // Todo programa en C debe devolver algun valor a menos que se especifique que no devuelve nada
}