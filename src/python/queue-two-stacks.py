class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class MyQueue(object):
    def __init__(self):
        self.first = Stack()
        self.second = Stack()
    
    def enqueue(self, item):
        self.first.push(item)

    def dequeue(self):
        if self.second.isEmpty():
            while not self.first.isEmpty():
                self.second.push(self.first.pop());
        self.second.pop()

    def first_element(self):
        if not self.second.isEmpty():
            return self.second.peek()
        else:
            while not self.first.isEmpty():
                self.second.push(self.first.pop())
            return self.second.peek()
        

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.enqueue(values[1])        
    elif values[0] == 2:
        queue.dequeue()
    else:
        print queue.first_element()
        
