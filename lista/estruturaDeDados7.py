import statistics


listLen = int(input("Defina o número de posições da lista: "))

listBase = []

for x in range(listLen):
  listBase.append(int(input("Insira o valor: ")))

listBase.sort()

modo = statistics.mode(listBase)
mediana = statistics.median(listBase)
print(listBase)

print("A moda dos valores inseridos é ", modo, " e a mediana é ", mediana)