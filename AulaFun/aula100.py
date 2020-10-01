'''
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vai colocá-los dentro da lista e a segunda funçao vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
'''
from random import randint
numeros = []
def sorteia(nu):
    for c in range(5):
        nu.append(randint(1,10))
    return nu

def somaPar(numeros):
    somadospar = 0
    for c in numeros:
        if c%2 == 0:
            somadospar += c
    if somadospar == 0:
        print('Nenhum numero par foi sorteado.')
    else:
        print(f'A soma dos valores pares foi {somadospar}')

numeros = (sorteia(numeros))[:]
print(f'Os valores sorteados foram {numeros}')
somaPar(numeros)