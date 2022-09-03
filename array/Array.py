
class Array(object):
  def __init__(self, sizeOfArray, arrayType=int):
    self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
    # initialize array with zeroes
    self.arrayItems = [arrayType(0)] * sizeOfArray

  def __str__(self):
    return ' '.join([str(i) for i in self.arrayItems])

  # function for key insertion at given index
  def insert(self, key, index):
    if index >= self.sizeOfArray:
      print('Given index exceeds the size of an array.')
      return
    for i in range(self.sizeOfArray-2, key-1, -1):
      self.arrayItems[i+1] = self.arrayItems[i]
    self.arrayItems[index] = key
    return self

  # function for deletion by index
  def delete(self, index):
    if index >= self.sizeOfArray:
      print('Given index exceeds the size of an array.')
      return self

    for i in range(index, self.sizeOfArray-1):
      self.arrayItems[i] = self.arrayItems[i+1]
    self.arrayItems[self.sizeOfArray-1] = 0
    return self

  # function for deleting first key of equal value
  def deleteKey(self, key):
    foundIndex = self.search(key)
    if foundIndex == -1:
      print('Element with equal value of given key does not exist.')
      return self
    self.delete(foundIndex)
    return self

  # function for key update at given index
  def update(self, key, index):
    if index >= self.sizeOfArray:
      print('Given index exceeds the size of an array.')
      return self
    self.arrayItems[index] = key
    return self

  # function for searching first key of equal value
  def search(self, key):
    # by brute force
    for i in range(self.sizeOfArray):
      if self.arrayItems[i] == key:
        return i
    return -1


a = Array(10, int)

a.insert(2, 5).insert(5, 5).insert(7, 9)
print(a)

a.delete(5)
print(a)

a.delete(0)
print(a)

a.update(3, 0).update(1, 1)
print(a)

print(a.search(2))

a.deleteKey(7).deleteKey(3)
print(a)
