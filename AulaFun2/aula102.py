#Aula 102
#Desafio:
'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o n° a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(num=1, show=False):
    if show:
        n_fat = 1
        print('Começando...', end=' ')
        for i in range(2,num+1):
            n_fat = n_fat * i
            print(n_fat,end=' ')
        print('!')
    else:
        n_fat = 1
        for i in range(2,num+1):
            n_fat = n_fat * i

        print(f'{n_fat}!')
fatorial(int(input('Valor: ')),show=True)
