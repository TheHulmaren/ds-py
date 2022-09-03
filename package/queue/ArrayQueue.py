from inspect import isfunction, ismemberdescriptor
from multiprocessing.dummy import Array


class ArrayQueue(object):
  def __init__(self, capacity):
    self.cap = capacity
    self.front = -1
    self.rear = -1
    self.items = [None]*capacity

  def __str__(self):
    return str(self.items)

  # checks if the queue is empty or not
  def isEmpty(self):
    if (self.rear, self.front) == (-1, -1):
      return True
    return False

  # checks if the queue is full or not
  def isFull(self):
    if (self.rear + 1) % self.cap == self.front:
      return True
    return False

  # returns the size(number of elements) of the queue
  def size(self):
    if self.isEmpty():
      return 0
    gap = self.rear - self.front
    if gap < 0:
      return self.cap + gap + 1
    return gap + 1

  # returns the front element of the queue
  def front(self):
    if self.isEmpty():
      return 
    return self.items[self.front]

  # enqueue an element into the queue
  # when failed returns None
  def enqueue(self, data):
    if self.isFull():
      return
    self.rear = (self.rear + 1) % self.cap
    self.items[self.rear] = data
    if self.front == -1:
      self.front = 0
    
    return self

  # dequeue a front element from the queue
  # when failed returns None
  def dequeue(self):
    dequeued = self.items[self.front]
    self.items[self.front] = None
    if self.front == self.rear:
      self.front, self.rear = (-1 ,-1)
      return dequeued
    
    self.front += 1
    return dequeued


if __name__=='__main__':
  pass