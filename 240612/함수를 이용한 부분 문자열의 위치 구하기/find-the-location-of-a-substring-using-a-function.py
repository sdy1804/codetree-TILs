string = input()
ob_string = input()

def check_position():
    if ob_string in string:
        return string.find(ob_string)
    else:
        return -1

print(check_position())