class Bomb:
    def __init__(self, code, color, second):
        self.code =code
        self.color = color
        self.second = second

bomb_code, color, second = input().split()
bomb1 = Bomb(bomb_code, color, second)

print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.second}")