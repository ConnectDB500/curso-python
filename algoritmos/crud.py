# CRUD operation with a list of dictionaries
class SimpleCRUD:
  def __init__(self):
    self.data = []

  def create(self, item):
    self.data.append(item)

  def read(self):
    return self.data
  
  def update(self, index, new_item):
    if 0 <= index < len(self.data):
      self.data[index] = new_item

  def delete(self, index):
    if 0 <= index < len(self.data):
      self.data.pop(index)