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
    self._size += 1

  def pop(self):
    if self.head:
      self._size -= 1
      probe = self.head
      self.head = self.head.next
      return probe.inData
    else:
      raise Exception("ERRO: A pilha não possui conteúdo.")

  def through(self):
    if not self.head:
      raise Exception("ERRO: A pilha não possui conteúdo.")
    else:
      probe = self.head
      while(probe):
        print(probe.inData)
        probe = probe.next

  def __len__(self): # RETORNA O TAMANHO DA LISTA
    return self._size

  def peek(self):
    return self.head

  def isEmpty(self):
    if not self.head:
      return True
    else:
      return False

  def __contains__(self, value):
    if self.isEmpty():
      raise Exception("ERRO: A pilha não possui conteúdo.")
    else:
      probe = self.head
      while probe:
        if probe.inData == value:
          return True
        probe = probe.next
      return False

  def __repr__(self):
    r = ""
    probe = self.head
    while probe:
      r = r + str(probe.inData) + "\n"
      probe = probe.next
    return r
  
  def __str__(self):
    return self.__repr__()

def isPalindrome():
    sentence = input("Insert a sentence: ")
    palindrome = LinkedStack()
    sentence = str(sentence).upper()
    for i in sentence:
        palindrome.push(i)
    count = 0
    for i in sentence:
        if palindrome.pop() != i:
            obj = False
            if not obj:
                print(sentence + " isn't a palindrome!")
            else:
                print(sentence + " is a palindrome!")
            return False
    obj = True  
    if not obj:
        print(sentence + " isn't a palindrome!")
    else:
        print(sentence + " is a palindrome!")
    return True

a = isPalindrome()
    
