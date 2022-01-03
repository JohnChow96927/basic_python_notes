# 形参
# 1.位置参数:按照顺序进行书写的参数名称
# 形参按照顺序接收实参传递过来的值,有多少个形参就接收多少个实参,不能多 也不能少
def func1(a, b, c):
    print(a, b, c)


# 2.缺省参数(默认参数):在定义函数时,给形参一个默认值,如果给其赋值,就使用赋的值,如果不赋值,就使用默认值
def func2(a, b, c=10):
    print(a, b, c)


# 3.不定长参数

# 位置不定长参数 *args

# 需求:计算多个数字的和,数字个数不确定
def sum_somenums(*args):
    # 位置不定长参数接收了所有顺序赋值的数据,并且将其打包为元组,放入了args变量中
    print(args)  # (1, 2, 3, 4, 5, 6)
    sum1 = 0
    for i in args:
        sum1 += i

    return sum1


print(sum_somenums(4, 5, 6, 7))

sum_somenums(1, 2, 3, 4, 5, 6)


# 关键字不定长参数  **kwargs
def print_somthing(**kwargs):
    # 将关键字赋值得到的值,进行拆分,形参名作为键,值作为值,打包成一个字典,放入kwargs 当中
    print(kwargs) # {'a': 1, 'b': 2, 'c': 3}



# TypeError: print_somthing() takes 0 positional arguments but 4 were given
# print_somthing(1, 2, 3, 4)
# 关键字不定长参数不能通过顺序赋值进行赋值,而是要使用关键字参数进行赋值

print_somthing(a=1, b=2, c=3)


# 如果不给c赋值,则c默认为10
# func2(2, 3)
# 如果给c赋值,就使用赋的值
# func2(4, 5, 6)


# 实参

# 1. 顺序赋值
# func1(1, 2, 3)

# 2. 关键字赋值 使用 形参名= 值的形式进行赋值
def func3(a, b, c):
    print(a, b, c)

# func3(1, 2, 3)
# func3(a=1, b=2, c=3)
# 注意: 使用关键字参数赋值,不能遗漏,也不能重复赋值
# TypeError: func3() missing 1 required positional argument: 'c'
# func3(a=1, b=2)

# TypeError: func3() got multiple values for argument 'a'
# func3(1,2,a=3)

# 注意:使用关键字参数赋值时,除非有关键字不定长参数,否则要注意参数名必须存在
# func3(a=1,b=2,c=3, d=4)

# 注意: 使用关键字参数赋值不需要按序赋值
# func3(b=2, c=3, a=1)
