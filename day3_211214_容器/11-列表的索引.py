# 列表的索引和字符串的索引基本相同
# 正数索引,从0开始,从左至右依次递增
# 负数索引,从-1开始,从右至左依次递减
list1 = [1, 2, 3, 4, 5]
'''
[1 , 2 , 3 , 4 , 5]
 0   1   2   3   4
 -5  -4  -3  -2  -1
'''

print(list1[3])  # 4
print(list1[-2])  # 4

# list 可以通过索引修改元素值
list1[4] = 6
print(list1)

# str不可以通过索引修改元素值
str1 = '12345'
# TypeError: 'str' object does not support item assignment
# str1[4] = '6'
# print(str1)
