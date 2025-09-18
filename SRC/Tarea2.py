#Tarea: cambiar el codigo del ejercicio 4 por el modo de match.

print("Ingrese la zona de envío. Elija un número.")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un Número: "))

if 1 <= zona <= 5:
    peso = int(input("Ingrese el peso del paquete en gramos: "))
    if peso <= 5000:
        match zona:
            case 1:
                total = peso * 11
            case 2:
                total = peso * 10
            case 3:
                total = peso * 12
            case 4:
                total = peso * 24
            case 5:
                total = peso * 27
        print(f"El envío de su paquete cuesta {total}.")
    else:
        print("No se puede enviar paquetes de más de 5 kg.")
else:
    print("La zona ingresada no existe")
