#include <stdio.h>

int factorial(double n) {
   if (n == 0 || n == 1) {
       return 1;
   } else {
       return n * factorial(n - 1);
   }
}

int fibonacci(double n) {
   if (n == 1 || n == 2) {
       return 1;
   } else {
       return fibonacci(n - 1) + fibonacci(n - 2);
   }
}

int main() {
   for (double i = 0; i <= 10; i++) {
       printf("%lf! = %d\n", i, factorial(i));
   }

   for (double i = 1; i <= 46; i++) {
       printf("fibonacci_%lf = %d\n", i, fibonacci(i));
   }

   return 0;
}