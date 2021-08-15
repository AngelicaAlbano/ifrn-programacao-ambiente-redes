# https://wiki.python.org.br/ExerciciosComStrings questao 12
# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
# e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
# O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

numero_telefone = []
numero_telefone = input('Digite o número de telefone: ')

# remover separador
numero_telefone = numero_telefone.replace('-', '')

print('Número sem formatação: ',numero_telefone)
if(len(numero_telefone) == 7):
    numero_telefone = '3' + numero_telefone
    numero_formatado = numero_telefone[:4] + '-' + numero_telefone[4:]
    print ('Número com formatação: ', numero_formatado)

