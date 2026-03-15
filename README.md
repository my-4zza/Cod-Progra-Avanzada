# Programacion-Avanzada-Codigos
# Optimización de Código en Python y C

Este repositorio contiene los programas base en **Python y C** desarrollados para una actividad de optimización de la experiencia educativa de **Programación Avanzada**. 

## Propósito del Ejercicio
El objetivo principal es analizar, optimizar y documentar línea a línea programas base en lenguajes de alto y bajo nivel. Se busca medir el impacto real de las optimizaciones implementadas sin alterar los nombres de los archivos originales, siguiendo una política estricta de versionado en las cabeceras.

## Integrantes del Equipo
* Alarcón Galván Jimmy Loucioss
* Alegría Ponce José Santiago
* Cid García Alfredo
* Hernández García Juan Carlos
* Pérez González Azael
* Portilla Durán Antonio de Jesús

---

## Estructura del Repositorio

| Archivo / Carpeta | Descripción |
| :--- | :--- |
| `README.md` | Instrucciones y política de versionado (este archivo). |
| `python_no_opt.py` | Versión optimizada del código en Python (mantiene nombre original). |
| `c_no_opt.c` | Versión optimizada del código en C (mantiene nombre original). |
| `results/` | Salidas crudas, archivos CSV de tiempos y análisis de rendimiento. |
| `tests/` | Casos de prueba de entrada y salida esperada. |
| `CHANGELOG.md` | Registro detallado de versiones, autores y mejoras. |
| `.gitignore` | Exclusión de binarios y archivos temporales pesados. |

---

## Política de Versionado
Para cumplir con los requisitos del ejercicio, cada archivo debe mantener su nombre original. El progreso se registra aumentando la versión en la cabecera del propio archivo:

* **Versión Inicial:** `1.0.0`
* **Versión Optimizada:** `1.1.0` (o similar)

---

## Ejecución y Pruebas

### Python
Para ejecutar y medir tiempos en Python:
```bash
python python_no_opt.py
