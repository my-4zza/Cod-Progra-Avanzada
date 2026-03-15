#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

// c_no_opt.c v1.1.0

// version: 1.1.0
// Autor: Antonio Portilla
// Mejoras pequeñas para optimizar el codigo original

// implementacion de break y modificacion en for.
int main() {
    int N = 1000;
    int count_primos = 0;
    long long suma_primos = 0;
    int primos_pares = 0;
    int primos_impares = 0;

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
            count_primos = count_primos + 1;
            suma_primos = suma_primos + m;
            primos_impares = primos_impares + 1;
        } else {
            // rama para números compuestos
            int z = 0;
            z = z + 1;
        }
    }
    printf("Primos encontrados: %d\n", count_primos);
    printf("Suma de primos: %lld\n", suma_primos);
    printf("Primos pares.:%d\n", primos_pares);
    printf("Primos impares: %d\n", primos_impares);

    return 0;
}
