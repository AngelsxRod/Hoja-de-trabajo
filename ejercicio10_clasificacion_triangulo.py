print("===== CLASIFICACIÓN DE TRIÁNGULO =====")
print("1. Equilátero")
print("2. Isósceles")
print("3. Escaleno")
print("=======================================")

opcion = int(input("Seleccione el tipo de triángulo: "))

match opcion:
    case 1:
        print("Triángulo Equilátero: Tiene sus tres lados iguales y sus tres ángulos iguales (60° cada uno).")
    case 2:
        print("Triángulo Isósceles: Tiene dos lados iguales y un lado diferente. Los ángulos de la base son iguales.")
    case 3:
        print("Triángulo Escaleno: Tiene sus tres lados de diferente longitud y sus tres ángulos diferentes.")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 3.")
