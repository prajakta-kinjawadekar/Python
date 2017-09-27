'''
Stack implementation

'''

class Stack(object):
  ''' Represents a stack i.e. FILO '''

  def __init__(self):
    self._stack = []
  
  def push(self, data):
    ''' Should push the data on the top of the stack '''
    self._stack.append(data)
  
  def pop(self):
    ''' Should remove the data at the top of the stack and return it '''
    return self._stack.pop()

 
  def get_stack(self):
    '''Should return the entire stack '''
    return self._stack

  @property
  def top(self):
    ''' Should return the data at the top of the stack '''
    return self._stack[-1]


if __name__=="__main__":
    stack1=Stack()
    data=[1,2,3,4,5,6]
    for d in data:
        stack1.push(d)
    print(stack1.pop())
    print(stack1.top)
    

