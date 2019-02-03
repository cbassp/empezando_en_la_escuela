numero_para_adivinar = 5
numero_del_usuario = int(input('Adivina el numero: '))

if numero_para_adivinar == numero_del_usuario:
    print('has acertado')
else:
    numero_del_usuario = int(input('Adivina el numero: '))
    if numero_para_adivinar == numero_del_usuario:
        print('has acertado')
    else:
        numero_del_usuario = int(input('Adivina el numero: '))
        if numero_para_adivinar == numero_del_usuario:
            print('has acertado')
        else:
            numero_del_usuario = int(input('Adivina el numero: '))
            if numero_para_adivinar == numero_del_usuario:
                print('has acertado')
            else:
                numero_del_usuario = int(input('Adivina el numero: '))
                if numero_para_adivinar == numero_del_usuario:
                    print('has acertado')
                else:
                    print('has superado el numero de intentos')



