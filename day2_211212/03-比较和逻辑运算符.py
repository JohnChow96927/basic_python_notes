# 比较运算符
# 大小的比较  >  <   >= <= != ==
# 比较运算符的运算结果是布尔类型数据,如果不等式成立,则返回True,如果不等式不成立,则返回False
# 判断是否相等使用的是== ,一个等号是赋值运算符,一定要区分开.
print(1 == 2)  # False
print(3 > 2)  # True
print(2 >= 2)  # True
# 一般不会使用纯数字进行比较运算,会使用变量进行比较运算
age = 18

print(age > 12)  # True

# 字符串类型的大小比较规则
# 字符串类型数据比较大小,按照ascii码的排序进行大小比对
# 数字一定小于字母, 大写字母一定小于小写字母
# 字符串进行大小比较,会从第一位字符开始比较,如果第一位大,则不会比对后边的字符,如果第一位相同会向下继续比较
# 如果前一位相同,比较后边的字符时,有字符比没有字符大
print('1' > '2')  # False  '2'大
print('12' > '9')  # False '9'大
print('a' > '4356')  # True 'a' 大
print('A' > 'a')  # False 'a' 大
print('910' > '91')

# 逻辑运算符??  与  或  非
# and  逻辑与  and左右两侧均为真,则为真,如果一侧为假即为假
print(True and False)  # False
print(True and True)  # True
print(False and False)  # False

# or  逻辑或 or 左右两侧都为假即为假,如果一侧为真,即为真
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False

# not  逻辑非  非真即假,非假即真
print(not False)  # True
print(not True)  # False

# and  同真即真
# or  同假即假
# not  真变假, 假变真

# 在正常使用时,我们不会使用逻辑运算符判断布尔值,而是使用比较运算,结合逻辑运算使用
age = 18

# 判断该学员是否大于15岁,并且小于32岁
print(age > 15 and age < 32)
# 了解: 我们再Python中比较运算符可以连续使用
print(15 < age < 32)

























