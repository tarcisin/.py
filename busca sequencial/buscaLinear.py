def pesquisaSeq(lista, alvo):
  for i in range(len(lista)):
    if lista[i] == alvo:
      return i
  return False

lista = [2, 12, 11, 23, 41, 23]
alvo = 23

exec = pesquisaSeq(lista, alvo)

if exec is not False:
  print("O índice do alvo ", alvo, " é ", exec)
else:
  print("O alvo não se encontra na lista")

# O MELHOR CASO É DE O(1), ONDE O ALVO ESTÁ NA PRIMEIRA POSIÇÃO DA LISTA;

# O CASO MÉDIO, POR DESCONSIDERAR CONSTANTES E VALORES QUE MULTIPLICAM N ACABA POR SER O(n);

# O PIOR CASO É O(n), POIS NESTE CASO O ALVO ESTÁ NA ÚLTIMA POSIÇÃO DA LISTA OU NEM MESMO ESTÁ NA LISTA, ENTÃO O ALGORITMO DEVERÁ PERCORRER TODAS AS POSSÍVEIS POSIÇÕES.