'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

ex.:
escreva('Olá, Mundo!)

saída:
~~~~~~~~~~~~~
 Olá, Mundo! 
~~~~~~~~~~~~~
'''

def escreva(texto):
    tamanho = len(texto)+2
    print('~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('~'*tamanho)

escreva('Olá, Mundo!')
escreva('Hi my name is Lucas.')
escreva('La nina.')