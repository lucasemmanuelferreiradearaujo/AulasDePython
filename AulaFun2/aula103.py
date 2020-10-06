#Aula 103
#Desafio:
'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def ficha(nome,gols):
    if nome in '':
        nome = 'desconhecido'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gols no campionato.')


ficha(str(input('Nome do jogador: ')).strip(' '),str(input('Gols: ')).strip(' '))
