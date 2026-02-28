print("===== PLANES TELEFÓNICOS =====")
print("1. Básico")
print("2. Estándar")
print("3. Premium")
print("==============================")

opcion = int(input("Seleccione un plan: "))

match opcion:
    case 1:
        print("\n--- Plan Básico ---")
        print("Precio: Q50/mes")
        print("Beneficios:")
        print("  - 500 MB de datos")
        print("  - 100 minutos de llamadas")
        print("  - 50 SMS")
    case 2:
        print("\n--- Plan Estándar ---")
        print("Precio: Q100/mes")
        print("Beneficios:")
        print("  - 3 GB de datos")
        print("  - Llamadas ilimitadas")
        print("  - SMS ilimitados")
        print("  - Redes sociales gratis")
    case 3:
        print("\n--- Plan Premium ---")
        print("Precio: Q200/mes")
        print("Beneficios:")
        print("  - 10 GB de datos")
        print("  - Llamadas ilimitadas")
        print("  - SMS ilimitados")
        print("  - Redes sociales y streaming gratis")
        print("  - Roaming incluido")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 3.")
