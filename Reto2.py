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