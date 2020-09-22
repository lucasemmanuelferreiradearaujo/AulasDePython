'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
jogadores['jogador0'] = randint(1,6)
jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)

# A função 'sorted' recebe os ítens do dicionário e ordena
# de acordo com a chave ('key') escolhida, que pode ser
# o primeiro (0) ou o segundo (1) elementos das tuplas

# Caso você queria ordenar decrescentemente, basta
# passar o parâmetro 'reverse=True' para a função 'sorted'

for c, v in sorted(jogadores.items(), key=itemgetter(1), reverse= True):
    print(f'O {c} tirou {v} no dado.')
    sleep(2)