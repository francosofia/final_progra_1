def leer_csv_a_matriz(archivo_csv, filas, columnas):
    """
    Lee un archivo CSV con números separados por ';' y lo convierte en una matriz.
    
    :param archivo_csv: Nombre del archivo CSV.
    :param filas: Número de filas que se espera en la matriz.
    :param columnas: Número de columnas que se espera en la matriz.
    :return: Una matriz de números (lista de listas).
    """
    with open("sopa_de_letras.csv", 'r') as archivo:
        lineas = archivo.readlines()

    datos = []

    # Procesar cada línea
    for linea in lineas:
        numeros = list(map(int, linea.strip().split(';')))
        datos.extend(numeros)

    # Asegurarse de que tenemos la cantidad correcta de datos
    if len(datos) != filas * columnas:
        raise ValueError(f"El archivo no contiene exactamente {filas * columnas} números")

    # Convertir los datos en una matriz
    matriz = []
    for i in range(0, len(datos), columnas):
        matriz.append(datos[i:i + columnas])

    return matriz


def encontrar_secuencias_consecutivas(lista):
    """
    Encuentra todas las secuencias consecutivas en una lista de números.

    :param lista: Lista de números.
    :return: Lista de secuencias consecutivas.
    """
    secuencias = []
    secuencia_actual = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1] + 1:
            secuencia_actual.append(lista[i])
        else:
            if len(secuencia_actual) > 1:
                secuencias.append(secuencia_actual)
            secuencia_actual = [lista[i]]

    # Añadir la última secuencia si es válida
    if len(secuencia_actual) > 1:
        secuencias.append(secuencia_actual)

    return secuencias


def detectar_secuencias_en_matriz(matriz):
    """
    Detecta secuencias consecutivas tanto horizontalmente como verticalmente en una matriz.
    
    :param matriz: La matriz de números.
    :return: Lista de secuencias consecutivas encontradas.
    """
    secuencias_encontradas = []

    # Verificar filas (horizontal)
    for fila in matriz:
        secuencias = encontrar_secuencias_consecutivas(fila)
        secuencias_encontradas.extend(secuencias)

    # Verificar columnas (vertical)
    columnas = len(matriz[0])
    for col in range(columnas):
        columna = [matriz[fila][col] for fila in range(len(matriz))]
        secuencias = encontrar_secuencias_consecutivas(columna)
        secuencias_encontradas.extend(secuencias)

    return secuencias_encontradas


def encontrar_secuencia_mas_corta_y_larga(secuencias):
    """
    Encuentra la secuencia consecutiva más corta y la más larga.
    
    :param secuencias: Lista de secuencias consecutivas.
    :return: La secuencia más corta y la más larga.
    """
    if not secuencias:
        return None, None

    secuencia_mas_corta = min(secuencias, key=len)
    secuencia_mas_larga = max(secuencias, key=len)

    return secuencia_mas_corta, secuencia_mas_larga


def contar_ocurrencias_secuencias(secuencias):
    """
    Cuenta cuántas secuencias consecutivas se encontraron.
    
    :param secuencias: Lista de secuencias consecutivas.
    :return: Número de secuencias encontradas.
    """
    return len(secuencias)


def mostrar_resultados(secuencias, secuencia_mas_corta, secuencia_mas_larga):
    """
    Muestra los resultados de las secuencias encontradas.
    
    :param secuencias: Lista de secuencias consecutivas.
    :param secuencia_mas_corta: Secuencia consecutiva más corta.
    :param secuencia_mas_larga: Secuencia consecutiva más larga.
    """
    print(f"Total de secuencias consecutivas encontradas: {contar_ocurrencias_secuencias(secuencias)}")

    if secuencia_mas_corta:
        print(f"Secuencia más corta: {secuencia_mas_corta} (Longitud: {len(secuencia_mas_corta)})")

    if secuencia_mas_larga:
        print(f"Secuencia más larga: {secuencia_mas_larga} (Longitud: {len(secuencia_mas_larga)})")

    # Imprimir todas las secuencias encontradas (opcional)
    if secuencias:
        print("Secuencias encontradas:")
        for secuencia in secuencias:
            print(secuencia)
    else:
        print("No se encontraron secuencias consecutivas.")


# Función principal para ejecutar el proceso completo
def main(archivo_csv):
    filas = 5  # Número de filas esperadas
    columnas = 10  # Número de columnas esperadas

    # Leer el archivo CSV y convertirlo en una matriz
    matriz = leer_csv_a_matriz(archivo_csv, filas, columnas)

    # Detectar secuencias consecutivas en la matriz
    secuencias_encontradas = detectar_secuencias_en_matriz(matriz)

    # Encontrar la secuencia más corta y más larga
    secuencia_mas_corta, secuencia_mas_larga = encontrar_secuencia_mas_corta_y_larga(secuencias_encontradas)

    # Mostrar los resultados
    mostrar_resultados(secuencias_encontradas, secuencia_mas_corta, secuencia_mas_larga)


# Ejecutar el programa principal con el archivo CSV de ejemplo
main('archivo.csv')