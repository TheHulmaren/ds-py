from ..list.LinkedList import LinkedList


class LLStack(object):

  def __init__(self):
    self.items = LinkedList()

  def __str__(self):
    return self.items.reverseStr()

  def push(self, data):
    self.items.insertAtFirst(data)
    return self

  def pop(self):
    if self.items.head is None:
      return
    popped = self.items.head.getKey()
    self.items.deleteAt(0)

    return popped

  def top(self):
    if self.items.head is None:
      return

    return self.items.head.getKey()


if __name__ == '__main__':
  pass
