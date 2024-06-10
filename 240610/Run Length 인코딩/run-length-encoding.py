string = input()
cnt = 1
new_string = []
len_sum = 0

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        cnt += 1
        if i == len(string) - 1:
            # print(f"{string[i-1]}{cnt}", end="")
            new_string.append(f"{string[i-1]}{cnt}")    
    else:
        # print(f"{string[i-1]}{cnt}", end="")
        new_string.append(f"{string[i-1]}{cnt}")
        cnt = 1

for i in range(len(new_string)):
    len_sum += len(new_string[i])
print(len_sum)

for elem in new_string:
    print(elem, end="")