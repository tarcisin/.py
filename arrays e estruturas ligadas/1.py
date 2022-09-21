from operator import getitem


class Array:

  def __init__(self, capacity, fillValue = None, logicalSize = 0):
    self.items = list()
    for count in range(capacity):
      self.items.append(fillValue)
  
  def __len__(self):  
      return len(self.items)

  def __str__(self):
    return str(self.items)

  def __iter__(self):
    return iter(self.items)

  def __getitem__(self, index):
    if 0 <= index < len(self.items):
      return self.items[index]
    raise Exception("O índice definido não está contido no domínio de posições do array")

  def __setitem__(self,index,newItem):
    if 0 <= index < len(self.items):
      self.items[index]=newItem
    raise Exception("O índice definido não está contido no domínio de posições do array")

  def size(self, logicalSize):
    for i in range(len(object)):
      if self.items[i] != None:
        self.logicalSize += 1
    return self.logicalSize
    
  