class Node:

  def __init__(self, inData, next = None):
    self.inData = inData
    self.next = next

class LinkedStack:

  def __init__(self):
    self.head = None
    self._size = 0
  
  def push(self, value):
    if not self.head:
      self.head = Node(value)
    else:
      res = Node(value, self.head)
      self.head = res

  def pop(self):
    if self.head:
      return self.head
    else:
      raise Exception("ERRO: A pilha não possui conteúdo.")

  def through(self):
    if not self.head:
      raise Exception("ERRO: A pilha não possui conteúdo.")
    else:
      probe = self.head
      while(probe):
        print(probe.inData, "\n")
        probe = probe.next