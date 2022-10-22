class stackList(object):
  _size = 0
  stack = []

  def push(self, value):
    self.stack.append(value)
  
  def pop(self):
    p = self.stack[self._size - 1]
    self.stack.remove(self._size - 1)
    return p

  def __len__(self):
    return self.stack[self._size]

  def peek(self):
    return self.stack[self._size - 1]
  
  def contains(self, value):
    for i in range(self._size):
      if self.stack[i] == value:
        return True
    else:
      return False
    
  def __repr__(self):
    r = ""
    for i in range(len(self.stack)):
      r = r + str(self.stack[i]) + "\n"
    return r
  
  def __str__(self):
    return self.__repr__()

fodase = stackList()

fodase.push(3)
fodase.push(2)
fodase.push(1)

print(fodase.peek)

print(fodase.pop)