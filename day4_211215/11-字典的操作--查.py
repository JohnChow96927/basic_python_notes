# 查询一个字典的键所对应的值
# 使用索引
stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

print(stu_dict['name'])
# KeyError: 'id'
# 如果查询的键不存在则报错
# print(stu_dict['id'])

# 使用get进行查询
print(stu_dict.get('name'))
# 如果查询的键不存在则默认返回None
print(stu_dict.get('id'))  # None
# 如果给get一个设置一个不存在键时的返回值,则查询的键不存在会返回指定数据内容
print(stu_dict.get('id', '查询的键不存在'))  # 查询的键不存在
# 如果查询的键存在,则会返回指定的value
print(stu_dict.get('age', '查询的键不存在'))  # 18

# dict_values(['xiaoming', 18, '男'])
# values是查询字典中所有的值的方法
print(stu_dict.values())

# dict_keys(['name', 'age', 'gender'])
# keys是查询字典中所有的键的方法
print(stu_dict.keys())

# dict_items([('name', 'xiaoming'), ('age', 18), ('gender', '男')])
# items是查询字典中所有的键值对的方法
print(stu_dict.items())

# 遍历字典
# 遍历字典时,默认是将字典的键依次赋值给临时变量i
'''
name
age
gender
'''
for i in stu_dict:
    print(i)

# 可以遍历字典中所有的值
for value in stu_dict.values():
    print(value)

# 一次性遍历字典的键和值
for key, value in stu_dict.items():
    print(f'key为{key}, value为{value}')

# 练习:
# 有一个字典 其中有三个键值对  姓名(name):   年龄(age):   性别(gender):
# 1.给字典中添加一个学号键值对
# 2.将自己的年龄改为18岁
# 3.删除年龄键值对
# 4.遍历字典获取其中的键和值

person_dict = {'name': '小黄', 'age': 25, 'gender': '男'}
person_dict['id'] = 10
person_dict['age'] = 18
person_dict.pop('age')
for key, value in person_dict.items():
    print(key, value)


print(person_dict)
