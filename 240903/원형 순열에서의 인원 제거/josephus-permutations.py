from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        if len(self.dq) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.dq)
    
    def pop(self):
        if self.empty() == True:
            raise Exception('Queue is empty')
        return self.dq.popleft()
    
    def front(self):
        if self.empty() == True:
            raise Exception('Queue is empty')
        return self.dq[0]

# def sol(n, k):
#     ans = []
#     q = Queue()
#     for i in range(1, n+1):
#         q.push(i)
    
#     while q.size() != 0:
#         for j in range(1, k):
#             q.push(q.front())
#             # print('q.pop()', q.pop())
#         last = q.pop()
#         # print(last)
#         ans.append(last)
#     return ans

N, K = map(int, input().split())

# ans = []
q = Queue()
for i in range(1, N+1):
    q.push(i)

while q.size() != 0:
    for j in range(1, K):
        q.push(q.front())
        q.pop()
        # print('q.pop()', q.pop())
    last = q.pop()
    print(last, end=" ")
    # ans.append(last)

# for elem in ans:
#     print(elem, end=" ")