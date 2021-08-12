# dd/mm/aaaa 01/08/2021
# retorna em formato extenso 1 de agosto de 2021

import calendar
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

data = input('Digite uma data no formato dd/mm/aaaa: ')

def data_extenso(data):
    dd, mm, yyyy = data.split('/')
    dia = dd
    mes = calendar.month_name[int(mm)].capitalize()
    ano = yyyy
    nova_data = dia+' de '+mes+' de '+ano
    return nova_data

print(data_extenso(data))
