from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()
    
    def push_back(self, item):
        self.dq.append(item)

    def empty(self):
        if len(self.dq) == 0:
            return True
        else:
            return False

    def pop_front(self):
        if self.empty():
            raise Exception('Deque is empty')
        return self.dq.popleft()
    
    def size(self):
        return len(self.dq)
    
    def front(self):
        return self.dq[0]
    
    def back(self):
        return self.dq[-1]

N = int(input())
arr = [i for i in range(1, N+1)]

dq = Deque()
for i in range(len(arr)):
    dq.push_back(arr[i])

while dq.size() != 1:
    dq.pop_front()
    # print('last', last)
    # print('dq.front()', dq.front())
    second_front = dq.pop_front()
    dq.push_back(second_front)

print(dq.front())