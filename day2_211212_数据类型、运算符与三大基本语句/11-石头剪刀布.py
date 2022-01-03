import random

# 1.   设置两个玩家 player computer
# 2.   player: 从控制台输⼊要出的拳 ⽯头(1)／剪⼑(2)／布(3)
# 3.   computer: 电脑 随机 出拳
# 4.   player和computer⽐较胜负
game_rule = {1: '👊', 2: '✌️', 3: '✋'}
player = int(input("请出拳 ⽯头(1)／剪⼑(2)／布(3):"))
computer = random.randint(1, 3)

# 1 玩家胜出
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
    print("恭喜你胜利了")
# 2 平局
elif player == computer:
    print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
    print("平局，再战300回合")
# 3 玩家失败
else:
    print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
    print("你输了")
