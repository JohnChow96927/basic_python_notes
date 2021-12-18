# # tuple12 = (1, 2, 3, 4)
# #
# #
# # def fun1():
# #     return (1,2,3,4)
# #
# #
# # print()
# #
# #
# # print(fun1() is tuple12)
# # dict1 = {'name': 'John', 'age': 18, }
# #
# #
# # def func1(dict):
# #     result = dict
# #     result['gender'] = 'male'
# #     result['id'] = 'z5233652'
# #
# #
# # func1(dict1)
# # print(dict1)
#
# # lambda匿名函数的作用就是快速定义一个匿名函数
# # 格式：lambda 参数列表：返回值表达式
# # lambda的调用格式
# # 格式1：（lambda表达式）（参数1，参数2，……）
# print((lambda num1, num2: num1 + num2)(2, 3))
#
# # 格式2:
# sum2 = lambda num1, num2: num1 + num2
# print(sum2(2, 3))
#
# # lambda作用
# # 1.简化代码
# # 2.当做参数进行传递
# list2 = [(2, 3), (4, 1), (3, 5), (6, 2)]
# list2.sort(key=lambda x: x[1])
#
# # lambda的缺点
# # 1.不能书写复杂函数：变量定义、循环语句等都不支持
# # 2.可读性较差，稍微长一点的语句就不容易读懂
#
#
# a = 10,
# print(type(a))  # tuple
