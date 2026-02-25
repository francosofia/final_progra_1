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
        flag_2 = salida(flag_2)

















