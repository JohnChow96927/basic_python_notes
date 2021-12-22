# 什么叫做异常类型????
# FileNotFoundError: [Errno 2] No such file or directory: 'python.txt'
# FileNotFoundError 异常类型
#  [Errno 2] No such file or directory: 'python.txt' 异常信息
# open('python.txt', 'r')

# 怎样捕获指定类型的异常

'''
try:
    可能出现异常的代码
except 异常类型:
    捕获到指定类型异常后执行的代码

如果try中出现的是except中书写的异常类型,则可以被捕获
如果try中出现的不是except中书写的异常类型,则不能被捕获,程序依然终止运行
'''

# try:
#     # NameError: name 'a' is not defined
#     print(a)
# except FileNotFoundError:
#     # NameError: name 'a' is not defined
#     # 由于我们上方代码出现的NameError类型的异常,所以使用FileNotFoundError类无法捕获,抛出的异常会终止程序运行
#     print('出现了NameError异常')
#
# print('程序结束')

# 如果我想捕获多个异常类型需要怎么做???
'''
方法一:
try:
    可能出现异常的代码
except (异常类型1, 异常类型2):
    捕获到指定异常后执行的代码
'''

# try:
#     # print(a)
#     open('a', 'r')
# except (FileNotFoundError,NameError):
#     print('出现了异常')
#
'''
方法二:
try:
    可能出现异常的代码
except 异常类型1:
    出现异常类型1时执行的代码
except 异常类型2:
    出现异常类型2时执行的代码
......
'''

# try:
#     # print(a)
#     open('a', 'r')
# except FileNotFoundError:
#     print('没有找到该文件')
# except NameError:
#     print('没有定义该变量')
#
# print('程序结束')

# 如果我们不知道会出现哪种类型的异常,我们该怎么办???  # Exception
# try..except和分支语句一样,只有一个except中的代码会被执行,以为出现异常后,后续代码将不会继续执行,不会同时抛出两个异常
# try中的代码一般情况下不会抛出异常,所以绝大多数情况不会执行except中的命令

try:
    # print(a)
    print(1/0)
    open('a', 'r')
except FileNotFoundError:
    print('没有找到该文件')
except NameError:
    print('没有定义该变量')
except Exception:
    print('出现未知异常')

print('程序结束')
