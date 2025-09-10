'''
Función: menu
Parametros de entrada: Ninguno
Ejecución: Imprimir en pantalla 4 opciones diferentes, Solicitar que elija una opción y la guerda en una variable.
Valor de retorno: Opción elegida
'''

def menu():
    print("1. Encabezado\n2. Pantalones\n3. Zapatos\n4. Salir\n")
    opcion = int(input("Elija una opción: "))
    return opcion
elección = menu()
match elección:
    case 1:
        print("Modo 1 seleccionado: Alta Tensión.")
    case 2:
        print("Modo 2 seleccionado: Media Tensión.")
    case 3:
        print("Modo 3 seleccionado: Baja Tensión.")
    case 4:
        print("Modo 3 seleccionado: Baja Tensión.")
    case _:
        print("Modo no válido")