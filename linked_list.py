class Node(object):
  
  def __init__(self, initdata):
    self.data=initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext

class LinkedList(object):
	
  def __init__(self):
    self.head = None
    self.tail = None
    
  def isEmpty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
    if(self.head.getNext() == None):
      self.tail = temp



  def size(self):
    count = 0
    current = self.head
    if current.next == None:
    	return 0
    while (current != None):
        current = current.getNext()
        count += 1

    return count

  def search(self, item):
    found = False
    current = self.head 
    while (current != None and not found):
      if current.getData() == item:
        found = True
      else:
    	current = current.getNext()
        
    return found

  def remove(self, item):
    found = False
    current = self.head
    prev = None

    while(current != None and not found):
      if current.getData() == item:
        found = True
      else:
        prev = current
    	current = current.getNext()

    if prev == None:
      self.head = current.getNext()
    # element is not 1st element, remove the node and rebuild the list
    else:
      if current.getNext() == None and found:
        self.tail = prev

      prev.setNext(current.getNext())

  def append(self, item):
    temp = Node(item)
        
    if(self.head == None):
      self.head = temp
    else:
      self.tail.setNext(temp)
      self.tail = temp

  def print_list(self):
  	current = self.head
  	while(current != None):
  		print current.getData()
  		current = current.getNext()


def main():

  mylist = LinkedList()
  mylist.add(5)
  mylist.add(7)
  mylist.add(15)
  mylist.add(8)
  mylist.append(100)
  mylist.append(23)
  size = mylist.size()
  mylist.print_list()
  print "The size of the list is "+str(size)




if __name__ == '__main__':
	main()
