from conta import *
from cliente import *

print('     Banco')
p = input('Você já tem uma conta?(s/n)\n')

saldo = 0
limite = 500

if p == 'n':
    nome = input('Digite seu nome:\n')
    cpf = int(input('Digite seu cpf:\n'))
    idade= int(input('Digite sua idade:\n'))
    cliente1 = cliente(nome,cpf,idade)
    conta1 = conta(saldo,cliente, limite)

    print('__________________________________')

while True:
    p = input('Digite uma opção:\ndepositar\nsacar\nconsultar_saldo\n=>')
    if p == 'depositar':
        s = float(input('Digite o valor para depositar:\n'))
        conta1.depositar(saldo, s)
        c = input('Mais alguma coisa?(s/n)')
        if c == 'n':
            break

    elif p == 'sacar':
        f = float(input('Digite o valor que deseja sacar:\n'))        
        conta1.sacar(saldo, limite, f)
        c = input('Mais alguma coisa?(s/n)')
        if c == 'n':
            break
        
    else:
        conta1.consultar_saldo(saldo)
        c = input('Mais alguma coisa?(s/n)')
        if c == 'n':
            break







