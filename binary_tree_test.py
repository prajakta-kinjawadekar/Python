import unittest
from binary_tree import BinaryTree

class BinaryTest(unittest.TestCase):
 
  def setUp(self):
  	self.btree = BinaryTree()
	data = [20,30,18,32,12]
	for d in data:
		self.btree.insert(d)

  def test_insert(self):
	''' To check whether the node is inserted into the Binary Tree '''

	self.tree=BinaryTree()
	self.assertEqual(self.tree.insert(20),"Inserted Root Successfully")
	self.assertEqual(self.tree.insert(18),"Inserted Node Successfully")

  def test_level_order(self):
	''' To check whether the tree is printed in level order(Breadth First Format) '''

	self.assertEqual(self.btree.level_order(),[20, 18, 30, 12, 32])

  def test_in_order(self):
	''' To check whether the tree is printed in in-order format '''

	self.assertEqual(self.btree.inorder(),[12, 18, 20, 30, 32])
	
  def test_pre_order(self):
	''' To check whether the tree is printed in pre-order format '''

	self.assertEqual(self.btree.preorder(),[20, 18, 12, 30, 32])

  def test_post_order(self):
	''' To check whether the tree is printed in post-order format '''

	self.assertEqual(self.btree.postorder(),[20, 30, 32, 18, 12])

  def test_find(self):
	''' To check whether the specified value exists in Tree or not '''

	self.assertEqual(self.btree.find(20),"Value Exists")
	self.assertEqual(self.btree.find(4),"Value does not Exist")


if __name__=="__main__":
    
    unittest.main()

