#Aula 106
#Desafio:
'''
Faça um mini-sistema que utilize o intractive Help do Python. O usuário vai digitar o comndo e o manual vai aparecer. Qunado o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.
'''
c = (
    '\033[m',       #0 - sem cor            
    '\033[0;30;41m',#1 - red
    '\033[0;30;42m',#2 - green
    '\033[0;30;43m',#3 - yellow
    '\033[0;30;44m',#4 - blue
    '\033[0;30;45m',#5 - roxo
    '\033[7;30m',#6 - branco
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end="")
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0], end='')

while True:
    titulo('Sitema de ajuda pyhelp', 2)
    comando = str(input("função ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)