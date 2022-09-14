import time

print("Em que ponto o algoritmo n^4 passa a funcionar melhor do que um algoritmo 2n?")
print("%18s%24s%18s%24s" %("n^4", "2n", "ent1", "ent2"))

ent = 0 #esta variável é o valor de entrada, é a base dos dois cálculos e aumenta em 1 inteiro a cada iteração
ent1 = 0
ent2= 0

ent += 1

print("%12s%16s" %(ent1, ent2))

tempoInit = time.time()

while True:

  for x in range(4):
    ent1 = ent**4
    tempo1 = time.time() - tempoInit
  for x in range(2):
    ent2 = ent * 2
    tempo2 = time.time() - tempoInit
  print("%18s%36s%26s%32s" %(tempo1, tempo2, ent1, ent2))
  ent += 1
  if tempo1 < tempo2:
    break

