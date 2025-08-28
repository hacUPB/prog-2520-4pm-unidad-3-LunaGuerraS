#Imprimir los numeros pares entre el 20 y el 80
'''
numero = 20
while numero<=80:
    print(numero)
    numero += 2   #Numero = numero + 1
'''

#Imprimir los numeros impares entre 99 y 61, en orden descendente
'''
numero = 99
while numero >= 61:
    print(numero)
    numero -= 2
'''

#Solicitar dos numero al usuario e imprimir los numeros impares entre ellos
'''
numero1 = int(input("Por favor ingrese un número: "))
numero2 = int(input("Por favor ingrese otro número: "))

if numero1 > numero2:
    mayor = numero1
    menor= numero2
else:
    mayor = numero2
    menor = numero1

while menor <= mayor:
    if menor % 2 == 1:
        print(menor)
    menor += 1
'''

#Imprimir los multiplos de 7 entre 0 y 100
'''
numero = 0
while numero <= 100:
    if numero % 7 == 0:
        print(numero)
    numero += 1
'''

#Solicitar un número al usuario e imprimir su tabla de multiplicar hasta 15
'''
numero = (int(input("Por favor, ingrese un número entero: ")))
multiplicar = 1
while multiplicar <= 15:
    resultado = numero * multiplicar
    print(f"{numero} x {multiplicar} = {resultado}")
    multiplicar += 1
'''
