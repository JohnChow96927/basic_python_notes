# 标识符:程序员自己定义的有特殊功能或者含义的字符组合就是标识符.
# 关键字:系统或者说Python定义的的有特殊功能或者含义的字符组合就是关键字.
# 标识符的命名规则:  不遵循就报错的就是命名规则

# 1.只能由数字,字母,下划线组成.
# abc% = 123
# abc_ = 123
# ___ = 123

# 2.首字母不能是数字
# 1abc = 123
# a111 = 123

# 3.不能使用关键字
# for = 123
# True = 123

# 4.严格区分大小写
true = 123
a = 1
A = 2
print(a)

# 标识符的命名规范:  根据程序员的职业操守进行遵守,不遵守代码也能运行
# 1.见名知意
name = 'jack'
mz = 'jack'
# 2.非知名缩写,不使用

# 3.尽量定义变量时不使用数字编号
# name1 =  name2 = name3 =

# 4.不使用系统内置函数名
# print = 1
# # TypeError: 'int' object is not callable
# print('数字')

# 5.一般在Python中变量名,函数名,方法名等使用下划线分隔法, 类名使用大驼峰命名法

# 小驼峰命名法
# 命名时,多个单词,首字母小写,其余单词首字母大写
className = 'Python+大数据40期'
studentFirstName = 'zhang'

# 大驼峰命名法
# 命名时,所有单词,首字母大写
ClassName = 'Python+大数据40期'
StudentFirstName = 'zhang'

# 下划线分隔法
class_name = 'Python+大数据40期'
student_first_name = 'liu'










