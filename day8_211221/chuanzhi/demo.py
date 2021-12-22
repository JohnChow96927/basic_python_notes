
import sys

# print(sys.path)

'''
['/Users/jizhengguo/Desktop/上海Python+大数据基础40期/day08/03-代码/chuanzhi', 
'/Users/jizhengguo/Desktop/上海Python+大数据基础40期/day08/03-代码',
'''
# 导入工程目录中的my_moudle 模块直接使用模块名即可
# import my_moudle01
#
# print(my_moudle01.age)
#
# from my_moudle03 import func2
#
# func2()

# 导入demo包中的my_module01
# import demo.my_moudle01

# import ../demo.my_moudle01

# 导入itheima文件夹中的my_module01
import itheima.my_moudle01

from itheima.my_moudle01 import age

print(age)

# 结论:
# 如果在导入模块时,不知道该怎么导,从工程目录中进行导入,一层一层进行导入

# 如果我们直接导入当前目录下的模块,且当前目录不是工程目录,pycharm错误检测就会认为你的导入方式不对,但是其实可以找到指定模块

# 有两种方法可以解决该问题:
# 1.从工程目录开始导入
# 2.让当前目录也变成资源路径: 在需要更改的文件夹上右键>>mark dir as >> source root

# import module01
# module01.func2()

# Python官方建议所有的导包路径从工程目录开始,尽量不要使用其他的或者指定某个文件为导包路径