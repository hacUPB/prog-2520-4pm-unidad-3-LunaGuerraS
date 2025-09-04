numero = int(input("Ingresar un numero entero mayor que 1: "))
divisor = numero // 2   #División entera
cont = 0

for i in range(2, divisor +1):
    if numero % 1 == 0:
        cont += 1

if cont == 0:
    print(f"El número {numero} no es primo")
else:
    print(f"{numero} no es primo")
    print(f"Los divisores de {numero} son:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)