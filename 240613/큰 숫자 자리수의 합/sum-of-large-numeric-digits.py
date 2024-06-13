a, b, c = map(int, input().split())
multi = a * b * c

def big_num_sum(multi):

    if multi < 10:
        return multi
    return big_num_sum(multi // 10) + big_num_sum(multi % 10)

print(big_num_sum(multi))