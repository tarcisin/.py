from fileinput import filename


fileName = str(input("Insira o nome do arquivo a ser lido: "))
"""O ARQUIVO A SER EXECUTADO NESSE CÓDIGO É O morphine.txt"""


with open(fileName, "r") as fileMain:
  lineNum = len(fileMain.readlines())
  for line in fileMain: 
    print(fileMain.readline())

  print("O número total de linhas é: ", lineNum)
  lineProg = int(input("Defina a linha que deseja acessar: "))

while True:
  currentLine = 0
  if lineProg > 0 and lineProg <= lineNum:
    fileMain = open(fileName, "r")
    for lines in fileMain:
      currentLine += 1
      if currentLine == lineProg:
        print(lines)
        fileMain.close()
        quit()
  if lineProg == 0:
    fileMain.close()
    quit()


