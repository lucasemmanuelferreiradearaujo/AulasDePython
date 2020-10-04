#Aula 101
#Desafio:
'''
Crie um programa que tenha uma função chamada vota() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGATIVO, POSITIVO ou OBRIGATÓRIO nas eleições.
'''
from datetime import datetime
now = datetime.now()

def vota(idade=0):
    idade = now.year-idade
    if idade > 18 and idade < 65:
        return 'Voto OBRIGATORIO'
    if idade < 18 and idade >= 16 or idade > 65:
        return 'Voto OPCIONAL'
    else:
        return 'Voto NEGADO'


print(vota(int(input('Digite o ano de nascimento: '))))
