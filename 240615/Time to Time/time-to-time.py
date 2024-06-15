a, b, c, d = map(int, input().split())
# first_elapsed_time = 0
# second_elapsed_time = 0
# min, hour = 0, 0

# while 1:
#     if hour == a and min == b:
#         break
#     if min == 60:
#         hour += 1
#         min = 0 
#     min += 1
#     first_elapsed_time += 1
# # print(first_elapsed_time)

# while 1:
#     if hour == c and min == d:
#         break
#     if min == 60:
#         hour += 1
#         min = 0 
#     min += 1
#     second_elapsed_time += 1
# print(second_elapsed_time)

print((c * 60 + d)-(a * 60 + b))