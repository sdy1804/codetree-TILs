from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        if len(self.dq) == 0:
            return 1
        else:
            return 0
    
    def pop(self):
        if self.empty() == True:
            raise Exception("Stack is empty")
        return self.dq.popleft()
    
    def front(self):
        if self.empty() == True:
            raise Exception("Stack is empty")
        return self.dq[0]

N = int(input())
command = [input().split() for _ in range(N)]

q = Queue()

for i in range(len(command)):
    if command[i][0] == 'push':
        q.push(command[i][1])
    elif command[i][0] == 'size':
        print(q.size())
    elif command[i][0] == 'empty':
        print(q.empty())
    elif command[i][0] == 'pop':
        print(q.pop())
    elif command[i][0] == 'front':
        print(q.front())