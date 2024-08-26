class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, num):
        new_node = Node(num)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.node_num += 1
    
    def push_back(self, num):
        new_node = Node(num)

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.node_num += 1
    
    def pop_front(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            self.node_num -= 1
            return temp.data
    
    def pop_back(self):
        if self.tail == None:
            return None
        elif self.tail.prev == None:
            temp = self.tail
            self.tail = None
            self.head = None
            self.node_num = 0
            return temp.data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.node_num -= 1
            return temp.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        if self.node_num == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.data
    
    def back(self):
        if self.tail == None:
            return None
        else:
            return self.tail.data

N = int(input())
command = [input().split() for _ in range(N)]

l = DoublyLinkedList()
for i in range(len(command)):
    if command[i][0] == 'push_front':
        l.push_front(command[i][1])
    elif command[i][0] == 'push_back':
        l.push_back(command[i][1])
    elif command[i][0] == 'pop_front':
        print(l.pop_front())
    elif command[i][0] == 'pop_back':
        print(l.pop_back())
    elif command[i][0] == 'size':
        print(l.size())
    elif command[i][0] == 'empty':
        print(l.empty())
    elif command[i][0] == 'front':
        print(l.front())
    elif command[i][0] == 'back':
        print(l.back())