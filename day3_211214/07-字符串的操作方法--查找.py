# 查找的方法
# find : 从左至右查找第一次出现的指定元素的正数下标, 如果元素不存在则返回-1
str1 = 'chuanzhiboke'
# find(self(不用传值), 子字符串, 起始位置(包含), 终止位置(不包含))
# 起始位置和终止位置可以省略,省略后自动在整个字符串中查找
# 使用find进行查找,获取的是字符串的正数下标
print(str1.find('c'))  # 0
print(str1.find('i'))  # 7

# 如果一个字符串中有两个相同的字符怎么办??? 只能获取从左至右第一次获取的元素下标
print(str1.find('h'))  # 1

# 如果查询的子字符串在目标字符串中不存在,会怎么样? 会得到 -1
print(str1.find('y'))  # -1

# 起始位置和终止位置怎么使用??? 获取的下标是从字符串开始数还是从起始位置数??????
# 规定查询范围后,获取的元素下标是从字符串开始的位置进行计数的
print(str1.find('h', 3, -1))  # 6
# 起始位置到终止位置是一个左闭右开的区间
print(str1.find('h', 3, 6))  # -1

# index: 从左至右查找第一次出现的指定元素的正数下标, 如果元素不存在则报错
# index(self(不用传值), start(起始位置), end(终止位置))   左闭右开区间
str1 = 'chuanzhiboke'

# 需求: 获取c元素的下标
# index 在查询时获取的也是正数下标
print(str1.index('c'))  # 0
print(str1.index('k'))  # 10

# ValueError: substring not found
# 如果使用index 查询数据时,没有找到子字符串,则会报错
# print(str1.index('h', 3, 6))
# print(str1.index('h', 3, 10))  # 6

# index 也是从左至右获取第一次查询到的元素么?
print(str1.index('h'))  # 1

# rfind :从右至左查找第一次出现的指定元素的正数下标, 如果元素不存在则返回-1
print(str1.rfind('h'))  # 6

# rindex:从右至左查找第一次出现的指定元素的正数下标, 如果元素不存在则报错
print(str1.rindex('h'))  # 6

# count 查询指定子字符串在目标字符串中出现的次数
print(str1.count('h')) # 2
print(str1.count('i')) # 1

# len()获取字符串长度
# len获取的是在字符串中有多少个元素
print(len(str1)) # 12
# 等价
print(str1.__len__()) # 12