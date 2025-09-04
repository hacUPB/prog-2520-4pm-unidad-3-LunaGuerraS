print ("Ingrese la zona de envío. Eliga un número.")
zona = int(input("1.Norteamérica\n2. Centroamérica\n3. Suramérica\n.4 Europa\n5. Asia\n Elija un Número: "))

if zona > 0 and zona < 6:
    peso =int(input("Ingrese e peso del paquete en gramos: "))
    if peso <= 5000:
        if zona == 1:
            total = peso * 11
        elif zona == 2:
            total = peso * 10
        elif zona == 3:
            total = peso * 12
        elif zona == 4:
            total = peso * 24
        elif zona == 5:
            total = peso * 27
        print(f"El envío de su paquete cuesta {total}.")
    else:
        print("No se puede enviar paquetes de más de 5 kg.")
else:
    print("La zona ingresada no existe")