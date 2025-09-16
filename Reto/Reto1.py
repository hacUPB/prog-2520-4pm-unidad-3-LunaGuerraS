# Simulación de consumo de combustible en vuelo.

combustible = int(input("Porfa ingrese la cantidad inicial de combustible en litros: "))
horas = int(input("Ingrese el el número de horas de vuelo: "))
umbral_seguridad = combustible/1000

for hora in range(1, horas + 1):
    consumo = int(input(f"Hora {hora}: Ingrese el consumo de combustible hasta ahora en litros: "))
    combustible -= consumo
    print(f"Después de la hora {hora}, quedan {combustible} litros de combustible.")
    if combustible < umbral_seguridad:
        print("Cuidado!! El combustible está por debajo del umbral de seguridad.")
        emergencia = input("¿Quiere iniciar un aterrizaje de emergencia? (Si/No): ")
        if emergencia() == "si":
            print("Aterrizaje de emergencia iniciado.")
            break
    if combustible <= 0:
        print("¡Emergencia! El avión se ha quedado sin combustible. Intente atterizaje de emerjencia en modo planeo.")
        break
else:
    print("Vuelo completado, Felicitaciones piloto :)")