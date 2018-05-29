quiere_arepa_input = input("¿Quiere arepa?: Si/No ").upper()

'quiero que el usuario siempre me diga que SI o que NO'

if quiere_arepa_input == 'SI':
    quiere_arepa = True
elif quiere_arepa_input == 'NO':
    quiere_arepa = False
else:
    print('No entiendo lo que me dice, respondea SI o NO. Esto lo tomare como un NO.')

tiene_virutita_input = input("¿Tiene virutita?: Si/No ").upper()
esta_arepero_input = input("¿Esta el arepero?: Si/No ").upper()
esta_pablo_input = input('¿Esta con Pablo?: Si/No ').upper()


tiene_virutita = tiene_virutita_input == 'SI'
esta_pablo = esta_pablo_input == 'SI'
puede_permitirselo = tiene_virutita or esta_pablo
esta_arepero = esta_arepero_input == 'SI'

if quiere_arepa and esta_arepero and puede_permitirselo:
    print('Tome su arepa pepiada.')
else:
    print('Vayase.')