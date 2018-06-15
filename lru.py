# LRU(Least Recently Used) Data Structure Implementation using a hash and doubly linked list in Python

class Node(object):

  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class LRU(object):

  def __init__(self, size):
    self.size = size
    self.head = None
    self.tail = None
    self.nodes = {}

  def read(self, node):
    this_node = self.nodes.get(node.data)
    if this_node:
      self.removeNode(node)
      self.set(node)
    else:
      self.set(node)

  def removeNode(self, node):
    this_node = self.head
    while this_node:
      if this_node.data == node.data:
        if this_node.prev is not None:
          this_node.prev.next = this_node.next
        else:
          self.head = this_node.next

        if this_node.next is not None:
          this_node.next.prev = this_node.prev
        else:
          self.tail = this_node.prev

        del self.nodes[node.data]

      this_node = this_node.next

  def set(self, new_node):
    if self.head is None:
      self.head = self.tail = new_node

    else:
      if len(self.nodes) >= self.size:
        tmp = self.tail.prev
        self.removeNode(self.tail)
        self.tail = tmp
        new_node.next = self.head
        new_node.prev = None
        self.head.prev = new_node
        self.head = new_node

      else:
        new_node.next = self.head
        new_node.prev = None
        self.head.prev = new_node
        self.head = new_node

    self.nodes[new_node.data] = new_node

  def show(self):
    this_node = self.head
    while this_node is not None:
      print (this_node.data, end=' ')
      this_node = this_node.next
    print ('')

a = LRU(4)

node1 = Node(12)
a.read(node1)
a.show()          # 12

node2 = Node(13)
a.read(node2)
a.show()          # 13 12

node3 = Node(14)
a.read(node3)
a.show()          # 14 13 12

node4 = Node(52)
a.read(node4)
a.show()          # 52 14 13 12

node5 = Node(16)
a.read(node5)
a.show()          # 16 52 14 13

node6 = Node(28)
a.read(node6)
a.show()          # 28 16 52 14

node7 = Node(13)
a.read(node7)
a.show()          # 13 28 16 52

node8 = Node(28)
a.read(node8)
a.show()          # 28 13 16 52
