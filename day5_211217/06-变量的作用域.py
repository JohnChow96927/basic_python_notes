# 全局变量:全局变量创建后在之后的函数中都可以使用
# 全局变量,也要遵循先定义后调用的原则

# 一般是在文件中顶格书写,在全局范围内生效的变量
num = 100


def func_a():
    print(num)


func_a()


def func_b():
    print(num + 2)


func_b()


# 局部变量: 在函数体内部定义,并且只能在函数体中使用的变量叫做局部变量

def func_c():
    b = 10
    print(b)


func_c()

# NameError: name 'b' is not defined
# 局部变量,不能在函数体外部调用,或者说局部变量在出了作用域后,就会被释放
# print(b)

# 注意: 形参的作用域也是函数体内部,出了函数体无法继续使用
# def sum1(a, b):
#     print(a + b)
#
# # NameError: name 'a' is not defined
# print(a)
# print(b)

# 注意:在函数体内部定义了局部变量,则同名全局变量无法被调用
num = 100


def func_d():
    num = 5
    print(num)


func_d()
