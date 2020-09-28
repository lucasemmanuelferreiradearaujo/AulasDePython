'''
Aprimore o desafio 93 paraque ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
dados_jogadores = []
cadastro_dados = {}


while True:
    cadastro_dados['nome'] = str(input('Nome do jogador: '))
    numero_de_jogos = int(input('Jogou quantos jogos? '))
    print('')
    cadastro_dados['totalGols'] = 0
    for c in range(numero_de_jogos):
        cadastro_dados[f'jogo {c}'] = aux = int(input(f'Quantos gols fez no jogo {c}: '))
        cadastro_dados['totalGols'] += aux
    dados_jogadores.append(cadastro_dados.copy())
    cadastro_dados.clear()
    if str(input('Continuar? ')) in 'Nn':
        break
print('-'*60)
print(f'Tabela de jogadores:')
print('-'*60)
for c in dados_jogadores:
    print(f"O jogador {c['nome']} fez um total de {c['totalGols']} gols no campionato atual.")
    for chave, valor in c.items():
        if valor != c['nome'] and valor != c['totalGols']:
            print(f"No {chave} fez {valor} gols.")
    print('-'*60)
