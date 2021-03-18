from os import write


for c in range(107,115):
    arquivo = open(f'aula{c}.py','w')
    arquivo.write(f"#Aula {c}\n")
    arquivo.write(f"#Desafio:\n")
    arquivo.write("'''\n\n")
    arquivo.write("'''")