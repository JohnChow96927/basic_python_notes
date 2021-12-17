# continue: 结束本次循环,直接进入下一次循环

# 需求: 吃苹果,一共五个苹果,迟到第三个苹果的时候迟到一条虫子, 扔掉这个苹果,继续吃下一个
# continue 不影响循环语句的循环次数
# 但是在一次循环中,如果执行了continue 将会立即进入下一次循环,后边的代码将不会继续执行
# 使用while循环中的continue 时,要注意循环变量的自增

apples_count = 5

i = 1
while i <= 5:
    if i == 3:
        print('吃到了一条虫子,这个苹果扔了吧')
        i += 1
        continue
    apples_count -= 1
    print(f'我吃了{5 - apples_count}个苹果')
    i += 1

# break 和continue 的注意事项
# 1. break 和continue在循环体中使用,否则报错

if i == 5:
    # 'break' outside loop
    # break
    # 'continue' outside loop
    # continue
    pass
# 2.break 和continue 只能控制自身所在的循环结构

for i in range(1, 6):
    for j in range(1, i+1):
        if j == 3:
            break
        print('*', end=' ')
    print()

# break 和continue 是循环控制关键字,所以说一般情况下是在循环的次数,或者循环的内容要进行控制时才会使用
# 所负责的区域,就是关键字所在的循环体

