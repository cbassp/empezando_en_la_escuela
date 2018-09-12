mi_lista = []

input_usuario = ""

while input_usuario != 'FIN':
    input_usuario = input('Que necesitas comprar?\nEscribe FIN para acabar: ').upper()
    if input_usuario != 'FIN':
        mi_lista.append(input_usuario)

largo_lista = len(mi_lista)
indice_actual = 0


while indice_actual < largo_lista:
    print('tengo que comprar {}'.format(mi_lista[indice_actual]))
    indice_actual += 1

#for item in mi_lista:
    #print('tengo que comprar {}'.format(item))
#esto es lo mismo que recorrer la lista con un while.

print('Esta es tu lista de la compra')