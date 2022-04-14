#Exec1
cel = float(input('Digite sua temperatura:'));
if (cel>30):
  print('Perigo de super aquecimento')
else:
  print('Temperatura normal')
  
 #Exec2
nome = str(input('Digite seu nome:'))
Valor = float(input('Digite o valor da sua compra: R$'));
pagamento = str(input('Vai ser pago a vista ou parcelado?'));
print('Nome:',nome);
print('Forma de pagamento:',pagamento);
if(pagamento=='a vista'):
  desconto = (Valor/100*7)
  conta = Valor-(Valor/100*7)
  r_desconto = f"R${desconto:_.2f}"
  r_desconto = r_desconto.replace(".", ",").replace("_", ".")
  print(f'Valor de desconto: {r_desconto}')
  c_desconto = f"R${conta:_.2f}"
  c_desconto = c_desconto.replace(".", ",").replace("_", ".")
  print(f'Valor da compra com desconto: {c_desconto}')
else:
  valorc = f"R${Valor:_.2f}"
  valorc = valorc.replace(".", ",").replace("_", ".")
  print(f'Valor da compra: {valorc}');
