string = input()
n = int(input())

if n >= len(string):
    for elem in string[::-1]:
        print(elem, end="")
else:
    for elem in string[-1:len(string) - n - 1:-1]:
        print(elem, end="")