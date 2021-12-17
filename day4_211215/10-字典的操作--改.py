# 字典的修改操作
stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# 用key修改value
# 使用字典[key] = value的形式可以修改指定键所对应的值
# 当key 不存在时,就是新增键值对, 当key存在的时候,就是修改已有键所对应的值
stu_dict['name'] = '小红'

print(stu_dict)

# update可以修改键值对
stu_dict.update(age=20)
# 这行代码先修改了gender的值,又新增了id:10键值对
stu_dict.update({'gender': '女', 'id': 10})
print(stu_dict)


