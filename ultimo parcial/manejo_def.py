import csv

"""
def cargar_matriz(path):
    matriz = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            matriz.append(row)
    return matriz

for fila in cargar_matriz('matriz_final_20250527.csv'):
    print(fila)
    """





def cargar_matriz(ruta):
    matriz = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            matriz.append((x) for x in fila)
    return matriz


#print(cargar_matriz("matriz_final_20250527.csv"))

def pedir_numero():
    while True:
        numero = input("Que desea hacer?\n1. Mostrar promedios\n2. Mostrar el mayor promedio\n")

        if numero.isdigit():
            numero = int(numero)

            if numero<5 and numero> 1:
                
                break
            
            print("Ingrese un numero valido")
    return numero




lista=[1,2,3,-4,5.545,-36,3247]

#print(sorted(lista, key= abs))


#print(list(zip(*matriz)))
def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer todas las líneas del archivo
        contenido = archivo.read().splitlines()
    return contenido

#print(leer_csv('nombres_final_20250527.csv'))


#print(leer_csv('legajos_final_20250527.csv'))


def leer_matrez(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read().splitlines()
    return contenido

legajo=leer_csv("legajos_final_20250527.csv")
nombre=leer_csv("nombres_final_20250527.csv")
genero=leer_csv("generos_final_20250527.csv")
lista_matriz = leer_matrez('matriz_final_20250527.csv')


def crear_matriz(lista):
    matriz = []
    for i in lista:
        fila = i.split(',')  # Dividir cada línea por comas para formar una fila
        matriz.append(fila)  # Añadir la fila a la matriz
    return matriz

matriz_completa = crear_matriz(lista_matriz)



def promedios(matriz):
    promedios = []
    numeros=[]
    for fila in range(1, len(matriz)):
        numero = sum(int(x) for x in matriz[fila])
        promedio = int(numero)/ 5  
        promedios.append(promedio)
        numeros=[]
    return promedios

def promedio_estudiante(estudiante,promedio):
    lista_estudiante=[]
    alumno=[]
    for i in range(1,len(estudiante)):
        alumno.append(estudiante[i])
        alumno.append(str(promedio[i-1]))
        lista_estudiante.append(alumno)
        alumno=[]
    return lista_estudiante

#print(promedio_estudiante(nombre,promedios(matriz_completa)))

#print(max(promedio_estudiante(nombre,promedios(matriz_completa)), key=lambda x: x[1]))

def ordenar(indice):
    if indice == "mayor":
        return sorted(promedio_estudiante(nombre,promedios(matriz_completa)), key=lambda x: x[1], reverse=True)
    elif indice == "menor":
        return sorted(promedio_estudiante(nombre,promedios(matriz_completa)), key=lambda x: x[1])

#indice = input("Ingrese 'mayor' para ordenar de mayor a menor o 'menor' para ordenar de menor a mayor: ")
#print(ordenar(indice))

def promedio_estudiante(estudiante, promedio):
    lista_estudiante = []

    for i in range(1, len(estudiante)):
        lista_estudiante.append([
            legajo[i],
            estudiante[i],
            genero[i],
            *matriz_completa[i],
            promedio[i-1]
        ])

    return lista_estudiante

def ordenar(orden):
    datos = promedio_estudiante(nombre, promedios(matriz_completa))

    if orden == "DESC":
        return sorted(datos, key=lambda x: x[8], reverse=True)
    elif orden == "ASC":
        return sorted(datos, key=lambda x: x[8])
    else:
        return datos
def mostrar_uno(alumno):
    print(
        alumno[0], "|",
        alumno[1], "|",
        alumno[2], "|",
        alumno[3], "|",
        alumno[4], "|",
        alumno[5], "|",
        alumno[6], "|",
        alumno[7], "|",
        alumno[8]
    )

def mostrar_todos(orden):

    print("LEGAJO | NOMBRE | GENERO | M_1 | M_2 | M_3 | M_4 | M_5 | PROMEDIO")

    lista_ordenada = ordenar(orden)

    for alumno in lista_ordenada:
        mostrar_uno(alumno)


#orden = input("Ingrese ASC o DESC: ")
#mostrar_todos(orden)
def armar_datos():
    datos = []

    lista_promedios = promedios(matriz_completa)

    for i in range(1, len(nombre)):
        fila = [
            legajo[i],
            nombre[i],
            genero[i],
            *matriz_completa[i],
            lista_promedios[i-1]
        ]
        datos.append(fila)

    return datos

#print(armar_datos())

