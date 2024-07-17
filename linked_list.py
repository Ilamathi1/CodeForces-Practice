class Node:

  def __init__(self):
    self.data = None
    self.next = None

  def setData(self,data):
    self.data = data

  def getData(self):
    return self.data

  def setNext(self,next):
    self.next = next
  
  def getNext(self):
    return self.next
  
  def hasNext(self):
    return self.next != None
  
  def listLength(self):
    current = self.head
    count = 0
    while current != None:
      count += 1
      current = current.getNext()
    return count

  def insertAtBeginning(self,data):
    newNode = Node()
    newNode.setData(data)

    if self.Length == 0:
      self.head = newNode
    else:
      newNode.setNext(self,head)
      self.head = newNode
    self.Length += 1