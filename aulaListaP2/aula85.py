"""
Crie um programa onde o usuário possa digitr sete valores numéricos e cadastre-os em uma lista únicas que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
"""

numeros = []
aux3 = []
aux2 = []

for pessoas in range(0,7):
    aux = int(input('Digite um valor: '))
    if aux%2 == 0:
        aux2.append(aux)
    else:
        aux3.append(aux)

numeros.append(aux2)
numeros.append(aux3)
numeros.sort()
print(numeros)