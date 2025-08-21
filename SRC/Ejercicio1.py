print ()
Nombre = input ("por favor ingrese su nombre: ")
print ("Bienvenido ", Nombre)

#Calcular el indice de Masa corporal
#IMC = peso / estatura ^2

#Leer estatura
estatura = input ("Ingrese su estatura en metros:")
estatura = float(estatura)
#leer peso
peso = input("Ingrese su peso en kilogramos")
peso = float(peso)
#Calcular imc
IMC = peso / estatura ** 2
#Mostrar IMC
print ("Su IMC = ", IMC)

#Cuando este en peso bajo
if IMC < 18.49:
    print("Está en sobre peso")
else:
    if IMC < 24.99:
        print("Está en un peso normal")
    else:
        if IMC < 29.99:
            print("Está en sobrepeso")
        else:
            if IMC < 39.99:
                print("Está en obesidad")
            else:
                print ("Esta en obesidad extrema")

#TAREA
#Crear un archivo.md en el mismo repositorio fuera de la carpeta SRC y
#Crear las siguientes tablas
#Operadores arirmeticos
#Operacionees relacionales
#Tipos de datos en Python
