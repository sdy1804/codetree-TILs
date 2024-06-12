def conti_part_seq(A, B):
    if B in A:
        return "Yes"
    else:
        return "No"

n1, n2 = map(int,input().split())
seq1 = input()
seq2 = input()
print(conti_part_seq(seq1, seq2))