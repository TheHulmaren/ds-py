class Stack(object):
  def __init__(self):
    self.items = []
    self.top = -1

  def __str__(self):
    return str(self.items)

  def push(self, data):
    self.top += 1
    self.items.append(data)

    return self

  def pop(self):
    if self.top == -1:
      print('Stack is empty')
      return
    popped = self.items[self.top]
    del self.items[self.top]
    self.top -= 1

    return popped

  def top(self):
    return self.items[self.top]


if __name__ == '__main__':
  a = Stack()
  a.push(2).push(7)

  print(a)
  print(a.pop())

  a.push(10).push(9)

  print(a.pop())
  print(a)

