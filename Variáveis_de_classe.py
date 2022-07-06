class A:
    vc = 123    #Variável de classe.
    
    def __init__(self):
        self.vc = 321   #Variável de instancia.
    
a1 = A()    #Atribuição da "a1" e "a2" é feita somente a variável de instância.
a2 = A()

print(a1.vc)       
print(a2.vc)
print(A.vc)
print('')

A.vc = 200 #Atribuição da "A.vc" é feita somente a variável da classe.

print(a1.vc)   
print(a2.vc)
print(A.vc)
print('')

print(a1.__dict__)       
print(a2.__dict__)
print(A.__dict__)