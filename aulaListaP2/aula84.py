"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Um listagem com as pessoas mais pesadas.
C) Uma lista com as pesssoas mais leves.
"""
pesoMaior = []
pesoMenor = []
cont = 0

while True:
    aux = int(input('Qual é o seu peso? '))
    cont+=1
    if aux >= 100:
        pesoMaior.append(aux)
    else:70    
        pesoMenor.append(aux)
    op = str(input('Continuar? [S/N] '))
    if op in 'N':
        break

print(cont)
print(pesoMaior)
print(pesoMenor)