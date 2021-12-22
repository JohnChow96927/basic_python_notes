# 模块导入和使用
# 方式一: import (全部导入) 模块名
# import random
# 调用 : 模块名.功能名
# 全部导入下,模块中所的功能都可以被使用
# print(random.randint(1, 2))
# print(random.randrange(1, 2))

# 方式二: from 模块名  import 功能名
# from random import randint

# 调用: 功能名
# 这种方式又叫做局部导入,并且只能使用被导入的功能
# print(randint(1, 2))

# 方式三: from 模块名 import *

# from random import *
# # 调用: 功能名
# # 这种方式也是局部导入,但是一次性导入了多个功能,* 是通配符,表示所有可以被导入的功能
# # __all__可以限制导入的内容(后边会讲)
# print(randint(1, 2))
# print(randrange(1, 9))


# 方法四: 给模块起别名
# import random as suiji

# NameError: name 'random' is not defined
# 如果给模块起了别名,则只能使用别名,不能使用原名称
# print(random.randint(1, 2))
# print(suiji.randint(1, 2))


# 方法五: 给功能起别名
from random import randint as rint

# NameError: name 'randint' is not defined
# 如果给功能起了别名,则原功能名称无法继续使用,会报错
# print(randint(1,3))
print(rint(1, 3))
