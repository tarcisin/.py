import math

iteracoes = int(input("Insira a quantidade de iterações: "))
numIter = 0
denm = 1
marcador = True
for i in range(iteracoes):
  numIter = numIter + 1 / denm if marcador else numIter - 1 / denm
  denm += 2
  marcador = not marcador

pi = numIter * 4
print("O valor aproximadi de pi baseado na aproximação de " + str(iteracoes) + " iterações, é " + str(pi))

