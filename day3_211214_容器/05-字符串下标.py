# 字符串下标: 在数据存储或提取时,通过下标,来确定字符串中的每一个元素
# 字符串中的下标是从0开始,从左至右依次递增的

str1 = 'itcast'
'''
i  t  c  a  s  t
0  1  2  3  4  5
'''

print(str1[2]) # c
print(str1[4]) # s

# 字符串中还有负数下标: 从-1开始从右至左依次递减

'''
i   t  c  a  s  t
-6 -5 -4 -3 -2 -1
'''

print(str1[-3]) # a
print(str1[-6]) # i


str2 = '我爱北京天安门'

print(str2[3])
print(str2[-4])