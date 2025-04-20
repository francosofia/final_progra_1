



def cargar_matriz():
    matris=[]
    matris_de_matrices=[]
    contador=0
    with open("sopa_de_letras.csv", 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        contenido = linea.strip().split(";")
        
        for i in contenido:
            
            if len(matris)<10:
                matris.append(i)
            else:
                
                matris_de_matrices.append(matris)
                
                matris=[]
                matris.append(i)
            
    return matris_de_matrices


#print(cargar_matriz())
def buscar_iguales_horizontal():
    matris= cargar_matriz()
    contenido_anterior=0
    lista_iguales=[]
    for lista in matris:
        for contenido in lista:
            if contenido== contenido_anterior:
                lista_iguales.append(contenido)
            if contenido!= contenido_anterior:
                contenido_anterior=contenido
    maximo=max(lista_iguales ,key=lista_iguales.count)
    minimo=min(lista_iguales ,key=lista_iguales.count)
    print(minimo)
    print(maximo)
    return lista_iguales




#print(buscar_consecutivos_horizontal())


def buscar_iguales_vertical():
    matriz = cargar_matriz() 
    cantidad_De_iguales=[]
    for columnas in range(9):
        for filas in range(3):
            if matriz[filas][columnas]==matriz[filas+1][columnas]:
                cantidad_De_iguales.append(matriz[filas][columnas])
                
    maximo=max(cantidad_De_iguales ,key=cantidad_De_iguales.count)
    minimo=min(cantidad_De_iguales ,key=cantidad_De_iguales.count)
    print(minimo)
    print(maximo)
    print(cantidad_De_iguales)
#
#resultado = buscar_consecutivos_vertical()
#print(resultado)
#


def buscar_consecutivos():
    matris= cargar_matriz()
    lista_consecutivos=[]
    matriz_consecutivas=[]
    
    for lista in matris:
        
        flag_primer_Caso=True
        
        for contenido in range(len(lista)-1):
            
            if flag_primer_Caso==True :
                
                primero=int(lista[0])
                segundo=int(lista[1])
                if primero==segundo-1:
                    
                    lista_consecutivos.append(primero)
                    flag_primer_Caso = False
            
            actual = int( lista[contenido])
            anterior =int (lista[contenido - 1])
            
            if actual == anterior+1 :
                lista_consecutivos.append(actual)
        if lista_consecutivos!=[]:
            matriz_consecutivas.append(lista_consecutivos)
            lista_consecutivos=[]
    return matriz_consecutivas



#print(buscar_consecutivos())





def buscar_consecutivos_vertical():
    matriz = cargar_matriz() 
    matriz_de_iguales=[]
    cantidad_De_iguales=[]
    for filas in range(len(matriz) - 1):
        for columnas in range(9):
            acutual= int(matriz[filas][columnas])
            siguiente=int(matriz[filas+1][columnas])
            
            if acutual == siguiente-1:
                cantidad_De_iguales.append(acutual)
                cantidad_De_iguales.append(siguiente)
                matriz_de_iguales.append(cantidad_De_iguales)
                cantidad_De_iguales=[]
        
        
#lo que define si es mas max o min es esto
#if cantidad_De_iguales!=[]:
#    maximo=max(cantidad_De_iguales ,key=cantidad_De_iguales.count)
#    minimo=min(cantidad_De_iguales ,key=cantidad_De_iguales.count)
#    print(minimo)
#    print(maximo)
#print(matriz_de_iguales)





print(buscar_consecutivos_vertical())


