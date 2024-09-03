from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()
    
    def push_front(self, item):
        self.dq.appendleft(item)
    
    def push_back(self, item):
        self.dq.append(item)
    
    def size(self):
        return len(self.dq)
    
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    
    def pop_front(self):
        if self.size == 0:
            raise Exception('Deque is empty')
        return self.dq.popleft()
    
    def pop_back(self):
        if self.size == 0:
            raise Exception('Deque is empty')
        return self.dq.pop()
    
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]

N = int(input())
command = [input().split() for _ in range(N)]

dq = Deque()
for i in range(N):
    if command[i][0] == 'push_front':
        dq.push_front(command[i][1])
    elif command[i][0] == 'push_back':
        dq.push_back(command[i][1])
    elif command[i][0] == 'pop_front':
        print(dq.pop_front())
    elif command[i][0] == 'pop_back':
        print(dq.pop_back())
    elif command[i][0] == 'size':
        print(dq.size())
    elif command[i][0] == 'empty':
        print(dq.empty())
    elif command[i][0] == 'front':
        print(dq.front())
    elif command[i][0] == 'back':
        print(dq.back())