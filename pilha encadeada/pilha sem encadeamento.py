class stack(object):
  stack = []

  def push(self, value):
    stack.append(value)
  
  def pop(self):
    p = stack[-len(stack)]
    stack.remove(-len(stack))
    return p

  def __len__(self):
    return self.len(stack)

  def peek(self):
    return stack[-len(stack)]
  
  def contains(self, value):
    for i in range(len(stack)):
      if stack[i] == value:
        return True
    else:
      return False