from manejo_def import *

numero = None
flag_2=True

numero = pedir_numero()

while True:
    if flag_2==True:
        
        match numero:
            case 1:
                print("1")
                flag_2 = False
            case 2:
                print("2")
                flag_2 = False
            case 3: 
                print("3")
                flag_2 = False
            case 4:
                break
        
        tonoto=input("Desea realizar otra consulta? (si/no): ")
        if tonoto.lower() == "si":
            numero = pedir_numero()
            flag_2=True
        elif tonoto.lower() == "no":
            print("Gracias por usar el programa.")
            break
        else:
            print("Respuesta no válida. Saliendo del programa.")
            break

















