# + 容器的拼接操作
str1 = '123'
str2 = '456'
# 字符串之间可以相加,但是相加后会产生一个新的字符串,原字符串不发生变化
print(str1 + str2)
print(str1)
print(str2)

list1 = [1, 2, 3]
list2 = [3, 4, 5]
# 列表之间可以相加,但是相加后悔产生一个新的列表,原列表不发生变化
print(list1 + list2)
print(list2)
print(list1)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# 元组之间可以相加,但是相加后会产生一个新的元组,原元组不发生变化
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)
print(tuple1)
print(tuple2)

set1 = {1, 2, 3}
set2 = {4, 5, 6}
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# 集合之间不能相加
# print(set1 + set2)

dict1 = {'a': 1}
dict2 = {'b': 2}
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# 字典之间不能相加
# print(dict1 + dict2)

# * 复制并拼接
# 其实*法运算和+法运算的底层逻辑相同 只不过一个是两个数据相加,一个是同一个数据加了指定次数
# 可以进行加法运算的数据类型都可以进行乘法运算,不能进行加法运算的也不能进行乘法运算
list1 = [1, 2, 3]
print(list1 * 3)

# in not in
# in或者not in可以使用在dict  set  tuple str  list 中
# 要注意,在dict 中使用in 或者not in 是判断元素知否在字典的键中存在

person_dict = {'name': '小黄', 'age': 25, 'gender': '男'}
print('小黄' in person_dict)  # False
print('name' in person_dict)  # True

# 判断元素是否在容器内,该容器一定要可以储存当前数据类型
# TypeError: 'in <string>' requires string as left operand, not int
# print(1 in '123')

# TypeError: unhashable type: 'set'
# 集合类型不能作为字典的键出现
# 扩展: 字典的键只能是元组,字符串,数字,bool等,不能是集合,列表,字典
# 同时不能作为字典键存在的数据类型,也不能储存到集合当中
# TypeError: unhashable type: 'list'
# set1 = {[1,2,3]}
# print({1, 2} in person_dict)
