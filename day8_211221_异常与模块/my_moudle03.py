'''
模块说明
'''

import os

__all__ = ['age', 'func1']


age = 18


def func1():
    print('我是一个孤独的函数')


def func2():
    print('我是一个有个性的函数')

# 如果我们不希望在导入模块时执行输出 ,循环 判断等测试代码我们可以将代码写到if __name__ == '__main__'中
# 在当前模块中运行时,测试代码执行
# 导入模块时,测试代码不执行
print(__name__) # __main__ 主程序入口,说明当前进程是从这个文件启动的
# 当把其当做模块导入其他文件时,会打印当前模块的模块名称  my_moudle03

if __name__ == '__main__':
    # 如果从当前文件启动,则执行该代代码
    # 如果导入到其他文件,则不执行该代码
    print('我已经被执行了')
    func1()
