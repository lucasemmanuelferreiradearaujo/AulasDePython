'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de aluno individualmente.
'''
Turma =[]
Aluno = []
cont = 1

while True:
    Aluno.append(str(input('Nome: ')))
    Aluno.append(float(input('Nota 1°:')))
    Aluno.append(float(input('Nota 2°:')))
    Turma.append(Aluno[:])
    Aluno.clear()
    print(f'Estudante: de n°{cont} cadastrado.')
    cont +=1
    resp = str(input("Continuar? "))
    if resp in 'Nn':
        break

print('')

while True:
    print('''Nota de todos os alunos[1]
Media de um unico aluno[2]
Sair[999]''')
    resp = int(input('Escolha: '))
    if resp == 999:
        print('Até logo.')
        break
    
    if resp == 1:
        for aluno in range(len(Turma)):
            print(f'Turma A: Estudante {Turma[aluno][0]}, Nota 1: {Turma[aluno][1]}, Nota 2: {Turma[aluno][2]}')

    if resp == 2:
        aux = int(input('Qual o n° do estudante? '))-1
        print(f'Estudante: {Turma[aux][0]}, sua média é {(Turma[aux][1]+Turma[aux][2])/2}')
    
    print('')