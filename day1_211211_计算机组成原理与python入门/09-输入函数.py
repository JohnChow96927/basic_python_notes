# input函数
# 特点:
# 1 input会阻塞等待数据的到来 直到获取到数据并且按了回车 才会继续运行
# 2 input前面绝大多数情况都会有一个变量接受数据
# 3 所有的通过input接受到的数据全部默认按照字符串对待
pass_word = input("请输入密码:")
print(type(pass_word))
print('您输入的年龄为：' + input('请输入你的年龄：'))

