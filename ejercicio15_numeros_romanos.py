simbolo = input("Ingrese un símbolo romano (I, V, X, L, C): ").upper()

match simbolo:
    case "I":
        print("I = 1")
    case "V":
        print("V = 5")
    case "X":
        print("X = 10")
    case "L":
        print("L = 50")
    case "C":
        print("C = 100")
    case _:
        print("Símbolo no válido. Ingrese I, V, X, L o C.")
