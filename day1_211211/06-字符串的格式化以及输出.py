# 字符串格式化
# 格式: '要格式化的字符串内容 变量占位符' % 变量

# 示例:
age = 11
age = age + 1
# 在此处动态修改变量的值,可以让输出内容发生变化
print('小朋友%d岁了' % age)

# 字符串格式化,是字符串的特性,还是print的特性??? 字符串
# print中输出的是表达式时,先计算再输出,输出时字符串已经拼接完成
# 字符串格式化后,用变量保存再输出,还没有输出时,字符串已经拼接成功,所以格式化是字符串的功能,不是print的功能
str1 = '小朋友%d岁了' % age
print(str1)

# 如果我想在一个输出语句中插入多个变量
name = 'xiaoming'
age = 18
gender = '男'
height = 1.83
# TypeError: %d format: a number is required, not str
# 使用占位符接收数据时,不同的占位符,所接受的数据类型是不同的
# %d 接收整型数据
# %f 接收浮点型数据
# %s 接收字符串数据
# TypeError: not enough arguments for format string
# 如果在一个格式化字符串中有多个变量,在%后边的变量名称要用括号括起来
print('我的名字是%s, 我的年龄是%d, 我的性别是%s, 我的身高是%f' % (name, age, gender, height))  # 我的名字是xiaoming, 我的年龄是18, 我的性别是男, 我的身高是1.830000
# TypeError: not enough arguments for format string
# 在%后边的括号内,不能少传变量,也不能多传变量,要与前边的占位符数量一致
# print('我的名字是%s, 我的年龄是%d, 我的性别是%s, 我的身高是%f' % (name, age, gender))
# TypeError: not all arguments converted during string formatting
# print('我的名字是%s, 我的年龄是%d, 我的性别是%s, 我的身高是%f' % (name, age, gender, height, height))
