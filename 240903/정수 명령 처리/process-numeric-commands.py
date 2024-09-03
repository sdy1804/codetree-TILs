class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty == 1:
            raise Exception('Stack is empty')
        return self.items.pop()
    
    def top(self):
        return self.items[-1]

N = int(input())
command = [input().split() for _ in range(N)]

s = Stack()
for i in range(len(command)):
    if command[i][0] == 'push':
        s.push(command[i][1])
    elif command[i][0] == 'size':
        print(s.size())
    elif command[i][0] == 'empty':
        print(s.empty())
    elif command[i][0] == 'pop':
        print(s.pop())
    elif command[i][0] == 'top':
        print(s.top())