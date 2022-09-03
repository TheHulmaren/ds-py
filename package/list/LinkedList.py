from fileinput import nextfile
from readline import insert_text


class Node:
  def __init__(self, key=None, next=None):
    self.key = key
    self.next = next

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next
    return self

  def getKey(self):
    return self.key

  def setKey(self, key):
    self.key = key
    return self


class LinkedList(object):
  def __init__(self):
    self.head = None

  def __str__(self):
    result = ''
    cur = self.head
    while (True):
      if cur is None:
        break
      result += str(cur.key) + ' '
      cur = cur.getNext()
    return result

  # returns a string containing items in reversed order
  # without changing actual order of the linked list
  # - uses backtracking approach
  # when failed returns None
  def reverseStr(self):
    if self.head is None:
      print('Head not defined')
      return
    result = []
    self.reverseStrIter(self.head, result)
    return str(result)

  # iteratetor used for reverseStr
  # when given node is None returns None
  def reverseStrIter(self, node, result):
    if node is None:
      return
    self.reverseStrIter(node.getNext(), result)
    result.append(node.getKey())

  # alters head pointer to point a node with given key
  def insertAtFirst(self, key):
    insertedNode = Node(key, self.head)
    self.head = insertedNode
    return self

  # inserts a node with given key at the last position
  # when head is not defined, performs insertAtFirst
  # when failed returns None
  def insertAtLast(self, key):
    cur = self.head

    if cur is None:
      return self.insertAtFirst(key)

    while (cur.getNext() is not None):
      cur = cur.getNext()

    insertedNode = Node(key)
    cur.setNext(insertedNode)
    return self

  # inserts a node with given key after a given node
  # when failed returns None
  def insertAfter(self, node, key):
    if node is None:
      return
    insertedNode = Node(key, node.getNext())
    node.setNext(insertedNode)

    return self

  # inserts a node with given key at the given index
  # when failed returns None
  def insertAt(self, key, index):
    if index == 0:
      self.insertAtFirst(key)
      return self

    targetNode = self.search(index-1)

    if targetNode is None:
      print('Index exceeds the length of the linked list')
      return

    self.insertAfter(targetNode, key)
    return self

  # deletes a node positioned at given index
  # when failed returns None
  def deleteAt(self, index):
    if index == 0:
      self.head = self.search(1)
      return self

    prevNode = self.search(index-1)
    if prevNode is None:
      print('Index exceeds the length of the linked list')
      return

    targetNode = prevNode.getNext()
    nextNode = None
    if targetNode is None:
      print('Index exceeds the length of the linked list')
      return
    else:
      nextNode = targetNode.getNext()

    prevNode.setNext(nextNode)
    return self

  # deletes a first node with the key of equal value
  # when failed returns None
  def deleteByKey(self, key):
    targetIndex = self.searchKey(key)
    if targetIndex == -1:
      return

    if self.deleteAt(targetIndex) is None:
      return

    return self

  # updates a key of node positioned at given index
  # when failed returns None
  def updateAt(self, key, index):
    targetNode = self.search(index)

    if targetNode is None:
      print('Error Occurred')

    targetNode.key = key
    return self

  # searches node by given index
  # when found returns node
  # if not returns None
  def search(self, index):
    if self.head is None:
      print('Header not defined')
      return

    return self.searchIter(self.head, index, 0)

  # iteratetor used for search
  # when given node is None returns None
  def searchIter(self, node, index, curIndex):
    if node is None:
      print('Given index exceeds the length of linked list')
      return
    if curIndex == index:
      return node

    return self.searchIter(node.getNext(), index, curIndex+1)

  # searches node with an equal key
  # when found returns index
  # if not returns -1
  def searchKey(self, key):
    if self.head is None:
      print('Header not defined')
      return -1

    curNode = self.head
    curIndex = 0
    while (curNode is not None):
      if curNode.getKey() == key:
        return curIndex
      curIndex += 1
      curNode = curNode.getNext()
    return -1

  # reverses linked list
  # - uses backtracking approach
  # when failed returns None
  def reverse(self):
    if self.head is None:
      print('Header not defined')
      return

    return self.reverseIter(self.head)

  # iteratetor used for reversing
  # when given node is None returns None
  def reverseIter(self, node):
    if node.getNext() is None:
      self.head = node
      return

    self.reverseIter(node.getNext())
    node.getNext().setNext(node)
    node.setNext(None)
    return 

  # finds a length of linked list 
  # when failed returns None
  def length(self):
    curIndex = 0
    curNode = self.head

    while(curNode is not None):
      curIndex += 1
      curNode = curNode.getNext()
    return curIndex

if __name__=='__main__':
  a = LinkedList()

  a.insertAtFirst(1).insertAtFirst(2).insertAtFirst(10)
  print(a)

  print(a.search(1).key)
  print(a.insertAfter(a.search(0), 15))

  print(a.insertAt(17, 0))
  print(a.insertAt(9, 2))

  print(a.deleteAt(4))
  print(a.deleteAt(0))

  print(a.updateAt(11, 1))

  print(a.deleteByKey(1))

  a.insertAtLast(100).insertAtLast(17).insertAtLast(5)
  a.reverse()
  print(a)

  print(a.length())

  print(a.reverseStr())