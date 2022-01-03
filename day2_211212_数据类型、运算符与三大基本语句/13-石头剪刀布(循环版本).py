import random

# 1.   设置两个玩家 player computer
# 2.   player: 从控制台输⼊要出的拳 ⽯头(1)／剪⼑(2)／布(3)
# 3.   computer: 电脑 随机 出拳
# 4.   player和computer⽐较胜负
try:
    game_rule = {1: '👊', 2: '✌️', 3: '✋'}
    score_board = {'player': 0, 'computer': 0}
    i = 0
    while abs(score_board['player'] - score_board['computer']) <= 5:
        player = int(input("请出拳 ⽯头(1)／剪⼑(2)／布(3):"))
        computer = random.randint(1, 3)
        result = player - computer

        # 1 玩家胜出
        if result == -1 or result == 2:
            print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
            print("恭喜你胜利了")
            score_board['player'] += 1
            print(f"当前比分为您 {score_board['player']} : {score_board['computer']} 电脑")
        # 2 平局
        elif result == 0:
            print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
            print("再战300回合")
            print(f"当前比分为您 {score_board['player']} : {score_board['computer']} 电脑")
        # 3 玩家失败
        else:
            print(f'您出{game_rule[player]}，电脑出{game_rule[computer]}')
            print("您输了")
            score_board['computer'] += 1
            print(f"当前比分为您 {score_board['player']} : {score_board['computer']} 电脑")
        # 设置终止条件
        i += 1
    print(f"最终比分为您 {score_board['player']} : {score_board['computer']} 电脑")
    if score_board['player'] > score_board['computer']:
        print("恭喜您胜利了！")
    # elif score_board['player'] == score_board['computer']:
    #     print("平局，真是旗鼓相当的对手！")
    else:
        print("很遗憾，您输了！")
except KeyError as e:
    print('您出的是个啥呀？（请输入1、2、3中的一个数）' + str(e))

