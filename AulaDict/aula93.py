'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jagodor e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato.
'''

dados={}
cont = 0

dados['nome'] = str(input('Nome do jogador: '))
numero_de_jogos = int(input('Jogou quantos jogos? '))
print('')
for c in range(numero_de_jogos):
    dados[f'jogo{c}'] = aux = int(input(f'Quantos gols fez no jogo {c}: '))
    cont += aux

print(f"O jogador {dados['nome']} fez um total de {cont} gols no campionato atual.\n")
for chave, valor in dados.items():
    if valor != dados['nome']:
        print(f"No {chave} fez {valor} gols.")