# Ejercicio 20: Sistema de Roles
# Mostrar permisos según tipo de usuario (Administrador, Moderador, Usuario, Invitado)

print("===== SISTEMA DE ROLES =====")
print("1. Administrador")
print("2. Moderador")
print("3. Usuario")
print("4. Invitado")
print("============================")

opcion = int(input("Seleccione el tipo de usuario: "))

match opcion:
    case 1:
        print("\n--- Administrador ---")
        print("Permisos:")
        print("  ✔ Crear usuarios")
        print("  ✔ Eliminar usuarios")
        print("  ✔ Modificar configuración del sistema")
        print("  ✔ Gestionar roles y permisos")
        print("  ✔ Acceso total al sistema")
    case 2:
        print("\n--- Moderador ---")
        print("Permisos:")
        print("  ✔ Moderar contenido")
        print("  ✔ Suspender usuarios")
        print("  ✔ Revisar reportes")
        print("  ✔ Editar publicaciones")
        print("  ✘ No puede eliminar usuarios")
    case 3:
        print("\n--- Usuario ---")
        print("Permisos:")
        print("  ✔ Crear publicaciones")
        print("  ✔ Editar su perfil")
        print("  ✔ Comentar")
        print("  ✘ No puede moderar")
        print("  ✘ No puede acceder a configuración del sistema")
    case 4:
        print("\n--- Invitado ---")
        print("Permisos:")
        print("  ✔ Ver contenido público")
        print("  ✘ No puede publicar")
        print("  ✘ No puede comentar")
        print("  ✘ No puede editar perfil")
        print("  ✘ Acceso limitado")
    case _:
        print("Opción no válida. Seleccione una opción del 1 al 4.")
