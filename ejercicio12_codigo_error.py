codigo = int(input("Ingrese el código de error/estado: "))

match codigo:
    case 200:
        print("200 - OK: La solicitud se procesó correctamente.")
    case 403:
        print("403 - Prohibido: No tiene permisos para acceder a este recurso.")
    case 404:
        print("404 - No Encontrado: El recurso solicitado no existe.")
    case 500:
        print("500 - Error Interno del Servidor: Ocurrió un error en el servidor.")
    case _:
        print(f"Código {codigo} no reconocido.")
