
#1 – Crear una función para cargar el archivo data_final_20250422.csv y transformarlo a una matriz de 10 filas
#por 10 columnas.

def abrir_csv():
    #lista=[]
    matriz=[]
    with open("data_final_20250422.csv", "r") as archivo:
        contenido = archivo.readlines()
    for lineas in contenido:
        lista=[]
        linea=lineas.strip().split(",")
        #print(linea)
        for caracter in linea:
            
            if len(lista)<10:
                lista.append(caracter)
            #else:
            #    matriz.append(lista)
                
            #    lista=[]
            #    lista.append(caracter)
        matriz.append(lista)
    
    return matriz

#print(abrir_csv())    
#2 – Si existen números consecutivos impares de manera horizontal, cuya leyenda será de acuerdo al caso:
# “EXISTEN NÚMEROS CONSECUTIVOS IMPARES”
# “NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES”

def buscar_consecutivos_impar():
    matriz=abrir_csv()
    retorno= "NO EXISTEN NÚMEROS CONSECUTIVOS IMPARES"
    for linea in matriz:
        
        for caracter in range(len(linea)-1):

            ahora=int(linea[caracter])
            siguiente=int(linea[caracter+1])

            if ahora%2 != 0 and ahora== siguiente-2 :

                retorno="EXISTEN NÚMEROS CONSECUTIVOS IMPARES"
                
    return retorno
    
                

#print(buscar_consecutivos_impar())
    
#3 – Cantidad de ocurrencias de números consecutivos impares.
def secuencias_consecutivos_impares(matriz):
    
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
                    
                    if j <= len(linea)-1 and int(linea[j-1]) == int(linea[j]) - 2:
                        
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
                cantidad_impares_consecutivos+=1
                lista_impares=[]
                
    return matriz_impares

matriz=abrir_csv()

#print(secuencias_consecutivos_impares(matriz))





#4 – Secu**/encia más corta (cantidad de números consecutivos impares que la componen), y los números
#correspondientes.

def consecutivos_mas_corto():
    minimo=100
    matriz=abrir_csv()
    matriz_impares = secuencias_consecutivos_impares(matriz)

    for linea in matriz_impares:
        actual=len(linea)
        
        if minimo>actual:
            minimo=actual
    return minimo



#print(consecutivos_mas_corto())


#5 – Secuencia más larga (cantidad de números consecutivos impares que la componen), y los números
#correspondientes.

def buscar_maximo():
    matriz=abrir_csv()

    matriz_impares = secuencias_consecutivos_impares(matriz)
    maximo=0
    for linea in matriz_impares:
        actual=len(linea)
        
        if maximo<actual:
            maximo=actual

    return maximo

print(buscar_maximo())