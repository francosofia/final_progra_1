import csv



def leer_csv_y_convertir_a_matriz(nombre_archivo):
    matrices = []
    with open(nombre_archivo, newline='') as archivo:
        lector = csv.reader(archivo)

        for fila in lector: # Itera sobre cada fila del archivo
            if len(fila) == 9: # Asegúrate de que hay 9 elementos para formar una matriz 3x3
                matriz = []
                matriz.append(fila[0:3])  # Añade la primera fila de la matriz
                matriz.append(fila[3:6])  # Añade la segunda fila de la matriz
                matriz.append(fila[6:9])  # Añade la tercera fila de la matriz
                matrices.append(matriz)  # Añade la matriz completa a la lista de matrices
    return matrices


def mostrar_matriz():

    matriz_recibida = leer_csv_y_convertir_a_matriz("sopa_de_letras.csv")

    for matriz in matriz_recibida:
        for fila in matriz:
            print(fila)
        print()


def matris_vocales(matrices):
    matriz_vocales=[]
    matrices_vocales=[]
    lista_vocales=[]
    for matris in matrices:
        for lineas in matris:
            for caracter in lineas:
                match caracter:
                    case "A":
                        lista_vocales.append(caracter)  # Añade la primera fila de la matriz
                        
                        break
                    case "E":
                        lista_vocales.append(caracter)  # Añade la primera fila de la matriz
                        
                        break
                    case "I":
                        lista_vocales.append(caracter)  # Añade la primera fila de la matriz
                        
                        break
                    case "O":
                        lista_vocales.append(caracter)  # Añade la primera fila de la matriz
                        
                        break
                    case "U":
                        lista_vocales.append(caracter)  # Añade la primera fila de la matriz
                        
                        break
            matriz_vocales.append(lista_vocales[0:3])  # Añade la primera fila de la matriz
            matriz_vocales.append(lista_vocales[3:6])  # Añade la segunda fila de la matriz
            matriz_vocales.append(lista_vocales[6:9])  # Añade la tercera fila de la matriz
            matrices_vocales.append(matriz_vocales)  # Añade la matriz completa a la lista de matrices
    print(matriz_vocales)

matris_vocales(leer_csv_y_convertir_a_matriz("sopa_de_letras.csv"))