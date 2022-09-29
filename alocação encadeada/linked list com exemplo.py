class Node:

  def __init__(self, inData, next = None):
    self.inData = inData
    self.next = next

class SinglyLinkedStructure:

  def __init__(self,):
    self.head = None
    self._size = 0

  def through(self): # PERCORRE A ESTRUTURA E IMPRIME OS DADOS DAS POSIÇÕES PERCORRIDAS
    if self.head: 
      aux = self.head
      while aux.next:
        print(aux.inData)
        aux = aux.next
      print(aux.inData)
    else:
      raise Exception("O conteúdo da lista está vazio")
  
  def getIndex(self, index): # ENCONTRA ELEMENTO PELO ÍNDICE
    probe = self.head
    while index > 0:
      probe = probe.next
      index -= 1
    return probe.data

  def getValue(self, value): # ENCONTRA ELEMENTO PELO VALOR
    aux = self.head
    while aux.inData != value:
      aux = aux.next
      if aux == None:
        return False
    if aux.inData == value:
      return True

  def addToStart(self, value): # ADICIONA UM ELEMENTO NO INÍCIO
    self.head = Node(value, self.head)
    self._size += 1

  def addToEnd(self, inData): # ADICIONA UM ELEMENTO AO FINAL DA LISTA
    if self.head:
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next   = Node(inData)
    else:
      self.head = Node(inData)
    self._size += 1
  
  def swapForIndex(self, index, input): # SUBSTITUI O ELEMENTO NO INDEX PELO VALOR DO DADO
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("Não é possível encontrar o índice indicado")
    if pointer:
      pointer.inData = input 
    else:
      raise IndexError("Não é possível encontrar o índice indicado")

  def swapForValue(self, targetValue, newItem):
    probe = self.head
    while probe != None and targetValue != probe.inData:
      probe = probe.next
    if probe != None:
      probe.inData = newItem
      return True
    else:
      return False
  
  def insertByIndex(self, index, newItem): # INSERE UM ELEMENTO EM QUALQUER POSIÇÃO DA LISTA
    if self.head is None or index <= 0:
      self.head = Node(newItem, self.head)
    else:
      probe = self.head
      while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
      probe.next = Node(newItem, probe.next)
    self._size += 1
  
  def removeOnStart(self): # REMOVE NO COMEÇO
    removedItem = self.head.inData
    self.head = self.head.next
    self._size -= 1
    return removedItem
    
  def removeOnEnd(self): # REMOVE NO FINAL
    removedItem = self.head.inData
    if self.head.next is None:
      self.head = None
    else:
      probe = self.head
      while probe.next.next != None:
        probe = probe.next
      removedItem = probe.next.inData
      probe.next = None
    return removedItem
  
  def removeByIndex(self, index): # REMOVE EM QUALQUER POSIÇÃO
    if index <= 0 or self.head.next is None:
      removedItem = self.head.inData
      self.head = self.head.next
      return removedItem
    else:
      probe = self.head
      while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
      removedItem = probe.next.inData
      probe.next = probe.next.next
      return removedItem

lista = SinglyLinkedStructure()

lista.addToEnd(5)
lista.addToEnd(6)
lista.addToEnd(7)

lista.addToStart(4)

lista.addToEnd(8)

lista.through()

print(lista.getValue(3))

lista.swapForValue(6, 3)

lista.through()

lista.swapForIndex(4, 6)

lista.through()

lista.swapForIndex(4, 8)
lista.addToStart(3)

lista.through()

lista.insertByIndex(3, 6)

lista.through()

lista.removeOnStart()

lista.removeByIndex(2)

lista.removeOnEnd()
lista.through()