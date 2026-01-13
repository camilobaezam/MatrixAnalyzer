import os

def ingresar_matriz_manual():
    """Permite ingresar la matriz manualmente por consola."""
    matriz = []
    print("\n--- Ingresar matriz manualmente ---")
    print("Ingresa cada fila separada por espacios (e.g., '1 2 -3').")
    print("Presiona Enter sin valores para terminar.\n")
    
    while True:
        fila_input = input("Fila: ").strip()
        if not fila_input:
            break
        
        # Procesar fila: split y convertir a int
        try:
            fila = [int(x) for x in fila_input.split()]
            if fila:
                matriz.append(fila)
            else:
                print("Fila vacía, ignora.")
        except ValueError:
            print("Error: Ingresa solo enteros separados por espacios.")
    
    if not matriz:
        print("No se ingresó ninguna fila válida.")
    return matriz


def cargar_matriz_desde_archivo(ruta):
    """Carga la matriz desde un archivo de texto."""
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{ruta}' no existe.")
        return None
    
    matriz = []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                fila_input = linea.strip()
                if fila_input:
                    # Split por espacios o comas
                    fila_input = fila_input.replace(',', ' ')
                    fila = [int(x) for x in fila_input.split() if x]
                    if fila:
                        matriz.append(fila)
        
        if not matriz:
            print("El archivo está vacío o no contiene datos válidos.")
            return None
        
        # Verificar si es rectangular (opcional, pero avisa)
        longitudes = [len(fila) for fila in matriz]
        if len(set(longitudes)) > 1:
            print("Advertencia: Matriz no rectangular (filas de diferentes longitudes).")
        
        print(f"Matriz cargada exitosamente ({len(matriz)} filas, {longitudes[0] if longitudes else 0} columnas).")
        return matriz
    
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


def procesar_matriz(matriz):
    """Reemplaza negativos por 0 y cuenta ceros y positivos."""
    if not matriz:
        print("Matriz vacía, no hay nada que procesar.")
        return None, 0, 0
    
    # Copia para no modificar original, pero como modifica en lugar, usamos copia profunda
    matriz_mod = [fila[:] for fila in matriz]
    
    ceros = 0
    positivos = 0
    
    for i in range(len(matriz_mod)):
        for j in range(len(matriz_mod[i])):
            valor = matriz_mod[i][j]
            if valor < 0:
                matriz_mod[i][j] = 0
                ceros += 1
            elif valor == 0:
                ceros += 1
            else:
                positivos += 1
    
    return matriz_mod, ceros, positivos


def mostrar_matriz(matriz, titulo="Matriz"):
    """Muestra la matriz en consola."""
    if not matriz:
        print("Matriz vacía.")
        return
    
    print(f"\n{titulo}:")
    for fila in matriz:
        print(fila)


def main():
    print("=== MatrixAnalyzer - Analizador de Matrices ===\n")
    
    matriz = None
    
    while True:
        print("Opciones:")
        print("1. Ingresar matriz manualmente")
        print("2. Cargar matriz desde archivo")
        print("3. Procesar matriz")
        print("4. Mostrar matriz actual")
        print("5. Salir")
        
        opcion = input("\nElige una opción: ").strip()
        
        if opcion == '1':
            matriz = ingresar_matriz_manual()
        elif opcion == '2':
            ruta = input("Ruta del archivo: ").strip()
            if ruta:
                matriz = cargar_matriz_desde_archivo(ruta)
            else:
                print("Debes ingresar una ruta.")
        elif opcion == '3':
            if matriz is None:
                print("No hay matriz cargada. Ingresa o carga una primero.")
                continue
            matriz_mod, ceros, positivos = procesar_matriz(matriz)
            mostrar_matriz(matriz, "Matriz original")
            mostrar_matriz(matriz_mod, "Matriz modificada (negativos reemplazados por 0)")
            print("\nAnálisis:")
            print(f"- Número de ceros: {ceros}")
            print(f"- Número de positivos: {positivos}")
        elif opcion == '4':
            if matriz is None:
                print("No hay matriz cargada.")
            else:
                mostrar_matriz(matriz, "Matriz actual")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
