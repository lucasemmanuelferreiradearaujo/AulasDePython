'''
Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dict e todos os dict em uma list. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima da média.
'''

dados = {}
lista = []
listamulher=[]
idademedia = []

print('-=-'*20)

while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: '))
        if dados['sexo'] in 'mMFf':
            break
        else:
            print('Por favor digite: M ou F para o sexo.')
    dados['idade'] = int(input('Idade: '))

    lista.append(dados.copy())

    if str(input('continuar: ')) in 'Nn':
        break

media = 0
for c in lista:
    media += c['idade']
    if c['sexo'] in 'Ff':
        listamulher.append(c.copy())
    
media = media/len(lista)

for c in lista:
    if c['idade'] > media:
        idademedia.append(c.copy())

print('-=-'*20)

print(f'A) Total de pessoas cadastras {len(lista)}.\n')

print(f'B) A média de idade do grupo é de {media:.2f} anos de idade.\n')

print(f'C) O total de mulheres cadastradas foi {len(listamulher)}.')
if len(listamulher) != 0:
    for v in listamulher:
        print(f"{v['nome']} com {v['idade']} anos de idade.")

print('')
print(f'D) O total de pessoas com a idade acima da média foi {len(idademedia)}.')
if len(idademedia) != 0:
    for v in idademedia:
        print(f"{v['nome']} com uma idade de {v['idade']}.")

print('-=-'*20)
