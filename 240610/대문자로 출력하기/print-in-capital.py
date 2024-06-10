string = list(input())

for s in string:
    if s.isalpha() == True:
        if s >= 'A' and s <= 'Z':
            print(s, end="")
        else:
            S = ord(s) - ord('a') + ord('A')
            print(chr(S), end="")