n = int(input())
blocks = list(int(input()) for _ in range(n))
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# temp array 만들어서 특정 구간은 제외하고 값을 넣음
# 이후 다시 붙여넣음
# 붙여넣은 block에서 다시 temp array에 특정 구간 제외하고 값을 넣음
# 이후 다시 붙여넣음

temp_array = [0 for _ in range(n)]
temp_array_idx = 0

for i in range(n):
    if i < s1-1 or i > e1-1:
        temp_array[temp_array_idx] = blocks[i]
        temp_array_idx += 1
# print(temp_array)

for copy1 in range(n):
    blocks[copy1] = temp_array[copy1]

temp_array = [0 for _ in range(n)]
temp_array_idx = 0

for j in range(n):
    if j < s2-1 or j > e2-1:
        temp_array[temp_array_idx] = blocks[j]
        temp_array_idx += 1
# print(temp_array)

for copy2 in range(n):
    blocks[copy2] = temp_array[copy2]

total_cnt = 0
for idx in range(len(blocks)):
    if blocks[idx] != 0:
        total_cnt += 1
print(total_cnt)
for idx in range(len(blocks)):
    if blocks[idx] != 0:
        print(blocks[idx])