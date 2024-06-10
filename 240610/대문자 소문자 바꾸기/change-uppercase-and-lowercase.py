string = input()

for s in string:
    if s >= 'A' and s <= 'Z':
        s = ord(s) - ord('A') + ord('a')
        print(chr(s), end="")
    else:
        s = ord(s) - ord('a') + ord('A')
        print(chr(s), end="")