import time

lista = open('lista de compras.txt', 'w')

lista.write('       Lista de compras:\n')

print('Por aqui você pode criar sua lista de compras')
time.sleep(1)
print('O que você irá comprar no mercado?(digite só quando acabar)')

while True:
    C = input('')
    if C == 'só':
        break
    else:
        lista.write(C + '\n')

print('Sua lista está salva!!!')
    





        

