from node import Node

class SinglyLinkedStructure:

  def __init__(self):
    self.head = None
    self._size = 0
  
  def append(self, inData): # ADICIONA UM ELEMENTO AO FINAL DA LISTA
    if self.head:
      pointer = self.head
      while(pointer.next):
        pointer = pointer.next
      pointer.next   = Node(inData)
    else:
      self.head = Node(inData)
    self._size += 1
  
  def __len__(self): # RETORNA O TAMANHO DA LISTA
    return self._size
  
  def __getitem__(self, index): # OBTÉM O ITEM DE DETERMINADA POSIÇÃO
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("Não é possível encontrar o índice indicado")
    if pointer:
      return pointer.inData 
    raise IndexError("Não é possível encontrar o índice indicado")

  def __setitem__(self, index, input): # DEFINE OU ALTERA O CONTEÚDO DE DETERMINADA POSIÇÃO
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

  def index(self, value):
    index = 0
    if self.head:
      if self.head.inData == value:
        return index
      else:
        probe = self.head
        while probe:
          if probe.inData == value:
            return index
          else:
            index += 1
            probe = probe.next
          raise Exception("O item buscado não está na lista;")
    else:
      raise Exception("O conteúdo da lista está vazio")

  def through(self): # PERCORRE A ESTRUTURA E IMPRIME OS DADOS DAS POSIÇÕES PERCORRIDAS
    if self.head: 
      aux = self.head
      while aux.next:
        print(aux.inData)
        aux = aux.next
      print(aux.inData)
    else:
      raise Exception("O conteúdo da lista está vazio")

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
    else:
      probe = self.head
      for i in range(index - 1):
        probe = probe.next
      probe.next = probe.next.next

  def removeByValue(self, value):
    if self.head.inData == value:
      self.head = self.head.next
    else:
      probe = self.head
      while probe.next.inData != value:
        probe = probe.next
      probe.next = probe.next.next
      



  
lista = SinglyLinkedStructure()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)

lista.removeByValue(5)

lista.through()
