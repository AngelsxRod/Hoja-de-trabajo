nota = float(input("Ingrese la nota numérica (0-100): "))

if nota < 0 or nota > 100:
    print("Nota no válida. Ingrese un valor entre 0 y 100.")
else:
    # Dividimos entre 10 y convertimos a entero para usar match
    rango = int(nota // 10)

    match rango:
        case 10 | 9:
            print(f"Nota: {nota} → A (Excelente)")
        case 8:
            print(f"Nota: {nota} → B (Muy Bueno)")
        case 7:
            print(f"Nota: {nota} → C (Bueno)")
        case 6:
            print(f"Nota: {nota} → D (Regular)")
        case _:
            print(f"Nota: {nota} → F (Reprobado)")
