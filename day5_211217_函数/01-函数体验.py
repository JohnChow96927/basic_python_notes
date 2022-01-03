'''
函数定义:
def 函数名(参数列表):
    函数体
    return 返回值

调用函数:
函数名(传参)
'''


def print_option():
    print('进入功能界面')
    print('圣诞节广告')


print('输入密码')
print_option()

print('取款完成')
print_option()

print('存款完成')
print_option()


# 如果我们想要修改功能页面展示效果,我们需要修改几个地方? 1个

# 函数可以增加代码的重用率,复用率, 提高开发效率,同时方便后期迭代和维护

'''
要求：定义一个函数，能够输出自己的姓名和年龄，并且调用这个函数让它执行

使用def定义函数
编写完函数之后，通过 函数名() 进行调用
'''

# def print_stu_info():
#     print('我的名字是小明')
#     print('我的年龄是18岁')

# 必须调用函数才能执行函数中的相关功能
# print_stu_info()

# NameError: name 'print_stu_info' is not defined
# 函数要先定义后调用,否则就会报错
# def print_stu_info():
#     print('我的名字是小明')
#     print('我的年龄是18岁')

# 函数名和变量名本质上是一样的,只不过函数内存放的是功能, 变量内存放的是数值
# (了解)本质上函数和变量内部储存的都是引用地址,只不过函数名储存的是function对象的引用地址,变量名内部储存的是其他数据类型的引用地址
