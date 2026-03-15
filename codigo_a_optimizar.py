# python_no_opt.py
# Versión: 2.0.0 (Actualización Mayor: Optimización algorítmica y cambio de paradigma)

# El código Python determina el valor modal de una lista de 13 enteros y calcula 
# la suma de sus dígitos. En esta versión mayor, se migró de una búsqueda lineal 
# anidada basada en bucles 'while' (O(n²)) hacia un mapeo de frecuencias 
# eficiente mediante la clase 'Counter' (O(n)), reduciendo drásticamente la 
# complejidad computacional.

# NOTAS DE LA VERSIÓN 2.0.0:
# - Se eliminó la estructura de bucles anidados i/j para evitar comparaciones redundantes.
# - Se implementó 'collections.Counter' para realizar el conteo en un solo paso lineal.
# - Se optimizó la suma de dígitos utilizando una expresión generadora más eficiente.
# - Se añadió un bloque try-except para el manejo de errores en la entrada de datos.


from collections import Counter

# Entrada de datos
entrada = input("Escribe la lista de 13 números separados por un espacio:\n")
try:
    numeros = [int(x) for x in entrada.split()]
except ValueError:
    print("Error: Asegúrate de ingresar solo números enteros.")
    exit()

# OPTIMIZACIÓN MAJOR (v2.0.0)
# Usamos Counter (basado en Hash Map) para contar en tiempo lineal O(n)
# Esto reemplaza los bucles while anidados que eran O(n^2)
conteos = Counter(numeros)

# Convertir a la estructura de lista de tuplas requerida para compatibilidad
frecuencias = list(conteos.items())

# Encontrar el valor modal (Counter ya tiene un método eficiente para esto)
if frecuencias:
    modo, max_cuenta = conteos.most_common(1)[0]
    
    # Sumar dígitos del valor modal (usando comprensión de tipos para mayor rapidez)
    suma_digitos = sum(int(d) for d in str(abs(modo)))

    # Salidas
    print("Frecuencias:", frecuencias)
    print("Modo:", modo, "con cuenta:", max_cuenta)
    print("Suma de dígitos del modo:", suma_digitos)
else:
    print("No se ingresaron números.")
