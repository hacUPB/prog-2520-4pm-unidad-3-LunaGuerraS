from ModuloReto import *

def menu_principal():
    while True:
        variable = menu()

        match variable:

            case "1":
                print("Has elegido el Problema 1.")
                zonas = int(input("Ingrese el número de zonas de carga del avión: "))

                problema_cg (zonas)

            case "2":
                print("Has elegido el Problema 2.")
                combustible = float(input("Porfa ingrese la cantidad inicial de combustible en litros: "))
                horas = int(input("Ingrese el el número de horas de vuelo: "))
                consumo = int(input(f"Ingrese cuanto combustible se consume por hora, en litros: "))

                problema_combustible(combustible, horas, consumo)

            case "3":
                print("Has elegido el Problema 3.")
                cant_etapas = int(input("Ingrese el número de etapas del cohete: "))
                cant_comb = int(input("Ingrese la cantidad inicial de combustible (m³): "))

                problema_cohete(cant_etapas, cant_comb)

            case "4":

                print("Adios")
                break
            case _:

                print("Opción inválida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    menu_principal()