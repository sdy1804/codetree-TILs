cnt = 0

def go_to_one(n):
    global cnt
    if n == 1:
        return cnt
    else:
        cnt += 1
        if n % 2 == 0:
            return go_to_one(n//2)
        else:
            return go_to_one(n//3)

N = int(input())
print(go_to_one(N))