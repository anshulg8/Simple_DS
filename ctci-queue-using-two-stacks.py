class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print items

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.isEmpty():
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2.isEmpty():
            return self.stack2.peek()

    def printQueue(self):
        self.stack2.printstack()

if __name__ == '__main__':
    q = QueueUsingTwoStacks()
    # print q.isEmpty()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.peek()
    q.enqueue(4)
    q.dequeue()
    q.printQueue()


    q.printQueue()
