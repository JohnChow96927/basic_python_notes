# 如果在一个函数的定义中,使用了多个函数的参数形式,顺序如何制定
# SyntaxError: non-default argument follows default argument
# 缺省参数只能放在位置参数之后
# def func1(a, b=1, c):
#     print(a)
#     print(b)
#     print(c)

# 位置不定长参数
# 如果顺序赋值,位置参数和缺省参数先获取数据,多余的数据都被args接收
# def func1(a, b, c=1, *args):
#     print(a)
#     print(b)
#     print(c)
#     print(args)

# 上边这种形式好  还是下边????  下边
# 因为设置缺省参数的目的就是不需要频繁赋值,而将位置不定长参数放在缺省参数后,则需要先对缺省参数赋值,才能给位置不定长参数赋值.
# 而且,根据官方文档和内置函数来看,都是这么写的
# def func1(a, b, *args, c=1):
#     print(a)
#     print(b)
#     print(c)
#     print(args)

# 关键字不定长参数
# **kwargs 只能放在最后,否则就报错
def func1(a, b, *args, c=1, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


# func1(1, 2, 3, 4, 5, 6, 7)
# 多余的关键字参数才会被kwargs接收
func1(1, 2, 3, 4, 5, 6, c=10, app='douyin', stu='xiaoming', school='chuanzhi')

# 参数的顺序为:位置参数>位置不定长参数>缺省参数>关键字不定长参数

# 使用*args 和**kwargs 可以接收一切参数

# args 和 kwargs可以不赋值

#虽然我们讲了排布顺序,但是一般情况下不要在一个函数中出现两种以上的参数类型

