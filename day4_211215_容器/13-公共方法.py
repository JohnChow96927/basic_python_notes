# len 获取容器的长度,或者说获取容器中元素的个数

str1 = '12345'
print(len(str1))

list1 = [1, 2, 3, 4]
print(len(list1))

# 字典中获取容器长度,得到的是键值对的个数
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(len(dict1))

# del  删除操作
# del的原理就是切断引用关系
del list1[1]

print(list1)

# del方法可以删除列表,字典中的相关数据
# 删除字典时,是删除键值对
del dict1['a']
print(dict1)

# 能不能删除字符串,元组,集合内的数据??
# 字符串和元组中的元素是不可修改的所以不能删除
# TypeError: 'tuple' object doesn't support item deletion
# tuple1 = (1, 2, 3, 4)
# del tuple1[2]
# TypeError: 'str' object doesn't support item deletion
# str1 = '1234'
# del str1[2]

# 集合内的数据无法单独获取只能遍历,所以无法删除
# del只能对字典和列表生效


# max  min
list1 = [1, 2, 3, 6, 4, 5]
print(max(list1))

str1 = '15432'
print(min(str1))

set1 = {1, 2, 5, 4, 3}
print(max(set1))

# 对于字典获取最大最小值时,获取的是最大或最小的键
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(min(dict1))  # a
