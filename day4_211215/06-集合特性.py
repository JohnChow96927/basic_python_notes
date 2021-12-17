# 集合特性: 无序, 不重复

# 定义方法: 变量 = {1,2,4,5,6,3}

set1 = {1, 2, 3, 3, 4}

# 由于集合是不重复的,如果输入的数据重复,则会自动去重
print(set1)  # {1, 2, 3, 4}
print(type(set1))  # <class 'set'>

# 无序:在程序员眼里,自己不能控制的顺序,就是无序
set2 = {'Tom', 'Bob', 'Rose'}
print(set2)
# 不能使用索引进行操作的容器,就是无序的
# TypeError: 'set' object is not subscriptable
# print(set2[1])

# 不重复
# 可以利用集合不重复的特性进行去重

list1 = [1, 2, 3, 3, 2, 4, 5, 6, 2, 3, 4]
# 需求:对list1内部的数据进行去操作
list2 = list(set(list1))

print(list2)

# 空的set集合怎么定义??? set()
set3 = {}
print(set3)
print(type(set3))  # <class 'dict'>

set4 = set()

print(set4)  # set()
print(type(set4))  # <class 'set'>

# 操作方法:
# 自己去看

# for 循环可以遍历集合
for i in set2:
    print(i)

# 练习: 计算1-1000 1000个数字中有多少个1, 比如11  2个  19 1个   111 3个
sum = 0
for i in range(1, 1001):
    # 每次获取的数值转换为字符串类型数据,使用count计算1的个数进行累加
    sum += str(i).count('1')

print(sum)


# 简单方法
print(str(list(range(1, 1001))).count('1'))


