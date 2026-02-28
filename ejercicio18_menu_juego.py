# Ejercicio 18: Menú de Juego
# Iniciar juego, cargar partida, configuración, créditos o salir

while True:
    print("\n===== MENÚ DE JUEGO =====")
    print("1. Iniciar juego")
    print("2. Cargar partida")
    print("3. Configuración")
    print("4. Créditos")
    print("5. Salir")
    print("=========================")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            print("\n¡Iniciando nuevo juego!")
            print("Cargando mundo...")
            print("¡Bienvenido, aventurero! Tu misión comienza ahora.")
        case 2:
            print("\n--- Cargar Partida ---")
            print("Partida 1: Nivel 5 - Bosque Encantado")
            print("Partida 2: Nivel 12 - Castillo Oscuro")
            print("Partida 3: (Vacía)")
            slot = input("Seleccione una partida (1-3): ")
            print(f"Cargando partida {slot}...")
        case 3:
            print("\n--- Configuración ---")
            print("Volumen: ████████░░ 80%")
            print("Brillo:  ██████░░░░ 60%")
            print("Idioma:  Español")
            print("(Configuración simulada)")
        case 4:
            print("\n--- Créditos ---")
            print("Desarrollado por: Estudiante Python")
            print("Versión: 1.0")
            print("Año: 2026")
            print("¡Gracias por jugar!")
        case 5:
            print("\n¡Hasta la próxima, aventurero!")
            break
        case _:
            print("Opción no válida. Seleccione una opción del 1 al 5.")
