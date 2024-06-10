s, q = input().split()
q = int(q)
requests = []
for i in range(q):
    requests.append(int(input()))
# print(requests)
for req in requests:
    if req == 1:
        s = s[1:] + s[0]
        print(s)
    elif req == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[::-1]
        print(s)