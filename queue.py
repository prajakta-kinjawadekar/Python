'''
Queue implementation

'''


class Queue(object):
  ''' Represents a queue i.e. FIFO '''


  def __init__(self):
  	self._queue = []
    
  def __repr__(self):
  	return "{0}".format(self._queue)

  def enqueue(self, data):
    ''' Should add the data at the end of the queue '''
    self._queue.append(data)
    
  
  def dequeue(self):
    ''' Should remove the data from the front of the queue and return it '''
    return self._queue.pop(0)
  
  
  def get_queue(self):
    '''Should return the entire queue '''
    return self._queue
  
  @property
  def front(self):
    ''' Should return the data at the front of the queue '''
    return self._queue[0]


if __name__=="__main__":
    queue=Queue()
    data=[1,2,3,4,5,6]
    for d in data:
        queue.enqueue(d)
    print(queue.get_queue())
    print(queue.dequeue())
    print(queue.front)
    
    
    
