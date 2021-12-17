# 如果想在函数体内部修改全局变量的值,则需要使用global关键字进行声明

# apples_count = 5
#
#
# def eat_apple(num):
#
#     # 直接使用符合赋值运算符,会先计算apples_count - num,此时apples_count没有定义所以会报错
#     # apples_count -= num
#     # 此处相当于重新定义了一个局部变量,并没有修改全局变量的值
#     apples_count = 5
#     apples_count -= num
#     print(f'我吃了{num}个苹果,还剩{apples_count}个')
#
#
# eat_apple(2)
#
# print(apples_count)


apples_count = 5


def eat_apple(num):
    # 此处 想要修改全局变量的值,可以使用global关键字进行声明
    # SyntaxError: name 'apples_count' is assigned to before global declaration
    # global声明变量必须在该变量调用之前
    apples_count -= num
    global apples_count
    print(f'我吃了{num}个苹果,还剩{apples_count}个')


eat_apple(2)

print(apples_count)

# # 了解
#
# a = 111
#
# def func_out():
#     a = 100
#     def func_in():
#         # 如果想让他使用外部函数中的变量可以使用nonlocal
#         nonlocal a
#         a += 1
#         print(a)
#     func_in()
#
#
# # 有三个变量a   一个是全局变量 111  一个是外部函数中的变量  100  还有一个是函数体内部的复合赋值运算
# # 现在我想让他使用外部函数中的变量需要怎么做??
# func_out()