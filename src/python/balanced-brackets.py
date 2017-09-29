class Stack:
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

def is_matched(expression):
    stack = Stack()
    for c in expression:
        if c == '{' or c == "[" or c == '(':
            stack.push(c)
        else:
            if stack.isEmpty():
                return False
            c_stack = stack.peek()
            if (c_stack == '{' and c == '}') or (c_stack == '[' and c == ']') or (c_stack == '(' and c == ')'):
                stack.pop() 
            else:
                return False
    return stack.isEmpty()
    """for c in expression:
        if c == '{':
            stack.push('}')
        elif c == '(':
            stack.push(')')
        elif c == '[':
            stack.push(']')
        else:
            if stack.isEmpty() or stack.peek() != c:
                return False
            stack.pop()
    return stack.isEmpty()"""

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
