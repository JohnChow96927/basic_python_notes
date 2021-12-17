# L:local  函数体内部
# E:edge   外部函数中(函数定义的嵌套)
# G:global 全局范围内
# B:built-in 内置变量

# LEGB原则就是Python中用于查询变量及函数顺序
# 举例
a = 100


def func1():
    # 使用变量时,先从函数体内部查找,如果函数体内部有该变量则使用
    a = 1
    print(a)  # 1


def func2():
    # 使用变量时,如果函数体内部没有该变量,则去外部函数的函数体中查找,如果有则使用
    a = 5

    def func3():
        print(a)

    func3()


def func4():
    # 使用变量时,如果函数体内部没有该变量,外部函数中也没有,则去全局变量中查找
    print(a)


def func5():
    # __file__是获取当前文件所在位置的绝对路径的
    # __file__ 在函数体内部,外部函数中和全局变量中都不存在,则去内置变量中进行查找
    print(__file__)


# func1()
#
# func2()
#
# func4()
#
# func5()


# legb应用
# def func6():
#     # UnboundLocalError: local variable 'a' referenced before assignment
#     # 根据legb原则,查找函数体内部是否存在a,查找到局部变量a,但是他是调用之后定义的,所以报错
#     print(a)
#     a = 1
#     print(a)
#
#
# func6()

# def func7():
#     # UnboundLocalError: local variable 'a' referenced before assignment
#     # a += 1  a = a + 1  根据legb原则发现有a的定义操作,但是要先计算出a+1的值才能赋值,此时相当于还没有定义就使用了a
#     a += 1
#
# func7()