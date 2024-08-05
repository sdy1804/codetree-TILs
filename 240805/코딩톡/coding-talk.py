n, m, p = map(int, input().split())
arr = [list(input().split()) for _ in range(m)]
for i in range(len(arr)):
    arr[i][1] = int(arr[i][1])

# 인원 수에 해당하는 참여자 리스트 생성
# arr에서 p부터 탐색 시작점
# p 이후에 오는 사람들은 읽었다는 것이 확실하므로 제외
# p 순서에 해당하는 작성자도 제외
programmers = []
for i in range(ord('A'), ord('A')+n):
    programmers.append(chr(i))

if arr[p-1][1] == 0:
    programmers.clear()

for msg in range(p-1, len(arr)):
    if arr[msg][0] in programmers:
        programmers.remove(arr[msg][0])
if arr[p-1][1] == arr[p-2][1]:
    programmers.remove(arr[p-2][0])

for elem in programmers:
    print(elem, end=" ")