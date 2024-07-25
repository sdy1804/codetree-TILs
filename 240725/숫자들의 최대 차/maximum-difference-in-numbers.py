N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

MAX_NUM = 10000

def count_num(l, r): # arr에 있는 숫자들이 해당 구간에 몇개 포함되는지 count
    cnt = 0
    for elem in arr:
        if elem >= l and elem <= r:
            cnt += 1
    return cnt

ans = 0
for i in range(1, MAX_NUM+1):
    ans = max(ans, count_num(i, i+K))
print(ans)