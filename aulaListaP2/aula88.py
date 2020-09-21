'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint

jogos = int(input('Quantos jogos? '))
lista_de_jogos = list()
lista_total_de_jogos = []
for i in range(jogos):
    for c in range(6):
        lista_de_jogos.append(randint(1,60))
    lista_total_de_jogos.append(lista_de_jogos[:])
    lista_de_jogos.clear()

for jogo in range(len(lista_total_de_jogos)):
    print(f'Jogo {jogo+1}°')
    print(lista_total_de_jogos[jogo])
