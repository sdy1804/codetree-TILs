A = input()
B = input()
AB_new_str = ""
BA_new_str = ""
AB_new_str = A+B
BA_new_str = B+A
if AB_new_str == BA_new_str:
    print('true')
else:
    print('false')