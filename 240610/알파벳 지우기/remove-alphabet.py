str1 = input()
str2 = input()
new_str1 = ""
new_str2 = ""

for s in str1:
    if s.isdigit() == True:
        new_str1 += s

for s in str2:
    if s.isdigit() == True:
        new_str2 += s

print(int(new_str1) + int(new_str2))