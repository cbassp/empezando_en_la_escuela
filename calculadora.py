operacion_a_realizar = input('¿Que operacion quieres realizar: multiplicacion / suma / resta / division: ').upper()
numero_uno = int(input('Dime un primer numero: '))
numero_dos = int(input('Dime un segundo numero: '))

if operacion_a_realizar == 'MULTIPLICACION':
    print('La {} de {} y {} es: {}'.format(operacion_a_realizar, numero_uno, numero_dos, (numero_uno * numero_dos)))

elif operacion_a_realizar ==  'SUMA':
    print('La {} de {} y {} es: {}'.format(operacion_a_realizar, numero_uno, numero_dos, (numero_uno + numero_dos)))

elif operacion_a_realizar ==  'RESTA':
    print('La {} de {} y {} es: {}'.format(operacion_a_realizar, numero_uno, numero_dos, (numero_uno - numero_dos)))
    
elif operacion_a_realizar ==  'DIVISION':
    print('La {} de {} y {} es: {}'.format(operacion_a_realizar, numero_uno, numero_dos, (numero_uno / numero_dos)))