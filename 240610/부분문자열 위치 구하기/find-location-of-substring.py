string = input()
object = input()

# print(string.find(object))

if object in string:
    print(string.index(object))
else:
    print(-1)