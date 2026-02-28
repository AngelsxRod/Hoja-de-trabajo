# Ejercicio 19: Clasificación de Figuras
# Mostrar fórmula del área según figura (Círculo, Cuadrado, Rectángulo, Triángulo)

import math

print("===== CLASIFICACIÓN DE FIGURAS =====")
print("1. Círculo")
print("2. Cuadrado")
print("3. Rectángulo")
print("4. Triángulo")
print("=====================================")

opcion = int(input("Seleccione una figura: "))

match opcion:
    case 1:
        print("\nFigura: Círculo")
        print("Fórmula del área: A = π × r²")
        radio = float(input("Ingrese el radio: "))
        area = math.pi * radio ** 2
        print(f"Área = π × {radio}² = {area:.2f}")
    case 2:
        print("\nFigura: Cuadrado")
        print("Fórmula del área: A = lado²")
        lado = float(input("Ingrese el lado: "))
        area = lado ** 2
        print(f"Área = {lado}² = {area:.2f}")
    case 3:
        print("\nFigura: Rectángulo")
        print("Fórmula del área: A = base × altura")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = base * altura
        print(f"Área = {base} × {altura} = {area:.2f}")
    case 4:
        print("\nFigura: Triángulo")
        print("Fórmula del área: A = (base × altura) / 2")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = (base * altura) / 2
        print(f"Área = ({base} × {altura}) / 2 = {area:.2f}")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
