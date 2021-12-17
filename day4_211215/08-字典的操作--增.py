# 字典的增加操作有哪些呢?
stu_dict = {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# 使用字典的key 增加键值对
# 如果使用的key 不存在,则系统会自动增加一个新的键值对
# stu_dict['id'] = 18
# stu_dict['height'] = 1.75

# print(stu_dict)

# update
# 使用updata 可以更新字典,如果更新的键值对,不存在,则新增
stu_dict.update(id=18, address='上海')
stu_dict.update({'height': 1.75, 'weight': 75})
print(stu_dict)