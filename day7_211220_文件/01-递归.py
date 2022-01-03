# 了解:  只需要知道什么是递归即可

# 算法: 就是讲数学逻辑用编程方式实现的一种思想

# 递归: 在函数内部调用函数本身.就是递归

# def func1():
#     return func1()
#
# func1()

# 如果我们想要利用递归就不能让函数无限递归下去

# 需求: 计算1-100的累加和

'''
f(1) = 1
f(2) = 1 + 2 = f(1) + 2
f(3) = 1 + 2 + 3 = f(2) + 3
f(4) = 1 + 2 + 3 + 4 = f(3) + 4
...
f(n) = 1 + 2 +... + n = f(n-1) + n
'''

def sum_num(num):
    # 使用递归时,要有明确的跳出条件
    if num == 1:
        return 1
    return sum_num(num-1) + num

# RecursionError: maximum recursion depth exceeded in comparison
# 超出了内存的最大调用深度,在Python中默认函数最多可以嵌套1000层,超出了就会报错
print(sum_num(998))

# 递归就是将一个复杂问题拆解为多个相同或相似的简单问题的思维方式

# 总结:
# 递归就是讲一个复杂问题拆分为多个相同或相似的简单问题的思维方式
# 递归要在函数内部调用函数本身
# 递归要有明确的跳出条件
# 递归不能超出最大调用深度

# 斐波那契数列
# 需求: 第三个数字是前两个数字之和

def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(50))

# 递归,我们在开发初期,尽量不要使用,算力消耗大,容易出错
