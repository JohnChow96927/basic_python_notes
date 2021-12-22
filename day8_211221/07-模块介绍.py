# 模块就是一个Python文件,这个文件中的函数,类,对象,全局变量等可以导入其他问价内进行使用,增强代码的复用性

# 但是不是所有的pyhton文件都可以作为模块进行导入
# 可以使用import关键字将模块进行导入,但是不能使用非标识符命名的Python文件
# 如果想要作为模块使用,文件命名时必须尊徐表示符的命名规范

# 注意:
# 1.文件命名时不能与系统模块重名
# 2.见名知意
# 3.遵循标识符的命名规则:
#   不能以数字开头,只能由数字字母下划线组成,不能使用关键字,严格区分大小写
# 4.尽量不要出现中文


import my_moudle01

print(my_moudle01.age)

import random
# AttributeError: module 'random' has no attribute 'randint'
# 如果我们自己定义的模块与系统模块重名,会覆盖系统模块,无法使用其功能
# print(random.randint(1, 2))

# import 传智有你会更好