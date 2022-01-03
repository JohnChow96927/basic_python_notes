# 当模块中没有__all__变量时,所有的功能都可以被导入
# 当__all__存在时, from 模块名 import *  只能导入__all__这个列表内添加的功能
# __all__ 写在什么位置都可以,但是习惯性写在模块开始位置

# AttributeError: module 'my_moudle03' has no attribute 'abc'
# 如果在__all__中添加了该模块中不存在的功能,在导包时将会报错

from my_moudle03 import *

func1()

# func2()

print(age)

# 如果不在__all__中,可以使用全部导入形式进行导入么? 可以
import my_moudle03
my_moudle03.func2()

# 如果不在__all__中,可以使用局部导入的形式进行导入么? 可以

from my_moudle03 import func2
func2()

# 结论:
# __all__ 只约束了from 模块名 import * 这种导入方式