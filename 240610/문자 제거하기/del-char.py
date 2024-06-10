string = list(input())
# nums = [input().split() for i in range(len(string)-1)]
nums = []
for i in range(len(string)-1):
    nums.append(int(input()))
# print(nums)

for index in nums:
    if len(string) > index:
        string.pop(index)
        for elem in string:
            print(elem, end="")
        print()
    else:
        string.pop(-1)
        for elem in string:
            print(elem, end="")
        print()