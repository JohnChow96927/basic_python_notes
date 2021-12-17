# 函数的说明文档,就是对函数的使用方式进行解释说明的一个文档注释

# 定义函数
# 需求: 四则运算计算器的开发

# def compute(num1, num2, symbol):
#     '''文档注释其实就是在函数的第一行书写的注释
#         文档注释不会参与到程序的运行当中
#     '''
#     if symbol == '+':
#         return num1 + num2
#     elif symbol == '-':
#         return num1 - num2
#     elif symbol == '*':
#         return num1 * num2
#     elif symbol == '/' and num2 != 0:
#         return num1 / num2
#     else:
#         return '数据有误'

# 按照语法规范一般文档注释使用三对双引号
# 在三对双引号中间敲击回车会自动提示参数及返回值的说明信息
def compute(num1, num2, symbol):
    """
    作用:计算两个数字之间的四则运算
    :param num1: 参与计算的第一个数字 (int float)
    :param num2: 参与计算的第二个数字 (int float)
    :param symbol: 计算符号 (str) + | - | * | /
    :return: 两个数字计算的结果
    """
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


# 在函数调用位置,鼠标悬停到函数名上方,会自动弹出文档注释,提示用户该函数的调用方法及工能
print(compute(3, 4, '+'))


# 一般书写详细的文档注释只是使用在需要别人调用的函数或方法上


# 练习
# 写一个函数打印一条横线
# 打印自定义行数的横线

def print_line():
    """打印横线"""
    print('-' * 30)


def print_lines(num):
    """打印num行横线"""
    for i in range(num):
        print_line()


print_lines(8)
