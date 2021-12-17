# 在函数中return之后的所有内用将不会继续执行

def func1():
    print('chuanzhi')
    print('python')
    return
    print('hello java')
    print('hello bigdata')


func1()


# 在分支语句中,如果一个分支有返回值,尽量保证所有的分支都有返回值
# 在分支语句中,尽量保证每个分支的返回值类型相同

def compute(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/' and num2 != 0:
        return num1 / num2
    else:
        return '数据有误'


# return 本质上return只能返回一个数据,如果返回多个数据,则需要使用容器包裹起来

def func3():
    return 1, 2, 3, 4


# 如果返回多个数据,用逗号隔开,默认打包为一个元组
print(func3())  # (1, 2, 3, 4)


# def func4():
#     return 3
#     return 4
#     return 5

# return如果不返回任何数据,默认返回None
# 只写return 没有返回值,或者不写return都会默认返回None

def func5():
    return


print(func5())  # None


def func6():
    pass


print(func6())  # None

# 练习
# 打印直角三角形 可以指定打印的行数, 并且在打印完成后,会返回星星的个数

'''
*
* *
* * *
* * * *
'''


# 打印一个三角形
# for i in range(5):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()

# 将打印三角形的代码封装到函数中
# def print_triangle(num):
#     for i in range(num):
#         for j in range(i + 1):
#             print('*', end=' ')
#         print()
#
#
# print_triangle(7)

# 返回*的个数
def print_triangle(num):
    sum1 = 0
    for i in range(num):
        for j in range(i + 1):
            print('*', end=' ')
            sum1 += 1
        print()
    return sum1


print(print_triangle(4))
