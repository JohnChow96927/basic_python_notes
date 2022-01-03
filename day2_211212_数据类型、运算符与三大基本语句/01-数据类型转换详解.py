# 如果想要让数据类型进行转换,那么我们需要给数据穿衣服,但是穿衣服也要遵循规则

# 定义变量
int1 = 10

float1 = 12.999999999

str1 = '10'
str2 = '12.1'
str3 = 'hello'

# int <<>> float
# 将整型转换为float类型,则在整数末尾加.0
print(float(int1))  # 10.0
print(type(float(int1)))  # <class 'float'>
# 将浮点型转换为整型数据,则将浮点型的小数部分全部删除,只保留整数部分
print(int(float1))  # 12
print(type(int(float1)))  # <class 'int'>

# int <<>> str
# 将字符串数据类型转换为整型,如果字符串内是整型数据,则转换成功
print(int(str1))  # 10
# 将字符串数据转换为整型,如果字符串内是浮点型,则转换失败,报错.
# ValueError: invalid literal for int() with base 10: '12.1'
# print(int(str2))
# 将字符串数据转换为整型,如果字符串内是字符组合,则转换失败,报错.
# ValueError: invalid literal for int() with base 10: 'hello'
# print(int(str3))

# 将int转换为str类型没有限制,可以随意转换
# print(str(123))

# float <<>> str
# 将字符串转换为浮点型数据,如果字符串内是整型,则转换成功,但是需要在整型数据末尾添加.0
print(float(str1))  # 10.0
# 将字符串转换为浮点型数据,如果字符串内是浮点型,则转换成功
print(float(str2))  # 12.1
# 将字符串转换为浮点型数据,如果字符串内是字符组合,则转换失败,报错.
# ValueError: could not convert string to float: 'hello'
# print(float(str3))

# 将float转换为str类型没有限制,可以随意转换
print(str(12.1))  # 12.1


# 结论:任何数据类型都可以转换为str类型.