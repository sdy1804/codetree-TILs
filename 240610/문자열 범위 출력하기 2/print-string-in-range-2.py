string = input()
n = int(input())

for elem in string[-1:len(string) - n - 1:-1]:
    print(elem, end="")