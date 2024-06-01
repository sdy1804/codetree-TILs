A_math, A_eng = map(int, input().split())
B_math, B_eng = map(int, input().split())

if A_math > B_math:
    print("A")
elif B_math > A_math:
    print("B")
elif (B_math == A_math) and (A_eng > B_eng):
    print("A")
else:
    print("B")