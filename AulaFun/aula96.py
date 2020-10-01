'''
Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(largura, comprimento):
    return largura*comprimento

arrea=area(int(input('Qual a largura? ')),int(input('Qual o comprimento? ')))

print(f'A area é de {arrea} m².')
