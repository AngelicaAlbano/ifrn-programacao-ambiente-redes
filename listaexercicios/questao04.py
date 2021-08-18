'''Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) 
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível 
criar um macaco canibal?'''

class Macaco:
    
    def comer(self, comida):
        if(type(comida) != Macaco):
            self.bucho.append(comida)
            print('Checando bucho de (', self.nome, ')')
            self.ver_bucho()
            return True
        else:
            print('Macacos não são canibais!')
            return False
            
    def ver_bucho(self):
        print('Bucho => ', self.bucho)
        self.digerir()
        
    def digerir(self):
        if(self.comer == False):
            print('Não foi possível digerir.')    
        print('Digestão ok!')    
    
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

macaco1 = Macaco('Julia')
macaco2 = Macaco('George')

print('\nAlimentando Julia')
print(20*'-')
macaco1.comer('Banana')
macaco1.comer('Pêra')
macaco1.comer('Côco')

print('\nAlimentando George')
print(20*'-')
macaco2.comer('Uva')
macaco2.comer('Abacate')
macaco2.comer('Mamão')

print('\nTentando canibalismo')
print(30*'-')
macaco1.comer(macaco2)
macaco2.comer(macaco1)