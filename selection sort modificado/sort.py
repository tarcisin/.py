def swap(lyst, i, j):

  temp = lyst[i]
  lyst[i] = lyst[j]
  lyst[j] = temp

def modifiedSelectionSort(reverse, lista):
  
  if reverse == False:
    i = 0
    while i < len(lista) - 1: # Faz n - 1 pesquisas
      minIndex = i # pelo menor
      j = i + 1
      while j < len(lista): # Inicia uma pesquisa
        if lista[j] < lista[minIndex]:
          minIndex = j
        j += 1
      if minIndex != i: # Troca se necessário
        swap(lista, minIndex, i)
    i += 1
    return lista
  else:
    i = 0
    while i < len(lista) - 1: # Faz n - 1 pesquisas
      minIndex = i # pelo menor
      j = i + 1
      while j < len(lista): # Inicia uma pesquisa
        if lista[j] < lista[minIndex]:
          minIndex = j
        j += 1
      if minIndex != i: # Troca se necessário
        swap(lista, minIndex, i)
    i += 1

    revList = []
    for i in range((len(lista))):
      revList.append(lista[(i + 1) * -1])
    return revList

harrypotter = [23, 42, 13, 22, 55, 33, 1, 5, 7, 8, 12, 16, 19, 20, 24, 32, 39, 45]

a = modifiedSelectionSort(False, harrypotter)
