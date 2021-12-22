# 方法一: import 包名.模块名
# import demo.my_moudle03

# 使用: 包名.模块名.功能名
# demo.my_moudle03.func2()

# 方式二: from 包名  import 模块名 这种形式也属于全部导入
# from demo import my_moudle03

# 使用: 模块名.功能名
# my_moudle03.func2()

# 方法三: from 包名.模块名 import 功能名
# from demo.my_moudle03 import func2

# 使用: 功能名
# func2()

# 方法四: from 包名.模块名  import *
# 这种方法也会受 __all__ 影响
# from demo.my_moudle03 import *

# 使用 功能名
# func1()
# print(age)

# 方法五: from 包名 import *

# 稍后再讲  涉及到init文件中的__all__
# from demo import *

# 方法六: import 包名
import demo
