from socket import AF_AAL5


def swap(lyst, i, j):

  temp = lyst[i]
  lyst[i] = lyst[j]
  lyst[j] = temp

def modifiedSelectionSort(reverse, lista):
  
  if reverse == False:
    n = len(lista)
    for j in range(n-1):
      minIndex = j
      for i in range(j, n):
        if lista[i] < lista[minIndex]:
          minIndex = i
      if lista[j] > lista[minIndex]:
        aux = lista[j]
        lista[j] = lista[minIndex]
        lista[minIndex] = aux
    return lista
  if reverse == True: 
    n = len(lista)
    for j in range(n-1):
      minIndex = j
      for i in range(j, n):
        if lista[i] < lista[minIndex]:
          minIndex = i
      if lista[j] > lista[minIndex]:
        aux = lista[j]
        lista[j] = lista[minIndex]
        lista[minIndex] = aux
    revList = []
    for i in range((len(lista))):
      revList.append(lista[(i + 1) * -1])
    return revList      