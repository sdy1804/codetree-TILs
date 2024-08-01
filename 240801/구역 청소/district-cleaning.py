a, b = map(int, input().split())
c, d = map(int, input().split())

ans = 0
# 조금씩 겹쳤을 경우
if a < c and c <= b and b < d:
    ans = d - a
elif c < a and a <= d and d < b:
    ans = b - c
# 완전히 겹쳤을 경우
elif a <= c and d <= b:
    ans = b - a
elif c <= a and b <= d:
    ans = d - c
# 안 겹친 경우
elif a < b < c < d:
    ans = (b - a) + (d - c)
elif c < d < a < b:
    ans = (b - a) + (d - c)

print(ans)