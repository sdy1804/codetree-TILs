n = int(input())
arr = [int(input()) for _ in range(n)]
# print(arr[3] % 10)
# arr[i], arr[i+1], arr[i+2]로 완전 탐색
# 각 자릿수 뜯어내기 -> 몫 또는 나머지 사용
# 천의 자리 : // 1000
# 백의 자리 : // 100 % 10
# 십의 자리 : // 10 % 10
# 일의 자리 : % 10
# 캐리 여부 확인 -> 캐리 없으면 all_carry = True, 합을 구하고, 최대 합과 비교
# 전부 다 캐리면 -1 출력

all_carry = True
total_max = 0
for i in range(len(arr) - 2):
    for j in range(i+1, len(arr) - 1):
        for k in range(j+1, len(arr)):
            # print(arr[i], arr[j], arr[k])
            if (arr[i] % 10 + arr[j] % 10 + arr[k] % 10) < 10:
                if (arr[i] //10 % 10 + arr[j] //10 % 10 + arr[k] //10 % 10) < 10:
                    if (arr[i] //100 % 10 + arr[j] //100 % 10 + arr[k] //100 % 10) < 10:
                        if (arr[i] //1000 + arr[j] //1000 + arr[k] //1000) < 10:
                            now_max = arr[i] + arr[j] + arr[k]
                            total_max = max(total_max, now_max)
                            all_carry = False
print(total_max)
if all_carry:
    print(-1)