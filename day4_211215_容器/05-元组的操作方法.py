# 元组不支持修改数据内容,所以在元组中不能执行增,删改的操作,只能进行查询,此时我们可以仿照list的查询方法学习元组

tuple1 = (1, 2, 4, 5, 4, 3)
# TypeError: 'tuple' object does not support item assignment
# 元组不能执行修改方法
# tuple1[3] = 4

# 元组可以使用索引值获取元素
print(tuple1[3])  # 5

# IndexError: tuple index out of range
# 如果获取的索引值不存在,则会报错
# print(tuple1[7])

# index和list 中的index 使用方法完全相同
# index 可以查询元组中,从左至右出现的第一个指定元素的正数下标值,
print(tuple1.index(4))
# 如果查询的数据不存在,则报错
# ValueError: tuple.index(x): x not in tuple
# print(tuple1.index(8))

# count 计数,获取指定元素在元组中出现的次数
print(tuple1.count(4))  # 2
print(tuple1.count(1))  # 1

# in  not in
print(1 in tuple1) # True
print(8 in tuple1) # False
