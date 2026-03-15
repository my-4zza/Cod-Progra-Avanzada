#include <stdio.h>

// c_no_opt.c v1.1.1
// version: 1.1.1
// Autor: Alegria ponce jose santiago
//Eliminacion de librerias no necesarias, elimine un else al final que era redundante y al ultimo if y prints reduje operadores
// declare variables a otro tipo (long long)
int main() {
    int N = 1000;
    int count_primos = 0, primos_pares = 0, primos_impares = 0;
    long long suma_primos = 0;

    if (N >= 2) { // mejora para poder saltar los demas pares
        count_primos = 1;
        suma_primos = 2;
        primos_pares = 1;
    }

    for (int m = 3; m <= N; m = m + 2) { // aqui se empieza directamente en 3 y salta de 2 en 2, evalua solo impares y reduce codigo inecesario.
        int es_primo = 1;
        int d = 2;

        while (d * d <= m) { // en esta mejora solo se busca hasta la raiz, ahi es primo
            if (m % d == 0) {
                es_primo = 0;
                break;           // con break se ahorra tiempo al no buscar mas divisores extra
            }
            d = d + 1;
        }

        if (es_primo) {
            count_primos++;
            suma_primos += m;
            primos_impares++;
        }
    }
   printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares: %d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}
