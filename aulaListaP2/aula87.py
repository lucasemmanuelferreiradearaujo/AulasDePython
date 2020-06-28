'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
somaColuna3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Qual o valor de [{l},{c}]: '))
        if matriz[l][c]%2 == 0:
            par += matriz[l][c]

for c in range(0,3):
    somaColuna3 += matriz[2][c]

maior = matriz[1][0]
if maior < matriz[1][1]:
    maior = matriz[1][1]
if maior < matriz[1][2]:
    maior = matriz[1][2]

print(par)
print(somaColuna3)
print(maior)
        


