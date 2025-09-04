# Determinar si un numero es par o impar
#Leer numero
numero = int(input("Ingresa un numero entero: "))
residuo = numero % 2
#Si residuo es 0 es par
if residuo == 0 :
    print(numero, "Es par")
else:
    print(numero, "Es impar")
    