#A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

#A basic queue has the following

class MyQueue(object):
    def __init__(self):
        self.items=[]
    
    def peek(self):
        i = self.items.pop()
        self.items.append(i)
        return i
        
    def pop(self):
        return self.items.pop()
        
    def put(self, value):
        self.items.insert(0, value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())