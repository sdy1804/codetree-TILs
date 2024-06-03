while 1:
    n = int(input())
    if n < 25:
        print("Higher")
    elif n == 25:
        print("Good")
        break
    else:
        print("Lower")