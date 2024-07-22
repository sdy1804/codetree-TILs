N = int(input())
string = input()

# 앞에서부터 뜯어서 전체 문자열에서 몇번 나타나는지 카운트
# 2번이하인 문자열이면 break로 중단하고 그에 대한 len 출력

for i in range(1, len(string) + 1):
    temp_string = string[:i]
    # print(temp_string)
    # print(string.count(temp_string))
    if string.count(temp_string) < 2:
        print(len(temp_string))
        break