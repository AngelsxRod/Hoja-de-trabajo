archivos = ["documento.txt", "imagen.png", "datos.csv"]

while True:
    print("\n===== SISTEMA OPERATIVO (Simulado) =====")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Modificar archivo")
    print("4. Listar archivos")
    print("5. Salir")
    print("=========================================")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            nombre = input("Ingrese el nombre del archivo a crear: ")
            if nombre in archivos:
                print(f"El archivo '{nombre}' ya existe.")
            else:
                archivos.append(nombre)
                print(f"Archivo '{nombre}' creado exitosamente.")
        case 2:
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            if nombre in archivos:
                archivos.remove(nombre)
                print(f"Archivo '{nombre}' eliminado exitosamente.")
            else:
                print(f"El archivo '{nombre}' no existe.")
        case 3:
            nombre = input("Ingrese el nombre del archivo a modificar: ")
            if nombre in archivos:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                indice = archivos.index(nombre)
                archivos[indice] = nuevo_nombre
                print(f"Archivo '{nombre}' renombrado a '{nuevo_nombre}'.")
            else:
                print(f"El archivo '{nombre}' no existe.")
        case 4:
            print("\n--- Archivos en el sistema ---")
            if archivos:
                for i, archivo in enumerate(archivos, 1):
                    print(f"  {i}. {archivo}")
            else:
                print("  No hay archivos.")
        case 5:
            print("Saliendo del sistema operativo...")
            break
        case _:
            print("Opción no válida. Seleccione una opción del 1 al 5.")
