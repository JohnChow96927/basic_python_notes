# 如果我们想自定义模块,那么模块名要遵循标识符命名规则
# 并且只有类, 全局变量,函数定义等可以导入其他文件

# 导入模块时,会将模块中所有的代码全部执行一遍,此时,全局变量,函数等,会保存到内存中,等待使用
# import my_moudle02

# my_moudle02.func()
#
# print(my_moudle02.age)

# from my_moudle02 import func
#
# func()

