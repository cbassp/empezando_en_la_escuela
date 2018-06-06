numero_a_adivinar = 0
numero = 1

while numero_a_adivinar != numero:
    numero_a_adivinar = int(input('Introduce un numero para que lo adivinen: '))
    numero = int(input('Adivina el numero: '))
    if numero_a_adivinar == numero:
        print('Bien, has acertado.')
    else:
        print('Mal, sigue intentandolo.')
