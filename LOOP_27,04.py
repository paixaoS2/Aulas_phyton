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

    #EXEC 4
N = 0
for i in range(3):
    num = float(input('Digite um número:\n'))
    if num < 0:
        N += 1
if N == 1:
    print(f'Você digitou 1 valor negativo!!!')
else:
    print(f'Você digitou {N} valores negativos!!!')

    #EXEC 5
nalu = int(input('Quantos alunos exitem nessa turma:\n'))

for i in range(nalu):
    nome = input('Digite o nome do aluno:\n')
    n1 = float(input('Digite a 1ª nota:\n'))
    n2 = float(input('Digite a 2ª nota:\n'))
    m = (n1 + n2) / 2
    print(nome)
    print(f'Sua média é{m}')
    if(m>=6):
        print('Aluno aprovado')
    elif(m<=4):
        print('Aluno reprovado')
    else:
        print('Aluno em recuperação')
    print('----------------------------')

    #EXEC 6
while True:
    n1 = int(input('Digite um número:\n'))
    n2 = int(input('Digite um número:\n'))
    if(n2 > n1):
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')
        break
    
    #EXEC 7

m1 = int(input('Digite o 1º número:\n'))

while True:
    m2 = int(input('Digite o 2º número:\n'))    
    if m2 == 0:
        print('Este valor é inválido, digite-o denovo!!!')
    else:
        div = m1/m2
        print(f'{m1} dividido por {m2} é {div}')
        break

    #EXEC 8
a = 0
b = 0
while True:
    a = float(input('Digite a nota 1a:\n'))
    if (a > 10) or (a < 0):
        print('Esse número é inválido')
    else:
        break
while True:
    b = float(input('Digite a nota 2a:\n'))
    if (b > 10) or (b < 0):
        print('Esse número é inválido')
    else:
        break
med = (a + b)/2
print(f'Sua média é {med}')
