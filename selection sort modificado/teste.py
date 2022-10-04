def swap(lyst, i, j):
 temp = lyst[i]
 lyst[i] = lyst[j]
 lyst[j] = temp

def modifiedSelectionSort(lyst):
  i = 0
  while i < len(lyst) - 1: # Faz n - 1 pesquisas
    minIndex = i # pelo menor
    j = i + 1
    while j < len(lyst): # Inicia uma pesquisa
      if lyst[j] < lyst[minIndex]:
        minIndex = j
      j += 1
    if minIndex != i: # Troca se necessário
      swap(lyst, minIndex, i)
      i += 1

harrypotter = [23, 42, 13, 22, 55, 33, 1, 5, 7, 8, 12, 16, 19, 20, 24, 32, 39, 45]

a = modifiedSelectionSort(harrypotter)