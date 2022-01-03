# 方法五: from 包名 import *

# 涉及到init文件中的__all__
# 只有在__init__.py文件中书写的__all__变量中添加的模块名称才能正常导入
# 如果不书写__all__所有的模块均不能导入
from demo import *

print(my_moudle03.age)
my_moudle03.func1()

my_moudle02.func()
