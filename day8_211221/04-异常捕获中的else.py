# else:当try中的代码全部执行完成没有出现任何异常时,会执行else中的命令

'''
try:
    可能出现异常的代码
except:
    出现异常后执行的代码
else:
    没有出现异常时执行的代码

结论: excetp和else 必定只有一个可以被执行
'''

try:
    # a = 1
    print(a)
except:
    print('出现异常啦')
else:
    print('没有出现异常')

# 下方代码和上方代码有什么区别????
# 将代码写入esle 和写入try的代码块下方语法上是完全一样的
# else可以增强代码的可读性
# 在开发中,要保证try中的代码尽可能的少,方便定位异常,以及对代码异常的分析和把控
try:
    # a = 1
    print(a)
    print('没有出现异常')
except:
    print('出现异常了')