# Ejercicio 8: Conversor de Unidades
# Convertir entre metros/kilómetros y Celsius/Fahrenheit según opción seleccionada

print("===== CONVERSOR DE UNIDADES =====")
print("1. Metros a Kilómetros")
print("2. Kilómetros a Metros")
print("3. Celsius a Fahrenheit")
print("4. Fahrenheit a Celsius")
print("=================================")

opcion = int(input("Seleccione una opción: "))

match opcion:
    case 1:
        metros = float(input("Ingrese los metros: "))
        km = metros / 1000
        print(f"{metros} metros = {km} kilómetros")
    case 2:
        km = float(input("Ingrese los kilómetros: "))
        metros = km * 1000
        print(f"{km} kilómetros = {metros} metros")
    case 3:
        celsius = float(input("Ingrese los grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    case 4:
        fahrenheit = float(input("Ingrese los grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
