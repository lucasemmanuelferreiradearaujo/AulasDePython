#Aula 104
#Desafio:
'''
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input()do Python, só que fazendo a validação para aceitar apenas um valor numérico.

Ex: n=leiaint('Digite um n')
'''


def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            return n
        else:
            print('\033[0;31mErro! Digite um n° valido.\033[m')
            

print(f"Você acabou de digitar o n° {leiaint('Digite um n°: ')}")