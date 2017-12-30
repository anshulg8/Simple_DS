# Queues: A Tale of Two Stacks -> https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

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

    def bottom(self):
        return self.items[0]

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
        if self.stack2.isEmpty():
            return self.stack1.bottom()
        else:
            return self.stack2.peek()

    def printQueue(self):
        self.stack2.printstack()


queue = QueueUsingTwoStacks()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.enqueue(values[1])
    elif values[0] == 2:
        queue.dequeue()
    else:
        print queue.peek()
