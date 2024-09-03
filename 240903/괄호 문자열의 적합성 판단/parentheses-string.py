class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def top(self):
        if self.empty == True:
            raise Exception('Stack is empty')
        return self.items[-1]
    
    def pop(self):
        if self.empty == True:
            raise Exception('Stack is empty')
        return self.items.pop()
    
    def size(self):
        return len(self.items)

string = input()

def sol(string):
    s = Stack()
    for i in range(len(string)):
        if string[i] == '(':
            s.push(string[i])
        else:
            if s.empty() == True: # 아무것도 없을 때 닫는 괄호
                return False
            else:
                s.pop()
        # print(s.top())
        # print(s.size())
    # print(s.empty())
    if s.empty() == False:
        return False
    else:
        return True

if sol(string):
    print('Yes')
else:
    print('No')