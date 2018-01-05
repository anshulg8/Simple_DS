class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if (self.value == data):
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return True

        elif self.value > data:
            if self.leftChild:
                self.leftChild.find(data)
            else:
                return False

        elif self.value < data:
            if self.rightChild:
                self.rightChild.find(data)
            else:
                return False

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getSize() + self.rightChild.getSize()
        elif self.leftChild:
            return 1 + self.leftChild.getSize()
        elif self.rightChild:
            return 1 + self.rightChild.getSize()
        else:
            return 1

    def preorder(self):
        if self:
            print (str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print (str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return -1

    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0

    def remove(self, data):
        if self.root is None:
            return False

        elif self.root.value == data:

            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None

            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.leftChild

            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.rightChild

            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNodeParent.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild

                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild

                    else:
                        if delNodeParent.value > delNode.value:
                            delNodeParent.leftChild = None
                        elif delNodeParent.value < delNode.value:
                            delNodeParent.rightChild = None

                return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            if data > node.value:
                node = node.rightChild

        # Case 1: data not found
        if node is None or node.value != data:
            return False

        # Case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            if data > parent.value:
                parent.rightChild = None
            return True

        # Case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            if data > parent.value:
                parent.rightChild = node.leftChild
            return True

        # Case 4: remove-node has right child only
        elif node.rightChild and node.leftChild is None:
            if data < parent.value:
                parent.leftChild = node.rightChild
            if data > parent.value:
                parent.rightChild = node.rightChild
            return True

        # Case 5: remove-node has both left and right children
        # You replace remove-node with either the left most child on its right side,
        # or the right most child on its left side.
        # You then delete the child from the bottom that it was replaced with.

        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None

    def preorder(self):
        print ("PreOrder")
        self.root.preorder()

    def postorder(self):
        print ("PostOrder")
        self.root.postorder()

    def inorder(self):
        print ("InOrder")
        self.root.inorder()

bst = Tree()
print (bst.insert(8))
bst.insert(6)
bst.insert(10)
bst.insert(7)
bst.insert(5)
bst.insert(9)
bst.insert(11)
bst.remove(11)

bst.preorder()
bst.postorder()
bst.inorder()
print(bst.getHeight())
print('Size = ', bst.getSize())
# Output
# True
# PreOrder
# 8
# 6
# 5
# 7
# 10
# 9
# 11
# PostOrder
# 5
# 7
# 6
# 9
# 11
# 10
# 8
# InOrder
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 3
