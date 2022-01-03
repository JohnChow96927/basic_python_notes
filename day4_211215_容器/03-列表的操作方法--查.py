# 列表的查询操作

# 可以通过索引值查询列表中的元素
# list1 = [1, 2, 3, 4]
# print(list1[2])  # 3


# index
# index 获取的是列表中从左至右第一次出现的指定元素的正数索引值,
hometown_list = ['上海', '北京', '南京', '郑州', '南京', '广州']
print(hometown_list.index('南京'))  # 2

# 如果查询的元素不在list当中会直接报错
# ValueError: '西安' is not in list
# print(hometown_list.index('西安'))

# find
# 列表中没有find方法,不要乱用
# AttributeError: 'list' object has no attribute 'find'
# print(hometown_list.find('上海'))

# count 计数,查询列表中有多少个指定的子元素,但是不能指定范围
print(hometown_list.count('上海'))
print(hometown_list.count('南京'))

# in  :判断元素是否在列表中
# not in: 判断元素是否不再列表中
# in 和not in 的返回值为bool类型
# 元素在前,容器再后
print('上海' in hometown_list)  # True
print('上海' not in hometown_list)  # False
# print(not ('上海' in hometown_list))  # False

# 遍历
for hometown in hometown_list:
    print(hometown)


