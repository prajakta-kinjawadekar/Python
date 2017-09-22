import unittest
from stack import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
	'''To create object of Stack'''
        self.stk = Stack()
	self.stk.push(3)

    def test_push(self):
	''' To check whether the data is pushed on the top of the stack '''
        self.assertEqual(self.stk._stack[0],3)

    def test_pop(self):
	''' To check whether the data is removed from the top of the stack and returned '''
	res=self.stk.pop()
	self.assertEqual(res,3)

    def test_top_property(self):
	res=self.stk.top
	self.assertEqual(res,3)
	
    def tearDown(self):
	'''To destroy object of Stack'''
        self.que=None


if __name__=="__main__":
    
    unittest.main()
