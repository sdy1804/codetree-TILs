A_cold, A_temp = input().split()
B_cold, B_temp = input().split()
C_cold, C_temp = input().split()

A_temp, B_temp, C_temp = int(A_temp), int(B_temp), int(C_temp)

if (A_cold == 'Y') and (A_temp >= 37):
    if ((B_cold == 'Y') and (B_temp >= 37)) or ((C_cold == 'Y') and (C_temp >= 37)):
        print("E")
    else:
        print("N")
else:
    if ((B_cold == 'Y') and (B_temp >= 37)) and ((C_cold == 'Y') and (C_temp >= 37)):
        print("E")
    else:
        print("N")