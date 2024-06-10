upper, lower = input().split()
ascii_sum = ord(upper) + ord(lower)
if ord(upper) > ord(lower):
    ascii_diff = ord(upper) - ord(lower)
else:
    ascii_diff = ord(lower) - ord(upper)
print(ascii_sum, ascii_diff)