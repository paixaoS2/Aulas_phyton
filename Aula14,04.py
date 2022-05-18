#Exec1
cel = float(input('Digite sua temperatura:'));
if (cel>30):
  print('Perigo de super aquecimento')
else:
  print('Temperatura normal')
  
 #Exec2
nome = (input('Digite seu nome:\n'))
Valor = float(input('Digite o valor da sua compra: R$'))
while True:
  pagamento = (input('Vai ser pago a vista ou parcelado?\n'))
  if (pagamento == 'a vista') or (pagamento == 'parcelado') or (pagamento == 'xerecard'):
    break
  else:
    print('Forma de pagamento inválida(lembre-se de deixar tudo minúsculo e sem acento!!!)')
print('')
print('---------------------------------------------------')
print('Nome:',nome);
print('Forma de pagamento:',pagamento)

if(pagamento=='a vista'):
  desconto = (Valor/100*7)
  conta = Valor-(Valor/100*7)
  r_desconto = f"R${desconto:_.2f}"
  r_desconto = r_desconto.replace(".", ",").replace("_", ".")
  print(f'Valor de desconto: {r_desconto}')
  c_desconto = f"R${conta:_.2f}"
  c_desconto = c_desconto.replace(".", ",").replace("_", ".")
  print(f'Valor da compra com desconto: {c_desconto}')

if(pagamento=='xerecard'):
  print('Vem descendo safada ( ͡° ͜ʖ ͡°)')

else:
    print('')
    print('---------------------------------------------------')
    parc = int(input('Digite o número de parcelas:\n'))
    valorc = (Valor/parc)
    if (parc > 5)and(parc < 12):
        valorc = (valorc + (valorc/100*5))
        print('Juros: 5%')
        valort = (valorc*parc)
        valort = f"R${valort:_.2f}"
        valort = valort.replace(".", ",").replace("_", ".")
    elif (parc >= 12):
        valorc = (valorc + (valorc/100*10))
        print('Juros: 10%')
        valort = (valorc*parc)
        valort = f"R${valort:_.2f}"
        valort = valort.replace(".", ",").replace("_", ".")

    valorc = f"R${valorc:_.2f}"
    valorc = valorc.replace(".", ",").replace("_", ".")
    if (parc <= 5):
      print(f'Valor da parcela com {parc} meses: {valorc}')
    else:
      print(f'Valor da parcela com {parc} meses: {valorc}')
      print(f'Valor total com juros:{valort}')

