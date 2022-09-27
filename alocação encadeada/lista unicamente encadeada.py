class Node:

  def __init__(self, inData):
    self.inData = inData
    self.next = None

node1 = Node(3)
node2 = Node(6)
node3 = Node(9) 

node1.next = node2
node2.next = node3
node3.next = node1

print(node1.next)
print(node1.next.inData)
print(node2.next)
print(node2.next.inData)
print(node3.next)
print(node3.next.inData)