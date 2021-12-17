# 字典的删除操作都有哪些呢??

stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# clear() 清空字典,将字典重置为{}

# stu_dict.clear()
# print(stu_dict) # {}

# pop() 删除字典中指定key所对应的键值对
print(stu_dict.pop('name'))
# print(stu_dict)
# TypeError: pop expected at least 1 argument, got 0
# 在字典中,pop不能什么也不填写
# stu_dict.pop()
# print(stu_dict)

# 如果删除的key 不存在将会报错
# KeyError: 'address'
# stu_dict.pop('address')
# print(stu_dict)

# popitem 删除键值对
# 官方文档上写的是随机删除一个键值对,但是经过反复测试只能删除最后一个

stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

stu_dict.popitem()
print(stu_dict.popitem())

print(stu_dict)
