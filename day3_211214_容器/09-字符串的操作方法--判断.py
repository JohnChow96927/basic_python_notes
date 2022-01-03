# 在字符串中可以存放各种数据,比如123,  abc  或者❤,那么怎么判断字符串中是什么呢?

# 字符串的判断
str1 = '123'
str1.isspace()  # 是否都为空白
str1.isupper()  # 是否都为大写
str1.islower()  # 是否都为小写
str1.isidentifier()  # 是否都为标识符
str1.isalnum()  # 是否都为数字或字母
str1.isnumeric()  # 是否都为数字
str1.isdecimal()  # 是否都为数字
str1.isdigit()  # 是否都为数字
str1.isalpha()  # 是否都为字母

str2 = 'name_error'
print(str2.isidentifier(),'标识符')

str3 = '123四⑤'
str4 = '12.1' # 只要有点,就不是纯数字
print(str3.isnumeric())  # True
print(str3.isdecimal())  # False
print(str3.isdigit())  # False
print(str4.isnumeric())  # False


str5 = 'abc123传智'
print(str5.isalnum()) # True
# 了解.
print(str5.encode('utf8').isalnum()) # False

str6 = 'hello python'
# startswith判断是否以...开头
print(str6.startswith('o')) # False
# endswith判断是否以...结尾
print(str6.endswith('n')) # True
