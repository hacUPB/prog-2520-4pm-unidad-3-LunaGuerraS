def problema_cg (zonas:int):
    peso_total = 0
    momento = 0
    for i in range(1, zonas + 1):
        distancia = float(input(f"Ingrese la distancia desde el datum a la zona {i} en pulgadas: "))
        peso = float(input(f"Ingrese el peso cargado en la zona {i} en libras: "))
        peso_total += peso
        momento += peso * distancia
        momento_total += momento
    if peso_total == 0:
        print("No se puede calcular el centro de gravedad: el peso total es cero.")
    else:
        CG = momento_total / peso_total
        print(f"El centro de gravedad (CG) calculado es: {CG}")
        rango_min = 140
        rango_max = 157
        if CG < rango_min or CG > rango_max:
            print("¡Alerta! El CG está fuera del rango permitido.")
        else:
            print("El CG está dentro del rango seguro para operar la aeronave, feliz vuelo :D")

def problema_combustible(combustible, horas, consumo):
    umbral_seguridad = combustible*0.25

    for hora in range(1, horas + 1):
            combustible -= consumo*hora
            print(f"Después de la hora {hora}, quedan {combustible} litros de combustible.")
            if combustible <= 0:
                print("¡Emergencia! El avión se ha quedado sin combustible. Intente atterizaje de emerjencia en modo planeo.")
                break
            if combustible <= umbral_seguridad:
                print("Cuidado!! El combustible está por debajo del umbral de seguridad.")
                emergencia = input("¿Quiere iniciar un aterrizaje de emergencia? (Si/No): ")
                if emergencia.upper() == "SI":
                    print("Aterrizaje de emergencia iniciado.")
                    break
            else:
                print("Vuelo completado, Felicitaciones piloto :D")

def problema_cohete(cant_etapas, cant_comb):

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

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Problema 1: Cálculo del centro de gravedad.")
    print("2. Problema 2: Simulación de consumo de combustible en una aeronave.")
    print("3. Problema 3: Simulación de consumo de combustible en un cohete por etapas.")
    print("4. Salir")
    opcion = input("Elige una opción (1-4): ")