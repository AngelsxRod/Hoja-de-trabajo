# Ejercicio 5: Conversión de Notas
# Ingresar letra (A, B, C, D, F) y mostrar su significado

letra = input("Ingrese una letra de nota (A, B, C, D, F): ").upper()

match letra:
    case "A":
        print("Excelente")
    case "B":
        print("Muy Bueno")
    case "C":
        print("Bueno")
    case "D":
        print("Regular")
    case "F":
        print("Reprobado")
    case _:
        print("Nota no válida. Ingrese A, B, C, D o F.")
