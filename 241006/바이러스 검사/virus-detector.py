n = int(input())
num_cumstomer = list(map(int, input().split()))
max_teamleader, max_member = map(int, input().split())

# 팀장은 무조건 1로 고정
# 팀장이 검사하고 남은 명수 // 팀원 한 명당 검사가능한 사람 수 -> 필요한 팀원 수
# 팀장이 검사하고 남은 명수 % 팀원 한 명당 검사가능한 사람 수 -> 0이 아니면 팀원 +1

for stores in range(n):
    num_member = (num_cumstomer[stores] - max_teamleader) // max_member
    if (num_cumstomer[stores] - max_teamleader) % max_member != 0:
        num_member += 1
    # 팀장
    num_member += 1

num_member *= n
print(num_member)