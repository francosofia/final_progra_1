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

def contar_cantidad_impares():
    matriz=abrir_csv()
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
                lista_impares=[]
    
    cantidad_impares_consecutivos = len(matriz_impares)
    return matriz_impares

print(contar_cantidad_impares())