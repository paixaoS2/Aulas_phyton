    #EXEC 1
number = 0

while True:
    name = str(input('Digite seu nome: '))
    n1 = float(input('Digite sua 1ª nota: '))
    n2 = float(input('Digite sua 2ª nota: '))
    m = (n1 + n2) / 2
    print('Sua média é',(m))
    if(m>=6):
        print('Aluno aprovado')
    elif(m<=4):
        print('Aluno reprovado')
    else:
        print('Aluno em recuperação')
    number = number + 1
    if number == 40:
        break

    #EXEC 2
cont = 100
while True:
    print (cont)
    cont = cont - 1
    if cont == 0:
        break

    #EXEC 3
cont = 0
while True:
    print (cont)
    cont = cont + 2
    if cont == 0:
        break
