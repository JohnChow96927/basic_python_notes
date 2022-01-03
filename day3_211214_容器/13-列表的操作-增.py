# append 在列表的末尾追加一个元素

list1 = [1, 2, 3, 4]
# 需求: 要在列表中追加一个元素5
print(list1.append(5))  # None(空)
# 当我们给列表追加数据时,没有产生新的列表,而是在原有列表的基础上进行了修改
print(list1)  # [1, 2, 3, 4, 5]

# str1 = '1234'
# # 当使用各种方法修改字符串中的数据时,产生了新的字符串,原字符串并没有被修改
# print(str1.replace('4', '5'))
# print(str1)

# insert 在指定位置追加一个元素
# insert(self(不用传值), index(插入的索引值), object(被插入的值))
name_list = ['小明', '小黄', '旺财', '小绿']

print(name_list[3])  # 小绿
# 需求: 在小明后边插入一个小丽
name_list.insert(1, '小丽')
print(name_list)  # ['小明', '小丽', '小黄', '旺财', '小绿']

print(name_list[3])  # 旺财

# 结论: insert可能会改变原有元素的下标值.所以append插入数据比insert更安全,开发中使用场景更多


# extend 在容器后边拼接一个新的容器

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 需求:在list1,后边拼接list2, 构造一个列表[1,2,3,4,5,6]
# list1.extend(list2)
# TypeError: 'int' object is not iterable
# extend中只能添加可迭代类型数据
list1.extend(3)

# 调用extend方法的列表进行了拼接操作,括号内的列表没有发生变化, 而是复制了一份,对list1进行了拼接
print(list1)  # [1, 2, 3, 4, 5, 6]
print(list2)  # [4, 5, 6]

# extend 和 append 有什么区别
# extend 会遍历括号中的容器中每一个元素,追加到列表末尾
# append 会将容器看做一个元素追加到列表末尾
list1.append(list2)

print(list1)  # [1, 2, 3, [4, 5, 6]]
print(list2)  # [4, 5, 6]