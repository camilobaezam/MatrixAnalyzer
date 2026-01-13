# MatrixAnalyzer

Un analizador de matrices simple en Python.  
Procesa una matriz (lista de listas de enteros), reemplaza todos los valores negativos por 0, y cuenta el número de ceros y números positivos en la matriz resultante.

Ideal para practicar:
- Listas de listas (matrices)
- Bucles anidados (for i, for k)
- Condicionales para modificar elementos
- Conteo de valores específicos
- Entrada/salida interactiva

## Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/camilobaezam/MatrixAnalyzer.git
   cd MatrixAnalyzer
2. Crea un archivo matriz.txt con una matriz (filas separadas por líneas, valores por espacios o comas).
Ejemplo:
-1 2 -5 40
9 65 -6 -34
0 -4 9 2

## Uso

Ejecuta el programa:
Bashpython MatrixAnalyzer.py
Menú interactivo:

Opción 1: Ingresar matriz manualmente (por consola)
Opción 2: Cargar matriz desde archivo
Opción 3: Procesar matriz (reemplazar negativos por 0, contar ceros y positivos)
Opción 4: Mostrar matriz actual
Opción 5: Salir

## Ejemplo de ejecución

Supongamos matriz inicial:
-1 2 -5 40
9 65 -6 -34
0 -4 9 2
Después de procesar:

Matriz modificada:
[0, 2, 0, 40]
[9, 65, 0, 0]
[0, 0, 9, 2]
Conteos: Ceros: 6, Positivos: 6

Salida en consola:

=== MatrixAnalyzer - Analizador de Matrices ===

Opciones:
1. Ingresar matriz manualmente
2. Cargar matriz desde archivo
3. Procesar matriz
4. Mostrar matriz actual
5. Salir

Elige una opción: 2
Ruta del archivo: matriz.txt

Matriz cargada exitosamente (3 filas, 4 columnas).

Elige una opción: 3

Procesando matriz...

Matriz original:
[-1, 2, -5, 40]
[9, 65, -6, -34]
[0, -4, 9, 2]

Matriz modificada (negativos reemplazados por 0):
[0, 2, 0, 40]
[9, 65, 0, 0]
[0, 0, 9, 2]

Análisis:
- Número de ceros: 6
- Número de positivos: 6
Ejemplos adicionales
Matriz pequeña manual
Opción 1: Ingresar filas:

Fila 1: -3 4 0
Fila 2: 5 -2 1
(Enter para terminar)

Procesar → Modificada: [0, 4, 0] [5, 0, 1]
Cerros: 3, Positivos: 3
Archivo inválido o vacío
→ Mensaje de error y opción para intentar de nuevo

## Notas

- Asume matrices rectangulares (todas filas mismo largo), pero maneja irregulares
- Entrada manual: ingresa valores separados por espacios, Enter para nueva fila o terminar
- Archivo: valores por espacios/comas, filas por líneas
- Usa UTF-8 para archivos
- No modifica el archivo original

## Ideas para extender

- Guardar matriz procesada en archivo
- Calcular suma/ media de elementos
- Contar negativos antes de reemplazar
- Soporte para matrices no rectangulares
- Interfaz gráfica con tkinter
- Leer desde CSV o Excel (con pandas)

## Autor
Camilo Baeza
