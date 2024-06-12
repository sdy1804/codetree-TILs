def sum_(A, B):
    sums = A + B
    return sums

def diff_(A, B):
    diffs = A - B
    return diffs

def divide_(A, B):
    divides = A / B
    return divides

def multiply_(A, B):
    multiplys = A * B
    return multiplys


a, o, c = input().split()
a, c = int(a), int(c)
if o == '+':
    print(f"{a} {o} {c} = {sum_(a, c)}")
elif o == '-':
    print(f"{a} {o} {c} = {diff_(a, c)}")
elif o == '/':
    print(f"{a} {o} {c} = {divide_(a, c):.0f}")
elif o == '*':
    print(f"{a} {o} {c} = {multiply_(a, c)}")
else:
    print('False')