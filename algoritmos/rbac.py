# Permission Tree (simplefied RBAC)
class PermissionNode:
  def __init__(self, name):
    self.name = name
    self.children = []

  def add_child(self, node):
    self.children.append(node)

  def has_permission(self, name):
    if self.name == name:
      return True
    return any(child.has_permission(name) for child in self.children)