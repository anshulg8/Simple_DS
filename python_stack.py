class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print items

s = Stack()

print s.isEmpty()
s.push(4)
s.push('dog')
s.push(6)
s.push('bob')
print s.isEmpty()
s.printstack()
print s.pop()
print ""
s.printstack()
