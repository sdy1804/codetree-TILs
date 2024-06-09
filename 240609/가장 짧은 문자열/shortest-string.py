string_1 = input()
string_2 = input()
string_3 = input()

longest_str = max(len(string_1), len(string_2), len(string_3))
shortest_str = min(len(string_1), len(string_2), len(string_3))

print(longest_str - shortest_str)