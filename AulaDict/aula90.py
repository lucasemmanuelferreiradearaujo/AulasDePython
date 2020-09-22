'''
Faça um progroma que leia nome e média de um aluno, guardando também a situação[aprovado or nao em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

turma = dict()
turma['nome'] = str(input('Nome: '))
turma['media'] = float(input('Média: '))
if turma['media'] > 6.9:
    turma['situacao'] = 'Aprovado'
else:
    turma['situacao'] ='Reprovado'

print(f"Estudante {turma['nome']} com a média {turma['media']} foi {turma['situacao']}.")
