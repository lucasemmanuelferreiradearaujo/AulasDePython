"""
faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*num):
    max = num[0]
    for c in num:
        if c > max:
            max = c
    print(f'O maior valor foi {max}')
        
maior(1)