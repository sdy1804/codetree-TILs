class Seq:
    def __init__(self, val, befPos, aftPos):
        self.val = val
        self.befPos = befPos
        self.aftPos = aftPos

# 체크해야 할 점 : 인스턴스들을 리스트1에 저장한 후, 리스트2로 소팅을 하면 과연 리스트2에 인스턴스 내용들이 그대로 있는가? -> Yes
# 객체 참조

N = int(input())
arr = list(map(int, input().split()))

info = []
for index in range(len(arr)):
    info.append(Seq(arr[index], index+1, 0))

sorted_info = []
sorted_info = sorted(info, key=lambda x: x.val)
# print(sorted_info[3].val)
# print(sorted_info[3].befPos)
for index in range(len(arr)):
    sorted_info[index].aftPos = index + 1
    # print(f'{sorted_info[index].val}, {sorted_info[index].befPos}', sorted_info[index].aftPos)

for index in range(N):
    print(info[index].aftPos, end=" ") # sorted_info에서 참조하는 객체들이 info에서도 참조되는 것을 이용.

# for i in range(1, N+1):
#     for j in range(N):
#         if i == sorted_info[j].befPos:
#             print(sorted_info[j].aftPos, end=" ")