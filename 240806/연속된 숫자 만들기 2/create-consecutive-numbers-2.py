arr = list(map(int, input().split()))
arr.sort()
# case 1 : 각 숫자 간격이 2 이상일 때 -> 2, 6, 9
# case 2 : 두 숫자 간격이 2일 때 -> 2, 4, 9 => 1번 이동 / 2, 4, 6 => 1번 이동
# case 3 : 모든 숫자 간격이 1 일 때 -> 2, 3, 4 => 0번 이동

if abs(arr[0] - arr[1]) > 2 and abs(arr[1] - arr[2]) > 2:
    print(2)
elif abs(arr[0] - arr[1]) == 2 or abs(arr[1] - arr[2]) == 2:
    print(1)
elif abs(arr[0] - arr[1]) == 1 and abs(arr[1] - arr[2]) == 1:
    print(0)