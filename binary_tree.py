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
            return "left:{0}-val:{1}-right:{2}".format(self.left, self.val, self.right)

    def __init__(self, root=None):
        ''' Constructor for BinaryTree '''

        self.root = root
    
    def insert(self, value):
        '''Insert root Node '''

        if self.root is None:
            self.root = self.Node(value)
	    return "Inserted Root Successfully"
        else:
            self.insert_node(self.root, value)
            return "Inserted Node Successfully"

    def insert_node(self,current,value):
        '''Insert a node into the Binary Tree '''

        while True:
            if value<current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = self.Node(value)
                    break
            elif value>current.val:
                if current.right:
                    current = current.right
   
                else:
                    current.right = self.Node(value)
                    break
            elif value == current.val:
                pass
	 

    def level_order(self):
        '''Prints Tree in level-order(Breadth First) '''

        head=self.root
        queue=[]
	data=[]
        while True:
            if head is None:
                return
	    data.append(head.val)
            [queue.append(node) for node in [head.left, head.right] if node]
            if queue:
                head=queue.pop(0)
            else:
                break
	return data

    def find(self, value):
       ''' Checks whether Node exists in Binary Tree '''

       node = self.root  
       while node != None:
            if node.val == value:
                return "Value Exists"
            node = node.left if value < node.val else node.right
       return "Value does not Exist"

    def inorder(self):
        ''' in-order tree traversal '''

        if self.root is None:
            return
        stack = []
	data=[]
        node = self.root
        print "\ninOrder"
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                data.append(node.val)
                node = node.right
	return data
    
    def preorder(self):
        ''' pre-order tree traversal '''
	
	data=[]
        if self.root is None:
            return
        stack = [self.root]
        print "\npreOrder"

        while stack:
            node = stack.pop()
            
            data.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
	return data

    def postorder(self):
        ''' post-order tree traversal '''
        traversal_lis = []
        node_stack = []
	data=[]
        current = self.root
        print "\npostOrder"
        while current or node_stack:

            while current:
                node_stack.append(current)
                data.append(current.val)
                traversal_lis.append(current.val)
                current = current.right
            if node_stack:
                node = node_stack.pop()
                current = node.left
	return data

if __name__ == '__main__':

      binTree=BinaryTree()
      data=[20,30,18,32,12]

      for d in data:
        print(binTree.insert(d)) 

      
      print(binTree.level_order())
      print(binTree.inorder())
      print(binTree.preorder())
      print(binTree.postorder())
      print(binTree.find(20))
      

