    #EXEC 1
def Epart(n1):
  if n1 % 2 == 0:
    return 'O número é par!!!'
  else:
    return 'O número é impar!!!'

n1 = int(input('Digite o número:\n'))
print (Epart(n1))

    #EXEC 2
def area(b,a):
  calc = b * a
  return calc

a = int(input('Digite a altura:\n'))
b = int(input('digite a largura:\n'))
print (f'Sua área será: {area(b,a)}')