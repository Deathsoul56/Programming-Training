#include <stdio.h>
#include <math.h>
#include <float.h>
#include <complex.h>

int main() {
    // Números especiales
    double Pi = M_PI;           // Valor de pi 3.141592653589793
    double e = M_E;             // Valor de e 2.718281828459045
    double inf = INFINITY;      // Infinito Positivo
    double minf = -INFINITY;    // Infinito Negativo
    double NoNumero = NAN;      // No es un número (Not a number)

    printf("Valor de Pi: %f, Valor de e: %f\n", Pi, e);
    printf("Infinito positivo: %f, infinito negativo: %f\n", inf, minf);
    printf("No es un numero: %f\n", NoNumero);

     // Definir algunos valores
    int x = 24;
    double y = 17.4;
    double complex z = 3.0 + 4.0 * I;

    // Operaciones
    printf("%d + %.2f = %.2f\n", x, y, x + y);                 // Suma
    printf("%d - %.2f = %.2f\n", x, y, x - y);                 // Resta
    printf("%d * %.2f = %.2f\n", x, y, x * y);                 // Multiplicación
    printf("%d / %.2f = %.2f\n", x, y, x / y);                 // División
    printf("%d // 9 = %d\n", x, x / 9);                        // División entera
    printf("%d %% 9 = %d\n", x, x % 9);                        // Módulo
    printf("√%d = %.2f\n", x, sqrt(x));                        // Raíz Cuadrada
    printf("%d^3 = %d\n", x, (int)pow(x, 3));                  // Potencia
    printf("%d^3 = %.2f\n", x, pow(x, 3));                     // Potencia con math.h
    printf("3√%d = %.2f\n", x, pow(x, 1.0 / 3.0));             // Raíz N-ésima con math.h
    printf("|-%.2f| = %.2f\n", -y, fabs(-y));                  // Valor absoluto
    printf("Re(%f + %fi) = %.2f\n", creal(z), cimag(z), creal(z));  // Parte Real
    printf("Im(%f + %fi) = %.2f\n", creal(z), cimag(z), cimag(z));  // Parte Imaginaria
    printf("|%f + %fi| = %.2f\n", creal(z), cimag(z), cabs(z));     // Módulo Número complejo
    printf("Arg(%f + %fi) = %.2f\n", creal(z), cimag(z), carg(z));  // Argumento de un complejo
    printf("(%f + %fi)* = %f + %fi\n", creal(z), cimag(z), creal(conj(z)), cimag(conj(z)));  // Conjugado

    // Funciones matematicas
    printf("e^2 = %f\n", exp(2));                  // Funciones exponencial
    printf("Ln(%f) = %f\n", x, log(x));            // Logaritmo Natural
    printf("Log_7(%f) = %f\n", x, log(x)/log(7));  // Logaritmo cualquier base
    printf("floor(%f) = %f\n", y, floor(y));       // Funciones Piso
    printf("Ceil(%f) = %f\n", y, ceil(y));         // Funciones Cielo
    printf("√(5^2+12^2) = %f\n", hypot(5, 12));    // Hipotenusa

    // Funciones Trigonometricas (Por defecto estan en Radianes)
    printf("sin(Pi/6) = %f\n", sin(Pi / 6));        // Función Seno
    printf("cos(Pi/6) = %f\n", cos(Pi / 6));        // Función Coseno
    printf("tan(Pi/6) = %f\n", tan(Pi / 6));        // Función Tangente
    printf("sec(Pi/6) = %f\n", 1.0 / cos(Pi / 6));  // Función Secante
    printf("csc(Pi/6) = %f\n", 1.0 / sin(Pi / 6));  // Función Cosecante
    printf("cot(Pi/6) = %f\n", 1.0 / tan(Pi / 6));  // Función Cotangente

    // Funciones Trigonometricas Inversas
    double value = 0.5;

    printf("Arcoseno(%f) = %f\n", value, asin(value) * 180 / Pi);   // Arcoseno en grados
    printf("Arcocoseno(%f) = %f\n", value, acos(value) * 180 / Pi); // Arcocoseno en grados
    printf("Arcotangente(%u) = %f\n", 1, atan(1) * 180 / Pi); // Arcotangente en grados

    // Funciones Hiporbolicas
    double xh = 3.0;

    printf("sinh(3) = %f\n", sinh(xh));          // Función Seno Hiperbólico
    printf("cosh(3) = %f\n", cosh(xh));          // Función Coseno Hiperbólico
    printf("tanh(3) = %f\n", tanh(xh));          // Función Tangente Hiperbólica
    printf("sech(3) = %f\n", 1.0 / cosh(xh));    // Función Secante Hiperbólica
    printf("csch(3) = %f\n", 1.0 / sinh(xh));    // Función Cosecante Hiperbólica
    printf("coth(3) = %f\n", 1.0 / tanh(xh));    // Función Cotangente Hiperbólica


    return 0;
}
