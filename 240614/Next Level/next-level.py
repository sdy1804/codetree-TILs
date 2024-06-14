class User:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user1 = User('codetree', 10)
ID, LV = input().split()
user2 = User(ID, LV)

print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")