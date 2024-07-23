import sys

N = int(input())
string = input()

# 앞에서부터 뜯어서 전체 문자열에서 몇번 나타나는지 카운트
# -> 테케에서 문제 발생 : 앞에서부터가 아닌 1개짜리 탐색, 2개짜리 부분문자열 탐색... 이런식으로 진행해야할듯
# count 함수로 해결되지 않는 부분이 있는듯? -> 나오는 경우들 리스트로 다 보관해야 할듯
# 2번이하인 문자열이면 break로 중단하고 그에 대한 len 출력
length_list = []
temp_list = []
for i in range(0, len(string)): # 시작점
    for j in range(1, N-i+1):
        # print(i, j)
        temp_string = string[i:i+j]
        temp_list.append(temp_string)
        # print(temp_string)
        # print(string.count(temp_string))
# print(temp_list)

for i in range(0, len(string)):
    for j in range(1, N+1):
        temp_string = string[i:i+j]
        # print(temp_string)
        # print(temp_list.count(temp_string))
        if temp_list.count(temp_string) >= 2 and len(temp_string) not in length_list:
            # print(temp_string)
            # print(temp_list.count(temp_string))
            length_list.append(len(temp_string))
# print(length_list)

total_len_min = sys.maxsize
for i in range(0, len(string)): # 시작점
    for j in range(1, N+1):
        temp_string = string[i:i+j]
        now_length = 0
        # print(temp_string)
        if temp_list.count(temp_string) < 2 and len(temp_string) not in length_list:
            now_length = len(temp_string)
            # print(now_length)
            total_len_min = min(now_length, total_len_min)
            # print(temp_string)
            # print(len(temp_string))
print(total_len_min)