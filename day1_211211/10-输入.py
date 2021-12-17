# 输入:程序员将数据传递到计算机中
# 输入的函数时input
# 进程结束,并且退出程序,code = 0 证明是合法退出没有出现报错或异常
# Process finished with exit code 0
# input是一个阻塞函数,执行到该代码时,会等待用户输入,输入后,代码继续执行.
# input('请输入一个字母:')

# input函数括号内是提示文字,也就是告诉用户输入数据的内容或者规则用的,不能输入到计算机中,而是输出到控制台

# 程序员手动输如的数据内容可以使用变量接收

# age = input('请输入你的年龄:')
#
# print('你的年龄是%s' % age)

# 使用input 接收的所有数据都是字符串数据类型

# num = input('请输入一个数字:')
# # TypeError: %d format: a number is required, not str
# print(type(num)) # <class 'str'>
# print('您输入的数字是:%d' % num)


# 从键盘上录入苹果的价格 、重量 ，输出: 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元.

price = float(input('请输入苹果的价格:'))
weight = float(input('请输入您要购买的重量:'))

# TypeError: can't multiply sequence by non-int of type 'str'
# 字符串数据类型之间不能进行数据的乘法运算
print(f'苹果单价 {price:.2f} 元／⽄，购买了 {weight:.2f} ⽄，需要⽀付 {price * weight:.2f} 元')

# 了解:如果想要进行数据类型转换,那么想转换为什么数据类型,就给这个数据穿一个什么数据类型的衣服
# 例如 现在想把'123'转换为int类型,  int('123')

# print('123')
# print(type('123'))
# print(type(int('123')))


print('123\t12\t\n12\t123\t')