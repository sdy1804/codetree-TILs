string = input()

string = string[:string.index('e')] + string[string.index('e')+1:]
print(string)