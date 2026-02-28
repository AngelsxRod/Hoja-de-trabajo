# Ejercicio 14: Menú Bancario Completo
# Consultar saldo, Depositar, Retirar, Transferir o Salir (actualizando saldo)

saldo = 1000.00

while True:
    print("\n===== MENÚ BANCARIO =====")
    print(f"Saldo actual: Q{saldo:.2f}")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Salir")
    print("=========================")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            print(f"\nSu saldo disponible es: Q{saldo:.2f}")
        case 2:
            monto = float(input("Ingrese el monto a depositar: Q"))
            if monto > 0:
                saldo += monto
                print(f"Depósito exitoso. Nuevo saldo: Q{saldo:.2f}")
            else:
                print("El monto debe ser mayor a 0.")
        case 3:
            monto = float(input("Ingrese el monto a retirar: Q"))
            if monto > 0 and monto <= saldo:
                saldo -= monto
                print(f"Retiro exitoso. Nuevo saldo: Q{saldo:.2f}")
            elif monto > saldo:
                print("Fondos insuficientes.")
            else:
                print("El monto debe ser mayor a 0.")
        case 4:
            cuenta = input("Ingrese el número de cuenta destino: ")
            monto = float(input("Ingrese el monto a transferir: Q"))
            if monto > 0 and monto <= saldo:
                saldo -= monto
                print(f"Transferencia de Q{monto:.2f} a la cuenta {cuenta} realizada.")
                print(f"Nuevo saldo: Q{saldo:.2f}")
            elif monto > saldo:
                print("Fondos insuficientes para la transferencia.")
            else:
                print("El monto debe ser mayor a 0.")
        case 5:
            print("Gracias por usar nuestro servicio bancario. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Seleccione una opción del 1 al 5.")
