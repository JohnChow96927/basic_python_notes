# break 是打破当前循环,也就是跳出当前循环的意思

# 需求: 在吃苹果,如果吃到一般吃到半条虫子会怎样??  不吃了
# 执行到break之后,循环异常终止,所有break之后的代码不会继续执行

apples_count = 5

i = 1
while i <= 5:
    # 当吃到第三个苹果的时候,有半条虫子
    if i == 3:
        print('有半条虫子,不能再吃了,不然到肚子里合体了')
        break
    print(f'我吃完了第{i}个苹果')
    i += 1

# break之后不需要写任何代码,除非,放到分支语句中
# while i <= 5:
#     break
#     if i == 1:
#         print('123')
#     i += 1
