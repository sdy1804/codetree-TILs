for _ in range(10):
    string = input()
    if string == 'END':
        break
    else:
        print(string[::-1])