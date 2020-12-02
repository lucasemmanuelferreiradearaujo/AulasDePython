#Aula 105
#Desafio:
'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.
'''
import numpy

def nota(num):
    totalDeNotas = len(num)
    menorNota = min(num)
    maiorNota = max(num)
    mediaNota = numpy.mean(num)
    lista = [totalDeNotas, menorNota, maiorNota, mediaNota]
    return lista

notas = []
while True:
    notas.append(float(input('Digite a nota do aluno: ')))
    if str(input('Continuar: ')) in 'Nn':
        break

dados = nota(notas)
print(dados)