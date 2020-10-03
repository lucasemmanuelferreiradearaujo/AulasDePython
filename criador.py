from os import write


for c in range(1,7):
    arquivo = open(f'aula10{c}.py','w')
    arquivo.write(f"#Aula 10{c}\n")
    arquivo.write(f"#Desafio:\n")
    arquivo.write("'''\n\n")
    arquivo.write("'''")