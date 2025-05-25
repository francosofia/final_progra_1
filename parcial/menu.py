import funciones 

opcion = input("Seleccione una opción:\n1. Crear archivo\n2. Leer archivo\n3. Modificar archivo\n4. Eliminar archivo\n5. Salir\n")

match  opcion:
    case "1":
        funciones.abrir_csv()
    case "2":
        funciones.leer_archivo()
    case "3":
        funciones.modificar_archivo()
    case "4":
        funciones.eliminar_archivo()
    case "5":
        print("Saliendo del programa.")
    case _:
        print("Opción no válida. Por favor, intente de nuevo.")




