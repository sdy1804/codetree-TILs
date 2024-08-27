class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node
    
    def erase(self, node):
        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
    
    def insert(self, node, new_data):
        if node == self.begin():
            self.push_front(new_data)
        elif node == self.end():
            self.push_back(new_data)
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
    
    def begin(self):
        return self.head

    def end(self):
        return self.tail

n, m = map(int, input().split())
arr = list(input())
command = [input().split() for _ in range(m)]

DLL = DoublyLinkedList()
for i in range(n):
    DLL.push_back(arr[i])

it = DLL.end()
for j in range(m):
    if command[j][0] == 'L':
        if it != DLL.head:
            it = it.prev
        else:
            continue
        # print(command[j][0], it.data)
    elif command[j][0] == 'R':
        if it != DLL.tail:
            it = it.next
        else:
            continue
        # print(command[j][0], it.data)
    elif command[j][0] == 'D':
        if it == DLL.head:
            DLL.erase(it)
            it = DLL.head
            # print(it.data)
        elif it != DLL.tail:
            DLL.erase(it.next)
            it = it.next
        else:
            continue
        # print(command[j][0], it.data)
    elif command[j][0] == 'P':
        DLL.insert(it, command[j][1])
        it = it.prev
        # print(command[j][0], it.data)

pr = DLL.head
while pr != DLL.tail:
    print(pr.data, end="")
    pr = pr.next