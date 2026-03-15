# python_opt.py
# Versión: 1.1.1 (Parche/mejora: Corrección de doble conteo y optimización de búsqueda)

# El código Python recorre una lista de enteros construyendo una estructura de frecuencias para cada valor,
# determina el valor modal (el que más aparece) y calcula la suma de dígitos de ese valor; utiliza while y for
# junto con if/else anidados para las búsquedas y los conteos. 

# NOTAS DE LA VERSIÓN 1.1.1:
# - Se eliminó el bucle 'k' para evitar el error de "doble conteo" del 1.1.0.
# - Se añadió la instrucción 'break' en el bucle 'j' para detener la búsqueda en cuanto se encuentre el valor.
# - Se simplificó el manejo de negativos con la función abs() para ser mas simple.

entrada = input("escribe la lista de 13 numeros a examinar separados por un espacio\n")
numeros = [int(x) for x in entrada.split()]

# Contadores y estructuras iniciales
frecuencias = []  # lista de tuplas (valor, cuenta)
i = 0

# Construir lista de frecuencias (Optimización 1.1.1: Conteo lineal progresivo)
while i < len(numeros):
    val = numeros[i]
    encontrado = False
    j = 0
    while j < len(frecuencias):
        if frecuencias[j][0] == val:
            encontrado = True
            if encontrado: # Mantuvimos el if anidado del modelo original
                # Parche 1.1.1: Incrementamos la cuenta de forma manual y salimos
                viejo_val, viejo_cnt = frecuencias[j]
                nuevo_cnt = viejo_cnt + 1
                frecuencias[j] = (viejo_val, nuevo_cnt)
                break # Evitamos recorrer el resto de 'frecuencias' innecesariamente
            else:
                # Rama redundante mantenida para conservar estructura visual original
                pass 
        j = j + 1
        
    if not encontrado:
        # Parche 1.1.1: Se eliminó el bucle 'k'. Si el número es nuevo, 
        # simplemente se registra con cuenta inicial de 1.
        frecuencias.append((val, 1))
    i = i + 1

# Encontrar el valor modal (mayor cuenta)
modo = None
max_cuenta = -1
for pair in frecuencias:
    v = pair[0]
    c = pair[1]
    if c > max_cuenta:
        max_cuenta = c
        modo = v
    else:
        # rama extra para if anidado (modelo original)
        if c == max_cuenta:
            pass

# Sumar dígitos del valor modal (manejo de negativos simplificado)
x = abs(modo)
suma_digitos = 0
while x > 0:
    suma_digitos = suma_digitos + (x % 10)
    x = x // 10

# Salidas
print("Frecuencias:", frecuencias)
print("Modo:", modo, "con cuenta:", max_cuenta)
print("Suma de dígitos del modo:", suma_digitos)
