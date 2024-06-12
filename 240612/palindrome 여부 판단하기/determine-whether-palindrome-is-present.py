def palindrome(string):
    if string == string[::-1]:
        print('Yes')
    else:
        print('No')

A = input()
palindrome(A)