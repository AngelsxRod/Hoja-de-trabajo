# Ejercicio 17: Operaciones Matemáticas Avanzadas
# Potencia, raíz cuadrada, módulo o valor absoluto

import math

print("===== OPERACIONES MATEMÁTICAS AVANZADAS =====")
print("1. Potencia")
print("2. Raíz cuadrada")
print("3. Módulo (residuo)")
print("4. Valor absoluto")
print("===============================================")

opcion = int(input("Seleccione una operación: "))

match opcion:
    case 1:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = base ** exponente
        print(f"{base} ^ {exponente} = {resultado}")
    case 2:
        numero = float(input("Ingrese el número: "))
        if numero >= 0:
            resultado = math.sqrt(numero)
            print(f"√{numero} = {resultado}")
        else:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
    case 3:
        num1 = float(input("Ingrese el dividendo: "))
        num2 = float(input("Ingrese el divisor: "))
        if num2 != 0:
            resultado = num1 % num2
            print(f"{num1} % {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    case 4:
        numero = float(input("Ingrese el número: "))
        resultado = abs(numero)
        print(f"|{numero}| = {resultado}")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
