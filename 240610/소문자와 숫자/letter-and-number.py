string = input()

for s in string:
    if s.isalpha() == True or s.isdigit() == True:
        if s >= 'A' and s <= 'Z':
            s = ord(s) - ord('A') + ord('a')
            print(chr(s), end="")
        else:
            print(s, end="")