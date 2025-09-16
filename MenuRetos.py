"""
#Crear una carpeta que se llame reto e ingresarle los 3 problemas y comenzar a hacer la tabla de analisis añadiendo el tipo de variable.

#Como estudiante de primer año de Ingeniería Aeronáutica, tu reto es diseñar un programa interactivo en Python que funcione completamente por consola y contenga un **menú principal con cuatro opciones**:

# Opción 1: Problema propuesto por el estudiante
# Opción 2: Problema propuesto por el estudiante
# Opción 3: Problema propuesto por el estudiante
# Salir del programa

#Las **primeras tres opciones** deben ser problemas relacionados con conceptos aeronáuticos generales, fuerzas sobre el avión, conceptos de vuelo, etc.
#¡Tú debes proponer y diseñar cada uno de estos tres problemas!
#El menú debe repetirse hasta que el usuario elija salir.

"""
#Diseñar un programa interactivo en Python que funcione completamente por consola y contenga un **menú principal con cuatro opciones**:

# Problema 1: Simulación de consume de combustibe

# Problema 2: Monitoreo de temperatura de motores

# Problema 3: Simulación de consumo de combustible en un cohete por etapas.

# Opción 4: Salir del programa

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Problema 1: Cálculo del centro de gravedad.")
    print("2. Problema 2: Simulación de consumo de combustible en una aeronave.")
    print("3. Problema 3: Simulación de consumo de combustible en un cohete por etapas.")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")

    match opcion:
        case "1":
            print("Has elegido el Problema 1.")

            # Cálculo del centro de gravedad (CG) de un avión de carga:

            zonas = int(input("Ingrese el número de zonas de carga del avión: "))

            suma_peso = 0
            suma_peso_posicion = 0

            for i in range(1, zonas + 1):
                posicion = float(input(f"Ingrese la posición (en metros) de la zona {i}: "))
                peso = float(input(f"Ingrese el peso cargado (en kg) en la zona {i}: "))
                suma_peso += peso
                suma_peso_posicion += peso * posicion

            if suma_peso == 0:
                print("No se puede calcular el centro de gravedad: el peso total es cero.")
            else:
                CG = suma_peso_posicion / suma_peso
                print(f"El centro de gravedad (CG) calculado es: {CG} metros.")

                # Rango permitido.
                rango_min = 10
                rango_max = 25

                if CG < rango_min or CG > rango_max:
                    print("¡Alerta! El CG está fuera del rango permitido.")
                else:
                    print("El CG está dentro del rango seguro para operar la aeronave")

        case "2":
            print("Has elegido el Problema 2.")

            # Simulación de consumo de combustible en vuelo.

            combustible = int(input("Porfa ingrese la cantidad inicial de combustible en litros: "))
            horas = int(input("Ingrese el el número de horas de vuelo: "))
            pesototal = int(input("Indique cual es el peso total de la aeronave al despegar en kg: "))
            umbral_seguridad = (combustible/pesototal)*100

            for hora in range(1, horas + 1):
                consumo = int(input(f"Hora {hora}: Ingrese el consumo de combustible hasta ahora en litros: "))
                combustible -= consumo
                print(f"Después de la hora {hora}, quedan {combustible} litros de combustible.")
                if combustible <= 0:
                    print("¡Emergencia! El avión se ha quedado sin combustible. Intente atterizaje de emerjencia en modo planeo.")
                    break

                if combustible < umbral_seguridad:
                    print("Cuidado!! El combustible está por debajo del umbral de seguridad.")
                    emergencia = input("¿Quiere iniciar un aterrizaje de emergencia? (Si/No): ")
                    if emergencia.upper() == "SI":
                        print("Aterrizaje de emergencia iniciado.")
                        break
                
            else:
                print("Vuelo completado, Felicitaciones piloto :)")

        case "3":
            print("Has elegido el Problema 3.")

            cant_etapas = int(input("Ingrese el número de etapas del cohete: "))
            cant_comb = int(input("Ingrese la cantidad inicial de combustible (m³): "))
            
            comb_restante = cant_comb
            
            for etapa_actual in range(1, cant_etapas + 1):
                comb_cons = int(input(f"Ingrese combustible consumido en etapa {etapa_actual} (m³): "))
                comb_restante -= comb_cons
                
                mensaje_etapa = (f"Etapa {etapa_actual}: Combustible restante = {comb_restante} m³")
                print(mensaje_etapa)
                
                if comb_restante <= 0:
                    print("Advertencia: El cohete se ha quedado sin combustible")
                    break
            
            input("\nPresione Enter para volver al menú principal...")
        case "4":
            print("Adios")
            break
        case _:
            print("Opción inválida. Por favor, elige una opción del 1 al 4.")     
      
