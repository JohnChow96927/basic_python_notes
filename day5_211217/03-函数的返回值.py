# 返回值,就是根据函数中数据的计算或运行内容,将函数中的数据传递到函数外部的一种方式


# def sum1(num1, num2):
#     print(num2 + num1)


# 思考,上边的函数,我们想在其计算结果的基础上乘以2 怎么做?
# 我们只能在函数体内进行修改,所以想在函数体外部修改,就需要使用到返回值

def sum2(num1, num2):
    return num1 + num2


# 在控制台输出数据,是print的功能,不是没有输出就没有返回值
# 可以使用print将返回值进行打印
# print(sum2(3, 4) * 2)

# 一般有返回值的函数,我们会使用变量接收其返回值
result = sum2(2, 3) * 2
print(result)

# 如果没有返回值,或默认返回None

list1 = [1, 2, 3, 4]
# 此时append方法返回None,证明其没有返回值
print(list1.append(5))  # None

import random

print(random.randint(1, 3))

# 严格的来讲,没有返回值的函数时不存在的,如果没有书写返回值,则自动返回None
