'''
faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
'''
def contador(inicio,fim,passo):
    print(f'A contagem começa em {inicio} e terminar em {fim} de {passo} em {passo}.')
    if passo > 0:
        if inicio > fim:
            for c in range(inicio,fim-passo,passo*-1):
                print(c,end=' ')
            print('fim')

        else:
            for c in range(inicio,fim+1,passo):
                print(c,end=' ')
            print('fim')

    else:   
        for c in range(inicio,fim-passo,passo):
            print(c,end=' ')
        print('fim')

contador(1,10,2)
contador(10,0,2)
contador(int(input('Inicio:')),int(input('Fim:')),int(input('passo:')))