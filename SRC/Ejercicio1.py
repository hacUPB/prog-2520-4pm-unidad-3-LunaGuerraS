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
elif IMC < 24.99:
    print("Está en un peso normal")
elif IMC < 29.99:
    print("Está en sobrepeso")
elif IMC < 39.99:
    print("Está en obesidad")
else:
    print ("Esta en obesidad extrema")

print(f"{Nombre}, tu IMC es de {IMC:0.2f}")