from mimetypes import init
from re import T
import time

print("%18s%24s%28s%28s" %("n²", "1/2 n² + 1/2 n", "valor de operação A", "valor de operação B"))

entrada = 0 

tempoInit = time.time()  # marca o inicio do loop para definir o tempo em que a busca será feita

while True: #este valor é definido como True para manter um loop constante, mas deve ser determinado em uma medida para calcular o limite da busca, como o valor "entrada"

  for x in range(2):
    a = entrada * entrada
    tempoA = time.time() - tempoInit
  for x in range(2):
    bE = entrada * entrada
    bF = bE * 1 / 2
    bS = entrada * 1 / 2
    b = bF + bS
    tempoB = time.time() - tempoInit
  print("%18s%36s%26s%32s" %(tempoA, tempoB, a, b))
  entrada += 1
  similar = []
  if a == b: # esta condicional adiciona cada valor de entrada (n) em que o valor de trabalho dos algoritmos se iguala
    similar.append(entrada)
  
