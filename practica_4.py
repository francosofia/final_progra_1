


lista=[1,2,3,4,5,6,7]


def lista_a_matriz_3x3(lista):
    matriz = []
    index = 0
    for fila in range(3):
        contenido = []
        for columna in range(3):
            if index < len(lista):
                contenido.append(lista[index])
            else:
                contenido.append("*")
            index += 1
        matriz.append(contenido)
    return matriz


#matriz = lista_a_matriz_3x3(lista)
#
#for fila in matriz:#se usa el bucle para q aparezcan una abajo de la otra
#    print(fila)

#encontrar palabras de un largo de 5 o de la variable palabra_1
#
def buscar_palabras():
    palabra_1="FRANCO"
    palanra_2="ZED"
    with open("letras.csv", 'r') as archivo:
        
        contenido=archivo.readlines()
        
    for linea in contenido:
        
        linea = linea.strip().split(";")
        
        for caracter in range(len(linea)- len(palabra_1) + 1):
            
            busqueda_1=''.join(linea[caracter:caracter + len(palabra_1)])
            
            print(busqueda_1.upper())
            if palanra_2 in busqueda_1.upper():#encuentra la secuencia muchas veces
                print("encontro zed")#encuentra la secuencia muchas veces
            if palabra_1==busqueda_1.upper():#encuentra la secuencia una sola vez
                
                print("encontro franco")


#print(buscar_palabras())



#tateti intento


def tateti():
    linea=["-"]*3
    matriz=[]
    turno ="x"
    flag_partida=True
    for i in range(3):
        matriz.append(linea)
    while flag_partida:
        
        if turno =="x":
            
            movimiento=int(input("ingrese su moviemiento indicando del 0 al 9 donde deceas colocar tu pieza"))
            
            while matriz[movimiento]!="-":
                
                print("esta casilla esta ocupada")
                
                movimiento=int(input("ingrese otro moviemiento indicando del 0 al 9 donde deceas colocar tu pieza"))
            
        if turno =="o":
            
            movimiento=int(input("del 0 al 9 donde deceas colocar tu pieza"))
            
    
    return matriz


#
#
#matriz = tateti()
#
#for fila in matriz:
#    print(fila)
#






matriz=[]
turno ="x"
flag_partida=True
for i in range(3):
    matriz.append(["-"] * 3)
movimiento_fila=int(input("en que fila quieres colocar tu pieza del 1 al 3"))
movimiento_columna=int(input("en que columna quieres colocar tu pieza del 1 al 3"))
print(matriz)
match movimiento_fila ,movimiento_columna:
    case 1|2|3:
        if matriz[movimiento_fila-1][movimiento_columna-1]!="-":
            print("entro")
        else:
            matriz[movimiento_fila-1][movimiento_columna-1]="x"
            print("cambio")
    case 4|5|6:
        if matriz[movimiento_fila-1][movimiento_columna-1]!="-":
            print("entro")
    case 7|8|9:
        if matriz[movimiento_fila-1][movimiento_columna-1]!="-":
            
            print("entro")
print(matriz)