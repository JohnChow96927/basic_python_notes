# 在一个函数的定义内,嵌套函数的调用

# def sum1(num1, num2):
#     print(num1 + num2)


# # 需求: 求三个数的平均值
#
# # 三个数求和
# def sum_three(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# # 求三个数的平均值
# def avg_three(a, b, c):
#     return sum_three(a, b, c) / 3
#
#
# print(avg_three(4, 6, 8))
#
# # 调用过程
# # 1.记录函数名称及参数
# # 2.调用位置找到函数并执行函数体中的代码


# 思考

# 求三个数的平均值
def avg_three(a, b, c):
    return sum_three(a, b, c) / 3


# 三个数求和
def sum_three(num1, num2, num3):
    return num1 + num2 + num3


print(avg_three(4, 6, 8))
