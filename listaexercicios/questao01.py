# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outrobro','Novembro','Dezembro']
temperaturas = [] # Armazena as temperaturas de cada mes.
mediaAno = 0 # Media Anual temperatura

def temperaturaPorMes ():
    print('Para calcular a temperatura média anual será nescessário informar a tempertura média por mês. \n')
    for mes in meses : 
        temp = int(input('Digite a temperatura média do mes de ' + mes +' :'))
        TemperaturaMediaMes = [mes,temp] # 
        temperaturas.append(TemperaturaMediaMes)
    mediaTemperaturaAnual()

def mediaTemperaturaAnual():
    global mediaAno # Media Anual temperatura
    mediaAnual = 0
    print('\n |-----------------------------------------------|')
    for i in range(len(temperaturas)):  
        mediaMes = int(temperaturas[i][1])
        mediaAnual = mediaAnual + mediaMes
    mediaAno = round( mediaAnual / 12)
    print('A temperatura média anual é: ',mediaAno,' graus.')
    mesAcimaDaMediaAnual()
    
def mesAcimaDaMediaAnual():
    tempAcimaMedia = []
    global mediaAno
    for temp in temperaturas:  
        if temp[1] > mediaAno:
            tempAcimaMedia.append(temp)
    for temp in tempAcimaMedia:
        print('A temperatura do mes de ',temp[0],' é de ',temp[1],' graus, acima da media anual que é ',mediaAno,'.')
        
        
if __name__ == "__main__":
    temperaturaPorMes()
