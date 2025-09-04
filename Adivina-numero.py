from random import randint

'''
Variable de entrada
Nombre  Tipo
gess    int

Variable de salida
Intentos    int

Variable de control
Numero  int
'''

num_aleatorio = randint(1,100)

intentos = 0
gess = -1   #Esto obliga al while a ser falso y actuar la primera vez

while gess != num_aleatorio:
    gess = int(input("Adivina un número oculto entre 1 y 100: "))
    intentos += 1
    if gess > num_aleatorio:
        print("El numero oculto es menor ")
    elif gess < num_aleatorio:
        print("El numero oculto es mayor ")
    else:
        print(f"Felicidades, adivinaste en numero era {num_aleatorio}")
    
print(f"Adivinaste en {intentos} intentos..")

