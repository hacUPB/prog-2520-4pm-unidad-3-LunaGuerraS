'''
mensaje = "Programación con Python"
numero = int(input("Ingrese el número:"))

for a in range(numero):
    print (f"{a+1}. {mensaje}")
'''

'''
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for a in range(numero + 1):
    if a % 2 == 0:
        suma += a #acumulador como tipo de variable
print(f"La suma de los pares hasta {numero} es {suma}")
'''

a = int(input("Ingresa un número entero positivo: "))

for a in range (1, a + 1):
    for l in range(1, a + 1):
        print (l, end=' ')
    print()