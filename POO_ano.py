from random import randint

class Pessoa:
    ano_atual = 2022
    
    def __init__(self, nome, idade): 
        self.nome = nome             
        self.idade = idade 
        
    def get_ano_nascimento(self):  #Método de Instância: é uma maneira de vincular uma função a um objeto de classe.
        print(self.ano_atual - self.idade) #(precisa receber o parametro self pois ele se refere a instância)
        
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): #Método de classe: precisa estar decorado com o @classmethod
        idade = cls.ano_atual - ano_nascimento         #ele não é referente a instância mas é referente a classe
        return cls(nome, idade)
    
    @staticmethod                    #Método estático: é como uma "Função normal", porém como está dentro da classe
    def gera_id():                   #podemos utilizá-lo com instâncias ou com a classe, mas dentro do corpo dele não
        rand = randint(10000, 19999) #se pode usar self ou cls.
        return rand
    
p1 = Pessoa.por_ano_nascimento('Luiz',1990)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())