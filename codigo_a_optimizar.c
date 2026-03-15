#include <stdio.h>

// c_no_opt.c v1.1.1
// version: 1.2.0
// Autor: Alegria ponce jose santiago
//Eliminacion de librerias no necesarias, elimine un else al final que era redundante y al ultimo if y prints reduje operadores
// declare variables a otro tipo (long long)
#include <stdio.h>

int main() {
    int N = 1000;
    int i, j;
    int count = 0, pares = 0, impares = 0;
    long long suma = 0;

    for (i = 2; i <= N; i++) {
        int primo = 1;

        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                primo = 0;
                break;
            }
        }
        if (primo) {
            count++;
            suma += i;

            if (i % 2 == 0)
                pares++;
            else
                impares++;
        }
    }
    printf("Primos encontrados: %d\n", count);
    printf("Suma de primos: %lld\n", suma);
    printf("Primos pares: %d\n", pares);
    printf("Primos impares: %d\n", impares);

    return 0;
}
