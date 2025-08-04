# Hass Table with Collision Handling (Chaining)
class hashTable:
  def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]

  def insert(self, key, value):
    index = simple_hash(key, self.size)
    for pair in self.table[index]:
      if pair[0] == key:
        pair[1] = value
        return
    self.table[index].append([key, value])

  def get(self, key):
    index = simple_hash(key, self.size)
    for pair in self.table[index]:
      if pair[0] == key:
        return pair[1]
    return None 