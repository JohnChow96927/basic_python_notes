# lambda匿名函数的作用就是快速定义一个简单的匿名函数
# 定义格式: lambda 参数列表: 返回值表达式

print(type(lambda num1, num2: num1 + num2))  # <class 'function'>


def sum1(num1, num2):
    return num1 + num2


print(type(sum1))  # <class 'function'>

# 无论使用def 定义,还是使用lambda定义只不过定义格式不同,但是本质上都是在定义函数

# lambda 的调用格式
# 格式1: (lambda表达式)(参数1, 参数2,,,,)
print((lambda num1, num2: num1 + num2)(2, 3))
# 这种方式,虽然不用定义变量名,但是只能使用一次,下一次使用必须重新定义函数

# 格式2:
# 使用变量接收lambda表达式,直接使用变量()调用函数
sum2 = lambda num1, num2: num1 + num2
print(sum2(2, 3))
# 使用变量接收后可以使用多次,直到变量被销毁为止

# lamdba作用
# 1.简化代码
# 2.可以当做参数进行传递
# list1 = [1, 4, 5, 3, 2]
# list1.sort()

# list2 = [(2, 3), (4, 1), (3, 5), (6, 2)]
# 需求: 根据列表内元组中下标为1的元素的大小进行排序
# 此时需要使用key进行规则传递
# list2.sort(key=lambda x:x[1])
# print(list2)


# lambda的缺点
# 1.不能书写复杂函数,变量定义,分支语句,循环语句等都不能书写在lambda中
# lambda a,b:for i in range(10):print(111)
# 2.lambda可读性较差,稍微长一点的语句就不容易读懂
# 需求: 使用lambda函数书写一个函数可以判断两个数字间的较大值
# 三目运算符: 条件成立时返回的数据  if  条件 else  条件不成立时返回的数据
max1 = lambda a, b: a if a > b else b

print(max1(9, 6))
