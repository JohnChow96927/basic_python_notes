# 函数的参数就是在使用函数时可以从函数外部动态的向函数内部传递数据,增加函数的灵活性,提高函数复用率

def compute(num1, num2):
    print(num1 + num2)


compute(1, 5)


# 如果不适用参数,我们就需要将数据写入函数体内例如:

def compute1():
    print(1 + 5)


compute1()

# 此时我想计算2 + 3

# 如果有参数则直接使用函数传参即可
compute(2, 3)


# 如果没有参数, 则需要重新定义一个函数


def sum1(num1, num2, num3):
    # print(a)
    print(num1 + num2 + num3)


# 在程序执行后,我们先将函数进行记录,加载到函数列表中
# 当调用函数时,参会执行函数体中的代码

# 在调用函数时,会将函数的参数动传递到函数体内部,按照顺序依次接收调用位置的值
# 在函数定义时添加的参数,叫做形参
# 在函数调用时添加的参数,叫做实参
# sum1(3, 4, 5)

# TypeError: sum1() missing 1 required positional argument: 'num3'
# 在调用函数时,必须保证每一个位置参数均被赋值,否则会报错
# sum1(1, 2)

# TypeError: sum1() takes 3 positional arguments but 4 were given
# 实参过多,没有形参可以接收也会报错
# sum1(1, 2, 3, 4)

# 练习:
# 需求: 有一个compute函数可以进行两个数值间的四则运算
# def定义一个函数, 有三个参数 num1  num2  symbol  调用函数 print输出结果

def compute(num1, num2, symbol):
    if symbol == '+':
        print(num1 + num2)
    elif symbol =='-':
        print(num1 - num2)
    elif symbol == '*':
        print(num1 * num2)
    elif symbol == '/' and num2 != 0:
        print(num1 / num2)
    else:
        print('输入有误')

# 不调用函数,不会执行函数体中的代码
compute(3, 4, '$')

