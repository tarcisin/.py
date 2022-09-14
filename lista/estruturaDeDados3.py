alturaOrig = float(input("Insira a altura de que a bola foi jogada: "))
razaoKick = 0.6
alturaAtual = alturaOrig * razaoKick
distanciaTotal = alturaOrig + alturaAtual

aprKick = int(input("Determine a quantidade de vezes em que a bola deve quicar: "))

kicksTotais = 1
for i in range(aprKick):
  kicksTotais = kicksTotais + 1
  distanciaTotal = alturaOrig + alturaAtual
  alturaAtual * 0.6
  
print("A distância total percorrida pela bola foi de ", distanciaTotal, ".\n")
print("A quantidade total de kicks da bola foi de: ", kicksTotais)
