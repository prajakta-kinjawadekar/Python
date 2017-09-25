import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
  
    def setUp(self):
	'''To create object of Queue''''
        self.que = Queue()
	self.que.enqueue(3)

    def test_enqueue(self):
      	''' To check whether the data is inserted at the end of the queue '''
        self.assertEqual(self.que._queue[0],3)

    def test_get_queue(self):
	'''To check whether the queue is printed '''
	res=self.que.get_queue()
        self.assertEqual(res,[3])

    def test_dequeue(self):
	'''To check whether the data is removed from front of the queue and returned '''
        res=self.que.dequeue()
        self.assertEqual(res,3)

    def test_front_property(self):
        res=self.que.front
        self.assertEqual(res,3)

    def tearDown(self):
	'''To destroy object of Queue''''
        self.que=None


if __name__=="__main__":
    
    unittest.main()
