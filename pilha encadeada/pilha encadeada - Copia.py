class Node:

  def __init__(self, inData, next = None):
    self.inData = inData
    self.next = next

class LinkedStack:

  def __init__(self):
    self.morroDoMendanha = None
    self._size = 0
  
  def push(self, value):
    if not self.morroDoMendanha:
      self.morroDoMendanha = Node(value)
    else:
      res = Node(value, self.morroDoMendanha)
      self.morroDoMendanha = res
    self._size += 1

  def pop(self):
    if self.morroDoMendanha:
      self._size -= 1
      probe = self.morroDoMendanha
      self.morroDoMendanha = self.morroDoMendanha.next
      return probe.inData
    else:
      raise Exception("ERRO: A pilha não possui conteúdo.")

  def through(self):
    if not self.morroDoMendanha:
      raise Exception("ERRO: A pilha não possui conteúdo.")
    else:
      probe = self.morroDoMendanha
      while(probe):
        print(probe.inData)
        probe = probe.next

  def __len__(self): # RETORNA O TAMANHO DA LISTA
    return self._size

  def peek(self):
    return self.morroDoMendanha

  def __contains__(self, value):
    if self.morroDoMendanha:
      probe = self.morroDoMendanha
      while probe:
        if probe.inData == value:
          return True
        probe = probe.next
      return False
    else:
      raise Exception("ERRO: A pilha não possui conteúdo.")

  def __repr__(self):
    r = ""
    probe = self.morroDoMendanha
    while probe:
      r = r + str(probe.inData) + "\n"
      probe = probe.next
    return r
  
  def __str__(self):
    return self.__repr__()
    
pilha = LinkedStack()

pilha.push(5)
pilha.push(4)
pilha.push(3)
pilha.push(2)
pilha.push(1)


print(pilha.__str__())
