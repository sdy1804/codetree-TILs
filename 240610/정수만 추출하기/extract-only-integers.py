A, B = input().split()
A_num = ""
B_num = ""

for s in A:
    if s.isdigit() == True:
        A_num += s
    else:
        break

for s in B:
    if s.isdigit() == True:
        B_num += s
    else:
        break
print(int(A_num)+int(B_num))