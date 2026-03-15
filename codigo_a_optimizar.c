#include <stdio.h>

// c_no_opt.c v1.1.1
// version: 1.2.0
// Autor: Alegria ponce jose santiago
//Eliminacion de librerias no necesarias, elimine un else al final que era redundante y al ultimo if y prints reduje operadores
// declare variables a otro tipo (long long)
N = 1000
count = 0
pares = 0
impares = 0
suma = 0

for i in range(2, N + 1):

    primo = True

    j = 2
    while j * j <= i:
        if i % j == 0:
            primo = False
            break
        j += 1

    if primo:
        count += 1
        suma += i

        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

print("Primos encontrados:", count)
print("Suma de primos:", suma)
print("Primos pares:", pares)
print("Primos impares:", impares)
