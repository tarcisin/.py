fileName = str(input("Insira o nome do arquivo a ser lido: "))
"""O ARQUIVO A SER EXECUTADO NESSE CÓDIGO É O arquivo.py"""

print("{:<25s} {:<16s} {:<4s}".format("Sobrenome", "Salário-Hora", "Horas Trabalhadas"))

with open(fileName, "r") as fileMain:
  for line in fileMain: 
    dados = line.split()
    print('{:<25s} {:<16s} {:<4s}'.format(dados[0], dados[1], dados[2]))

fileMain.close()


