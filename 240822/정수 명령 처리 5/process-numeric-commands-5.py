N = int(input())
command = [input().split() for _ in range(N)]

temp_list = []

for i in range(len(command)):
    if 'push_back' in command[i]:
        temp_list.append(command[i][1])
    
    if 'pop_back' in command[i]:
        temp_list.pop()
    
    if 'size' in command[i]:
        print(len(temp_list))
    
    if 'get' in command[i]:
        command[i][1] = int(command[i][1])
        print(temp_list[command[i][1] - 1])