import math
import random
from re import T

value = int(input("Defina um valor para ser advinhado: "))
highest = int(input("Defina o valor máximo da área de busca: "))
lowest = int(input("Defina o valor mínimo da área de busca: "))

r = int(random.randrange(lowest, highest))
area = math.ceil((math.log(2, 10) * (highest - lowest))) + 1
j = 0

while j != area:
  print("O número gerado é: ", r)
  take = str(input("Defina se o seu número é maior (>), menor (<), ou se está correto (=): "))
  if j == area:
    print("Você está trapaceando!")
    break

  if take == "=":
    j += 1
    print("Você acertou em ", j, " tentativas.")
    break

  elif take == '>':
    t = random.randrange(take, highest)
    r = t
    j += 1

  elif take == '<':
    t = random.randrange(lowest, take)
    r = t
    j += 1
  
