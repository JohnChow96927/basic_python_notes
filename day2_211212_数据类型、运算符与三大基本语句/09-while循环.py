# 循环语句:就是相同或者相似的事情,反复去做
'''
while 条件:
    条件成立,则反复执行while中的代码块
'''

# # 需求:说一万遍,传智播客好
# i = 0
# while i < 3:
#     print('传智播客好' + str(i))
#     i += 1
#
# #  练习题:循环打印5次
# i = 1
# while i <= 8:
#     print(f'第{i}次打印')
#     i += 1

# 分析: i 控制的是循环次数

# 拿到一个循环语句我们要分析如下事项
# 1.要循环多少次
# 2.从哪一个数值开始循环
# 3.循环的跳出条件
# 练习: 跑圈,跑10次
# i = 1
# while i <= 10:
#     print(f'我跑了{i}圈')
#     i += 1


# 死循环
# 死循环又叫无限循环,是程序的一种正常的执行状态,但是由于循环条件恒成立,所以不能跳出循环.
# i = 1
# while i <= 10:
#     print(f'我跑了{i}圈')

# 死循环是bug 么?  不是,程序员在开发中经常会使用死循环.

# 猜拳游戏升级

# 导入random模块
import random
player_score = 0
computer_score = 0

while True:
    # 获取用户所出的拳型
    player = int(input('请输入您要出的拳型:⽯头（1）／剪⼑（2）／布（3）'))

    # 获取电脑所出的拳型
    # randint是随机生成一个1-3之间的整数 randint的区间范围是左闭右闭的[1,3]
    computer = random.randint(1, 3)
    print(computer)

    # 比较判定胜利方
    result = player - computer

    if result == -1 or  result == 2:
        player_score += 1
        print('玩家获胜')
    elif result == 0:
        print('平局')
    else:
        computer_score += 1
        print('电脑获胜')
    print(f'玩家的分数是{player_score}, 电脑的分数是{computer_score}')

# while循环必须的元素有哪些?
# while 关键字
# 循环条件
# 循环体
