print("===== MENÚ DE RESTAURANTE =====")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Ensalada")
print("4. Bebida")
print("===============================")

opcion = int(input("Seleccione una opción: "))

match opcion:
    case 1:
        print("Ha seleccionado: Hamburguesa")
    case 2:
        print("Ha seleccionado: Pizza")
    case 3:
        print("Ha seleccionado: Ensalada")
    case 4:
        print("Ha seleccionado: Bebida")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
