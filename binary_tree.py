'''
Binary Tree implementation


'''

from stack import Stack
from queue import Queue


class BinaryTree:
    ''' Represents a binary tree '''

    class Node:
        ''' Represents a node in the binary tree '''

        def __init__(self, val, left=None, right=None):
            ''' Constructor for Node '''
            self.val = val
            self.left = left
            self.right = right

        def __repr__(self):
            return "{0}<-{1}->{2}".format(self.left, self.val, self.right)

    def __init__(self, root=None):
        ''' Constructor for BinaryTree '''
        self.root = root

    def insert(self, value):
        ''' Insert root Node '''
        # check if node is root node
        if self.root is None:
            self.root = self.Node(value)
            return "Inserted Root Successfully"
        else:
            self.insert_node(self.root, value)
            return "Inserted Node Successfully"

    def insert_node(self, current, value):
        '''Insert a node into the Binary Tree '''
        while True:
            # insert Node on left
            if value < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = self.Node(value)
                    break
            # insert Node on right
            elif value > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = self.Node(value)
                    break
            elif value == current.val:
                pass

    def level_order(self):
        '''Prints Tree in level-order(Breadth First) '''
        head = self.root
        que = Queue()
        data = []
        while True:
            if head is None:
                return
            data.append(head.val)
            # append the parent's left or right node into the queue
            [que.enqueue(node) for node in [head.left, head.right] if node]
            if que.get_queue():
                head = que.dequeue()
            else:
                break
        return data

    def find(self, value):
        ''' Checks whether Node exists in Binary Tree '''
        node = self.root
        while node is not None:
            if node.val == value:
                return "Value Exists"
            node = node.left if value < node.val else node.right
        return "Value does not Exist"

    def inorder(self):
        '''
        in-order tree traversal
        Until all nodes are traversed
        Step 1 :Visit all nodes in left subtree.
        Step 2 :Visit root node.
        Step 3 :Visit all nodes in right subtree
        '''
        if self.root is None:
            return
        stack = Stack()
        data = []
        node = self.root
        while stack.get_stack() or node:
            if node:
                stack.push(node)
                node = node.left
            else:
                node = stack.pop()
                data.append(node.val)
                node = node.right
        return data

    def preorder(self):
        '''
        pre-order tree traversal
        Until all nodes are traversed
        Step 1 : Visit root node.
        Step 2 : Visit all nodes in left subtree.
        Step 3 : Visit all nodes in right subtree.
        '''
        data = []
        if self.root is None:
            return
        stack = Stack()
        stack.push(self.root)
        while stack.get_stack():
            node = stack.pop()
            data.append(node.val)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
        return data

    def postorder(self):
        '''
        post-order tree traversal
        Until all nodes are traversed
        Step 1 :Visit all nodes in left subtree.
        Step 2 :Visit all nodes in right subtree.
        Step 3 : Visit root node.
        '''
        traversal_lis = []
        stack = Stack()
        data = []
        current = self.root
        while current or stack.get_stack():
            while current:
                stack.push(current)
                data.append(current.val)
                traversal_lis.append(current.val)
                current = current.right
            if stack.get_stack():
                node = stack.pop()
                current = node.left
        return data

if __name__ == '__main__':

    binTree = BinaryTree()
    data = [20, 30, 18, 32, 12]

    for d in data:
        print(binTree.insert(d))

    print("\nBFS Traversal:\n{0}".format(binTree.level_order()))
    print("\ninOrder:\n{0}".format(binTree.inorder()))
    print("\npreOrder:\n{0}".format(binTree.preorder()))
    print("\npostOrder:\n{0}".format(binTree.postorder()))
    print("\nThe given {0}".format(binTree.find(20)))

