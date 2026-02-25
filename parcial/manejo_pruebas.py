"""
1  Crear una función para cargar el archivo data_final_20250422.csv y transformarlo a una matriz de 10 filas
por 10 columnas.
Luego de la carga del archivo (ítem 1), buscar e informar:
2  Si existen números consecutivos impares de manera horizontal, cuya leyenda será de acuerdo al caso:
 “EXISTEN NÚMEROS CONSECUTIVOS IMPARES”
 “NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES”
Cabe aclarar que cada secuencia de números consecutivos impares se debe tomar completa, no se divide.
Por ejemplo: la secuencia 1, 3, 5 no admite las secuencias 1, 3 o 3, 5.
En caso de existir números consecutivos impares:
3  Cantidad de ocurrencias de números consecutivos impares.
4  Secuencia más corta (cantidad de números consecutivos impares que la componen), y los números
correspondientes.
5  Secuencia más larga (cantidad de números consecutivos impares que la componen), y los números
correspondientes.
6  Salir

"""

#1rear una función para cargar el archivo data_final_20250422.csv y transformarlo a una matriz de 10 filas
#por 10 columnas.
#Luego de la carga del archivo (ítem 1), buscar e informar:

def abrir_csv(path):
    matriz = []

    with open(path, 'r') as file:
        contenido = file.readlines()
    for lineas in contenido:
        lista=[]
        linea=lineas.strip().split(",")
        for caracter in linea:
            if len(lista)<10:
                lista.append(caracter)
        matriz.append(lista)
    return matriz

#print("Matriz cargada:", abrir_csv('parcial\data_final_20250422.csv'))

"""
2  Si existen números consecutivos impares de manera horizontal, cuya leyenda será de acuerdo al caso:
 “EXISTEN NÚMEROS CONSECUTIVOS IMPARES”
 “NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES”
Cabe aclarar que cada secuencia de números consecutivos impares se debe tomar completa, no se divide.
Por ejemplo: la secuencia 1, 3, 5 no admite las secuencias 1, 3 o 3, 5.
En caso de existir números consecutivos impares:
"""

def consecutivos_impares(matriz):
    matriz=abrir_csv()
    retorno= "NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES"
    for linea in matriz:
        
        for caracter in range(len(linea)-1):

            ahora=int(linea[caracter])
            siguiente=int(linea[caracter+1])

            if ahora%2 != 0 and ahora== siguiente-2 :

                retorno="EXISTEN NÚMEROS CONSECUTIVOS IMPARES"
                
    return retorno


#
#for fila in matriz:
#    contador = 0
#    for num in fila:
#        if num % 2 != 0:
#            contador += 1
#            if contador == 2:
#                print("EXISTEN NÚMEROS CONSECUTIVOS IMPARES")
#                exit()
#        else:
#            contador = 0

#print("NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES")

matriz = [
    [2, 4, 6, 8],
    [1, 3, 5, 2],
    [7, 9, 11, 13],
    [2, 1, 4, 3],
    [5, 7, 9, 11],
    [2, 4, 6, 8],
]

secuencias = []

for fila in matriz:
    secuencia_actual = []
    
    for num in fila:
        if num % 2 != 0:  # es impar
            secuencia_actual.append(num)
        else:
            if len(secuencia_actual) >= 2:
                secuencias.append(secuencia_actual)
            secuencia_actual = []
    
    # chequeo al final de la fila
    if len(secuencia_actual) >= 2:
        secuencias.append(secuencia_actual)

# Resultado
if secuencias:
    print("EXISTEN NÚMEROS CONSECUTIVOS IMPARES")
    print("Secuencias encontradas:", secuencias)
    
    mas_grande = max(secuencias, key=len)
    print("La secuencia más grande es:", mas_grande)
else:
    print("NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES")




#matriz = abrir_csv('parcial/data_final_20250422.csv')
#print(consecutivos_impares(matriz))

#



def contar_cantidad_impares(matriz):
    matriz_impares=[]
    lista_impares=[] 
    cantidad_impares_consecutivos=0
    for linea in matriz:
        indice=0
        while indice < (len(linea) -1):
            ahora=int(linea[indice])
            siguiente=int(linea[indice+1])
            if  ahora %2 != 0 and ahora== siguiente-2 :
                lista_impares.append(ahora)
                j = indice + 1  # Comenzamos desde el siguiente al "siguiente"
                while j < len(linea) and j > 0:
                    if j < len(linea) and int(linea[j-1]) == int(linea[j]) - 2:
                        agregar = int(linea[j])
                        lista_impares.append(agregar)
                        j += 1
                    else:
                        break
                # Después de encontrar todos los impares consecutivos, actualizar indice
                indice = j  # Saltar al final de la secuencia
            else:
                indice += 1
            if lista_impares:
                matriz_impares.append(lista_impares)
                lista_impares=[]
    cantidad_impares_consecutivos = len(matriz_impares)
    return matriz_impares
#

matriz=abrir_csv('parcial\data_final_20250422.csv')#

#print(contar_cantidad_impares(matriz))#






#
##4  Secuencia más corta (cantidad de números consecutivos impares que la componen), y los números
##correspondientes.

def secuencia_mas_corta(matriz):
    secuencia_max =[0]*11
    
    for secuencia in matriz:
        if len(secuencia) < len(secuencia_max):
            secuencia_max = secuencia
    return secuencia_max



#print(secuencia_mas_corta(contar_cantidad_impares(matriz)))




##5  Secuencia más larga (cantidad de números consecutivos impares que la componen), y los números
#correspondientes.




def secuencia_mas_larga(matriz):
    secuencia_max =[]
    for secuencia in matriz:
        if len(secuencia) > len(secuencia_max):
            secuencia_max = secuencia
    return secuencia_max

#print(secuencia_mas_larga(contar_cantidad_impares(matriz)))



