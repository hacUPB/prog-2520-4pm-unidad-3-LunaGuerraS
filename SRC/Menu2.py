#Utilizamos una variable tipo booleana -> una bandera
control = True

while True: #Bucle infinito. Se rompe con break
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opción = int(input("Elija una opción: "))

    match opción:
        case 1:
            print("1. Patacón con suero")
            print("2. Yuca con chicharron")
            print("3. Platano amarillo con suero y queso")
            print()
            opc1 = int(input("Ingrese su elección"))
            match opc1:
                case 1:
                    print("$1000000")
                case 2:
                    print("$1500000")
                case 3:
                    print("$2000000")
            print()
        case 2:
            print("1. Carne asada")
            print("2. Chicharrón")
            print("3. Mojarra frita")
            print()
            opc1 = int(input("Ingrese su elección"))
            match opc1:
                case 1:
                    print("$1000000")
                case 2:
                    print("$1500000")
                case 3:
                    print("$2000000")
            print()
        case 3:
            print("1. Limonada")
            print("2. Michelada")
            print("3. Jugos naturales")
            print()
            opc1 = int(input("Ingrese su elección"))
            match opc1:
                case 1:
                    print("$1000000")
                case 2:
                    print("$1500000")
                case 3:
                    print("$2000000")
        case 4:
            print("1. Arroz de leche")
            print("2. Tres leches")
            print("3. Brownies")
            print()
            opc1 = int(input("Ingrese su elección"))
            match opc1:
                case 1:
                    print("$1000000")
                case 2:
                    print("$1500000")
                case 3:
                    print("$2000000")
        case 5:
            break
        case _:
            print("Opción no disponible")
            print()
            
#Traer 3 problemas (enunciado) que tenga que ver con esto. Para RETO.