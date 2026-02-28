# Ejercicio 2: Mes del Año
# Ingrese un número del 1 al 12 y muestre el nombre del mes

numero = int(input("Ingrese un número del 1 al 12: "))

match numero:
    case 1:
        print("Enero")
    case 2:
        print("Febrero")
    case 3:
        print("Marzo")
    case 4:
        print("Abril")
    case 5:
        print("Mayo")
    case 6:
        print("Junio")
    case 7:
        print("Julio")
    case 8:
        print("Agosto")
    case 9:
        print("Septiembre")
    case 10:
        print("Octubre")
    case 11:
        print("Noviembre")
    case 12:
        print("Diciembre")
    case _:
        print("Número no válido. Ingrese un número del 1 al 12.")
