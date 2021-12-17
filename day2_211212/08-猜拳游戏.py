'''
1/输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）

2/电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能

3/⽐较胜负
'''
# 了解:在Python中有一个随机模块
# random模块
# import random
#
# # 获取用户所出的拳型
# player = int(input('请输入您要出的拳型:⽯头（1）／剪⼑（2）／布（3）'))
#
# # 获取电脑所出的拳型
# # randint是随机生成一个1-3之间的整数 randint的区间范围是左闭右闭的[1,3]
# computer = random.randint(1, 3)
#
# # 对于拳型进行判断得出输赢方
# if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
#     print('电脑获胜')
# elif player == computer:
#     print('平局')
# else:
#     print('玩家获胜')



'''
p  c   win  差值
1  1    平   0
1  2    p    -1
1  3    c    -2
2  1    c    1
2  2    平   0
2  3    p   -1
3  1    p    2
3  2    c    1
3  3    平   0
'''

# 导入random模块
import random

# 获取用户所出的拳型
player = int(input('请输入您要出的拳型:⽯头（1）／剪⼑（2）／布（3）'))

# 获取电脑所出的拳型
# randint是随机生成一个1-3之间的整数 randint的区间范围是左闭右闭的[1,3]
computer = random.randint(1, 3)
print(computer)

# 比较判定胜利方
result = player - computer

if result == -1 or  result == 2:
    print('玩家获胜')
elif result == 0:
    print('平局')
else:
    print('电脑获胜')


