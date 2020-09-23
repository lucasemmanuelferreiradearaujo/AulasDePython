'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario se por acaso a CTPS for diferente de ZERO, o diconario recebera também o ano de contratação e o salario. Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar.
'''
import datetime

dados =dict()
hj = datetime.date.today()

 
dados['nome'] = str(input('Nome: '))
dados['ano'] = int(input('Ano de nascimento: '))
dados['carteira'] = int(input('CTPS: '))

if dados['carteira'] <= 0:
    del dados['carteira']
else:
    dados['anoContrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = 32 - (hj.year - dados['anoContrato'])

dados['ano'] = hj.year - dados['ano']

for chave, valor in dados.items():
    print(f'chave = {chave}, valor = {valor}')