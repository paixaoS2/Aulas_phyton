class conta:
    def __init__(self, saldo,cliente, limite):
        self.limite = limite
        self.saldo = saldo
        self.cliente = cliente
        
           
    def sacar(self,saldo, limite, f):
        if f < saldo or f < limite:
            self.saldo -= f
            print(f'Valor sacado com sucesso\n Seu saldo é de R$:{self.saldo}')
        else:
            print('Não foi possível completar o saque!!!')
        
    def depositar(self,saldo, s):
        self.saldo += s
        print(f'Você depositou R${s}\n Seu saldo é de R$:{self.saldo}')
    
    def consultar_saldo(self,saldo):
        print(f'Seu saldo é de R$:{self.saldo}')
        