n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = False

for i in range(n1-n2+1):
    if B == A[i:i+len(B)]:
        check = True
if check == True:
    print("Yes")
else:
    print("No")