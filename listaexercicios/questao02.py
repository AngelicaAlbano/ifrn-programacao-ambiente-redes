''' Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra
o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''

quantidadeMouse = 0
situacao = [['necessita da esfera',0],['necessita de limpeza',0],['necessita troca do cabo ou conector',0],['quebrado ou inutilizado',0]]

total =0

def main():
    numMouse = 0
    while True:
        print ('''   
        Situação do mouse.                        
        1- necessita da esfera 
        2- necessita de limpeza
        3- necessita troca do cabo ou conector 
        4- quebrado ou inutilizado 
        0- para encerrar o programa
        ''')
        numMouse += 1
        print('Digite o número correspondente a situação do mouse de número: ',numMouse)
        opcao = int(input('Opção: '))
        
        if opcao == 1: # Esfera
            situacao[0][1] = situacao[0][1] + 1 
        elif opcao == 2:# Limpeza
            situacao[1][1] = situacao[1][1] + 1 
        elif opcao == 3:# Troca
            situacao[2][1] = situacao[2][1] + 1 
        elif opcao == 4:# Quebrado
            situacao[3][1] = situacao[3][1] + 1 
        elif opcao == 0:# bye bye
            print('encerrando programa.')
            break
        else:
            print('Digite uma opção valida.')
    
    
    total = situacao[0][1] +situacao[1][1] +situacao[2][1] +situacao[3][1]
    
    print('\nSituação do mouse.                      | Quantidade | % Percentual |')
    print('1- Necessita da esfera                   ',situacao[0][1], '\t\t', situacao[0][1]/total *100)
    print('2- Necessita de limpeza                  ',situacao[1][1], '\t\t', situacao[0][1]/total *100)
    print('3- Necessita troca do cabo ou conector   ',situacao[2][1], '\t\t', situacao[0][1]/total *100)
    print('4- Quebrado ou inutilizado               ',situacao[3][1], '\t\t', situacao[0][1]/total *100)
    print('\nTotal                                    ',total)


if __name__ == "__main__":
    main()
