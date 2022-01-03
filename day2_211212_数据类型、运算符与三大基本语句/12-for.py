# 在Python 中有两种循环,一种是for循环一种是while循环
# for循环一般配合容器类型进行使用
'''
for循环格式:

for 临时变量 in 容器类型(可迭代类型):
    循环体

for循环中没有循环条件,依次从容器类型中取值,直到所有的值取完,循环自动终止
'''

str1 = 'itcast'
for i in str1:
    print(i)


# 没有循环变量,所以不用考虑自增问题,书写过程中不容易出现bug

# range 范围类型,内部是多个整型数据组成的数据集合
# range 是一个左闭右开的区间,包含0, 不包含5
for i in range(0, 5):
    print(i)


# while循环打印0-4
i = 0
while i < 5:
    print(i)
    i += 1