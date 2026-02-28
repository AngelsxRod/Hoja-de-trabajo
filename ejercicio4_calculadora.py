num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\n===== OPERACIONES =====")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("=======================")

opcion = int(input("Seleccione una operación: "))

match opcion:
    case 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
