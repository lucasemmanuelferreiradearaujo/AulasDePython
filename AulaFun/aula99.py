"""
faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*num):
    if num != ():
        max = num[0]
        for c in num:
            if c > max:
                max = c
        print(f'Foram cadastrados {len(num)} valores.')
        print(f'O maior valor foi {max}.')
    else:
        print('Nenhum valor cadastrado.')
        
maior(20,30,40)