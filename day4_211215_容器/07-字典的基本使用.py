# 字典的定义
# 格式: 变量 = {key1:value1, key2:value2.....}
stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# 在开发中,键相当于维度,值相当于数据值

# 字典存在的意义就是便于程序员快速的存取数据,所以要做到键要见名知意

# stu_dict1 = {'xiaoming':18, '男':'123'}
# 这样写就不方便存取数据了, 所以如果这样写还不如用列表

# 空的字典定义  {}
dict_temp = {}

print(dict_temp)  # {}
print(type(dict_temp))  # <class 'dict'>

# 提取字典中的指定元素
# 在字典中一定要通过key取值,如果有一天你需要使用值去校验键,那么证明你的数据存储出现了问题
# 格式: 字典[key] = value
print(stu_dict['name']) # xiaoming

# 注意事项:
# 1.字典中的键,是不能重复的,如果重复的话后赋值会覆盖先赋的值
stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男', 'name':'小红', 'id':18}
print(stu_dict)

# 2.取值时,如果key不存在,会报错
# KeyError: 'height'  证明在字典中没有height这个键
print(stu_dict['height'])

# 3.字典中的键值对只能成对出现,不能单独出现键或者值
# stu_dict = {'name': 'xiaoming', 'age': 18, 'gender':}
# print(stu_dict)




