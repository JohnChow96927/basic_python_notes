# FileNotFoundError
# 出现异常后,程序会终止运行,在异常代码之后的所有代码将不会继续执行
# file = open('chuanzhi.txt', 'r', encoding='utf8')
# 所以我们要在异常出现后,处理异常,防止影响我们正常代码的运行
# print('程序结束')

# 异常捕获的基本形式
'''
try:
    可能出现异常的代码片段
except:
    如果try中的代码出现异常,则执行except中的代码
'''

try:
    # 此处没有终止程序运行
    open('chuanzhi.txt', 'r', encoding='utf8')
    # 上边一行代码出现异常,下边的代码均不会被执行
    print('文件开启成功,开始读文件')
except:
    # try中的代码出现异常,则执行except来处理异常,不会造成程序终止运行
    print('打开文件失败,没有对应的文件')

# 由于程序没有终止,所以try...except执行结束后,将继续执行后续代码
print('程序结束')

# 结论:
# 1.try中代码块内部,如果出现异常代码,异常代码之后的所有代码不会继续执行
# 2.try中的代码出现异常后,立即执行except中的代码处理异常
# 3.将可能出现异常的代码写入try中,不会终止程序运行
# 4.try...except执行结束后,将继续向下执行.