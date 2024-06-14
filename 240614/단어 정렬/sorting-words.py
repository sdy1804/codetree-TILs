n = int(input())
alphabet = [input() for _ in range(n)]

alphabet.sort()

for elem in alphabet:
    print(elem)