print("===== TIPO DE VEHÍCULO =====")
print("1. Carro")
print("2. Moto")
print("3. Camión")
print("4. Bicicleta")
print("============================")

opcion = int(input("Seleccione un tipo de vehículo: "))

match opcion:
    case 1:
        print("Carro: Vehículo de cuatro ruedas para transporte de pasajeros, capacidad de 2 a 7 personas.")
    case 2:
        print("Moto: Vehículo de dos ruedas, ligero y rápido, ideal para movilidad urbana.")
    case 3:
        print("Camión: Vehículo pesado de carga, utilizado para transporte de mercancías.")
    case 4:
        print("Bicicleta: Vehículo de dos ruedas impulsado por pedales, ecológico y saludable.")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
