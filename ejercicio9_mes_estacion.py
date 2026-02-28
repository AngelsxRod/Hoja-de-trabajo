# Ejercicio 9: Número de Mes y Estación
# Ingresar número de mes y mostrar estación del año

mes = int(input("Ingrese el número del mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        print(f"Mes {mes} → Invierno")
    case 3 | 4 | 5:
        print(f"Mes {mes} → Primavera")
    case 6 | 7 | 8:
        print(f"Mes {mes} → Verano")
    case 9 | 10 | 11:
        print(f"Mes {mes} → Otoño")
    case _:
        print("Número no válido. Ingrese un número del 1 al 12.")
