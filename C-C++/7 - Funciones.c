#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>

// 1. Función básica sin parámetros
void saludar() {
    printf("¡Hola, bienvenido la clase de funciones de C!\n");
}

// 2. Función con parámetros
int funcion(int x) {
    return x + 5;
}

// 3. Función con varios parámetros
int funcion2(int x, int y) {
    int z = x - y;   // Las variables locales solo existen en la función
    return z;
}

// 4. Función con múltiples valores de retorno (usamos punteros)
void calcular_estadisticas(int numeros[], int size, int* suma, float* promedio, int* maximo, int* minimo) {
    *suma = 0;
    *maximo = numeros[0];
    *minimo = numeros[0];
    
    for (int i = 0; i < size; i++) {
        *suma += numeros[i];
        if (numeros[i] > *maximo) *maximo = numeros[i];
        if (numeros[i] < *minimo) *minimo = numeros[i];
    }
    *promedio = (float)*suma / size;
}

// 5. Función que devuelve el caracter más repetido de un string
char caracter_mas_repetido(const char* cadena) {
    if (strlen(cadena) == 0) {
        return '\0';
    }
    
    int frecuencias[256] = {0}; // ASCII extendido
    
    for (int i = 0; cadena[i]; i++) {
        if (cadena[i] != ' ') {
            frecuencias[(unsigned char)cadena[i]]++;
        }
    }
    
    char max_char = '\0';
    int max_freq = 0;
    
    for (int i = 0; i < 256; i++) {
        if (frecuencias[i] > max_freq) {
            max_freq = frecuencias[i];
            max_char = (char)i;
        }
    }
    
    return max_char;
}

// 6. Función con parámetros por defecto (no existe en C, simulamos con sobrecarga)
void saludar_persona(const char* nombre) {
    printf("Hola %s!\n", nombre);
}

void saludar_persona_default() {
    saludar_persona("Invitado");
}

// 7. Función con argumentos variables (necesitamos stdarg.h)
#include <stdarg.h>
int sumar_numeros(int count, ...) {
    va_list args;
    va_start(args, count);
    int suma = 0;
    
    for (int i = 0; i < count; i++) {
        suma += va_arg(args, int);
    }
    
    va_end(args);
    return suma;
}

// 8. Función con argumentos de palabra clave variables (no existe en C puro)
// Simulamos con una estructura
typedef struct {
    const char* nombre;
    int edad;
    const char* ciudad;
} Persona;

void info_persona(Persona p) {
    if (p.nombre) printf("nombre: %s\n", p.nombre);
    if (p.edad > 0) printf("edad: %d\n", p.edad);
    if (p.ciudad) printf("ciudad: %s\n", p.ciudad);
}

// 9. Decorador para medir tiempo de ejecución (simulado con punteros a función)
typedef void (*FuncionVoid)();
typedef int (*FuncionInt)();

void medir_tiempo_void(FuncionVoid func) {
    clock_t inicio = clock();
    func();
    clock_t fin = clock();
    printf("Tiempo de ejecución: %.4f segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
}

int medir_tiempo_int(FuncionInt func) {
    clock_t inicio = clock();
    int resultado = func();
    clock_t fin = clock();
    printf("Tiempo de ejecución: %.4f segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
    return resultado;
}

// 10. Función lenta para probar el decorador
int operacion_lenta() {
    long suma = 0;
    for (long i = 0; i < 10000000; i++) {
        suma += i;
    }
    return suma;
}

// Programa principal
int main() {
    saludar(); // Invocar la función
    
    printf("Comienzo del programa %d\n", funcion(5));
    
    int valor1 = 10;
    int valor2 = 4;
    int valor3 = funcion2(valor1, valor2);
    printf("%d\n", valor3);

    int vector[] = {15, 23, 20, 11, 9, 16, 15, 22, 30, 17};
    int size = sizeof(vector) / sizeof(vector[0]);
    int suma, max_num, min_num;
    float promedio;
    
    calcular_estadisticas(vector, size, &suma, &promedio, &max_num, &min_num);
    printf("Suma: %d, Promedio: %.2f, Máximo: %d, Mínimo: %d\n", suma, promedio, max_num, min_num);

    const char* x = "Mi nombre es Máximo decimo Meridio, comandante de los ejércitos del norte, general de las legiones Félix. leal, sirviente del único emperador Marco Aurelio, padre de un hijo asesinado, esposo de una esposa asesinada. Y juro que me vengaré. en esta vida o en la otra.";
    char resultado = caracter_mas_repetido(x);
    printf("El carácter que más se repite en '%s' \nes '%c'\n", x, resultado);

    int suma_nums = sumar_numeros(3, 1, 2, 3);
    printf("La suma de (1, 2, 3) es: %d\n", suma_nums);
    
    Persona persona = {"Juan", 30, "Madrid"};
    info_persona(persona);

    // Llamada a la función con medición de tiempo
    printf("\nEjecutando operación lenta...\n");
    double res = medir_tiempo_int(operacion_lenta);
    printf("Resultado: %d\n", res);

    return 0;
}