# 一次性导入多个模块
# import random, os
#
# # 格式: import 模块1, 模块2 .....
# print(random.randint(1, 5))
# print(os.listdir())

# 如果想给多个模块起别名
import random as suiji, os as caozuo

# 此时,原模块名已经无法使用
# print(random.randint(1, 5))
# print(os.listdir())
print(suiji.randint(1, 5))
print(caozuo.listdir())

# import random, os
# 在Python中不建议一次性导入多个模块 建议分开来写


# 一次性导入多个功能
from os import mkdir, rmdir, rename, listdir
# 可以使用from 模块名 import 功能名1, 功能名2 .....这种形式一次性导入多个功能

# 如果想给功能起别名
# 可以在每个功能后边添加as  别名
# 但是给功能起别名后,原名称就无法使用了
from os import mkdir as md, rmdir as rd, rename, listdir
