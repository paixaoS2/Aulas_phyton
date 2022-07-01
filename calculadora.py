def calc(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == 'x':
        return x * y
    else:
        return x / y


print('Calculadora do Paixão :3')   
x = int(input('Digite um número:\n'))
while True:
    z = input('Que operação gostaria de usar?\n( +, -, x, %)\n')
    if z == '+' or z == '-' or z == 'x' or z == '%':
        break
    else:
        print('Digite uma operação valida')

y = int(input('Digite outro número:\n'))
        
try:
    res = calc(x,y,z)
    print(f'{x} {z} {y} = {res}')
except:
    print('Esta conta é impossível!!!')




