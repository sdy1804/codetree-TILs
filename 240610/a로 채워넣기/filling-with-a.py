string = list(input())

string[1], string[-2] = 'a', 'a'

print("".join(string))