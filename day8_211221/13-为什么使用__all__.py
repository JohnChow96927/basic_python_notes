# __all__ 可以约束from import *
# 因为from import  * 不可以给功能名称起别名

# from my_moudle03 import age as age03
# from my_moudle02 import age as age02
#
# # 如果存在同名功能,谁后导入,我们就使用谁的功能
# # print(age)
# # 怎么解决同名问题??? 给功能起别名
# print(age02)
# print(age03)

from my_moudle02 import *
from my_moudle03 import *
import pyecharts
# from import * 这种形式导入数据,我们不确定他是否存在同名方法, 所以会使用__all__控制我们要导入的功能
# 一般情况下除了自己写的模块或者非常熟悉的模块不会使用from 模块 import *,防止和其他模块中的功能重名
# 如果非要用一般也会手动修改__all__

# 有些时候,三方包或者库中,一个模块几百个方法,但是真正需要暴露给程序员你的方法就几个,我们把他写到__all__中就可以了

print(age)
