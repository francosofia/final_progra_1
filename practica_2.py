# Leer el archivo CSV
with open('sopa_de_letras.csv', 'r') as archivo:
    # Leer todas las líneas del archivo
    lineas = archivo.readlines()

# Crear una lista para almacenar los números
datos = []

# Procesar cada línea
for linea in lineas:
    # Dividir cada línea por el delimitador ';' y convertir a enteros
    numeros = list(map(int, linea.strip().split(';')))
    
    datos.extend(numeros)

# Asegurarse de que tenemos exactamente 50 números
if len(datos) != 50:
    raise ValueError("El archivo no contiene exactamente 50 números")

# Convertir los datos en una matriz 5x10
matriz = []
for i in range(0, 50, 10):
    matriz.append(datos[i:i + 10])

# Mostrar la matriz original
print("Matriz original (5x10):")
for fila in matriz:
    print(fila)

# Aplanar y ordenar la matriz
datos_ordenados = sorted(datos)

# Reconstruir la matriz 5x10 ordenada
matriz_ordenada = []
for i in range(0, 50, 10):
    matriz_ordenada.append(datos_ordenados[i:i + 10])

# Mostrar la matriz ordenada
print("\nMatriz ordenada (5x10):")
for fila in matriz_ordenada:
    print(fila)
