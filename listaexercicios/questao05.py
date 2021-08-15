# https://wiki.python.org.br/ExerciciosClasses questao 11

class Carro:
    
    def andar(self, distancia):
        if(distancia >= self.consumo):
            print('Não temos combustível suficiente para esse percurso.')
            return False
        for km in range(1,distancia+1):
            distancia-=1
            if(km%15==0): # a cada 15km gasta 1L de combustivel
                self.nivelCombustivel-=1
        print('Concluímos o percurso.')
        return True
        
    def adicionar_gasolina(self, litros):
        self.nivelCombustivel += litros
        self.consumo = litros * 15
        print('Abasteceu ', litros, 'litros.')
        return True
    
    def obter_gasolina(self):
        print('Nível de combustível')
        return self.nivelCombustivel
    
    def __init__(self):
        self.nivelCombustivel = 0
        self.consumo = self.nivelCombustivel*15 # km por L

fusca = Carro()
print(fusca.adicionar_gasolina(20))
print(fusca.obter_gasolina())
print(fusca.andar(100)) 
print(fusca.andar(301)) # testar validação - quando o combustível não é suficiente pro percurso
print(fusca.obter_gasolina())
