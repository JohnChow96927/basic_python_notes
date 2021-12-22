# finally:最终,最后的意思在所有try...except中代码执行结束后,不管有没有异常,都会执行finally

'''
格式:
try:
    可能出现异常的代码
except:
    出现异常后执行的代码
else:
    没有出现异常时执行的代码
finally:
    无论是否出现异常都会执行的代码
'''

# try:
#     # a = 1
#     print(a)
# except:
#     print('出现异常了')
# else:
#     print('没有出现异常')
# finally:
#     print('无论是否出现异常都会执行')

# 如果不写finally 将代码到try..except之外会怎样?
# 无论是否出现异常,上下两个代码块的执行效果完全一致
# try:
#     # a = 1
#     print(a)
# except:
#     print('出现异常了')
# else:
#     print('没有出现异常')
#
# print('无论是否出现异常都会执行')

# finally可以可以增强可读性,提高逻辑的严谨性
# finally 无论什么情况下都会被执行,哪怕报错
# 比如关闭文件,日志处理,奔溃日志采集等等都可以使用finally


# try:
#     # input('请输入您要删除的金额')
#     print(a)
# except FileNotFoundError:
#     print('异常出现了')
# else:
#     print('异常没有出现')
# finally:
#     print('怎样都拦不住我执行')

# try:
#     # input('请输入您要删除的金额')
#     print(a)
# except FileNotFoundError:
#     print('异常出现了')
# else:
#     print('异常没有出现')
#
# print('一不小心就拦住了')