# 推导式的作用是可以快速的生成一个数据容器

# 需求:创建一个列表,列表内是1-100中所有的整数

list1 = []
for i in range(1, 101):
    list1.append(i)

print(list1)

# 使用推导式完成
list2 = [i for i in range(1, 101)]

print(list2)

# 需求: 创建一个列表,列表内是1-100的偶数
list3 = []
for i in range(1, 101):
    if i % 2 == 0:
        list3.append(i)

print(list3)

# 使用推导式完成
list4 = [i for i in range(1, 101) if i % 2 == 0]
print(list4)

# 需求: 创建一个列表,列表内部是1-100的正数,但是不能是2 3 5 7 的倍数
list5 = []
for i in range(1, 101):
    if i % 2 != 0:
        if i % 3 != 0:
            if i % 5 != 0:
                if i % 7 != 0:
                    list5.append(i)

print(list5)

# 使用推导式完成
list6 = [i for i in range(1, 101) if i % 2 != 0 if i % 3 != 0 if i % 5 != 0 if i % 7 != 0]

print(list6)

# 练习:
# 需求:创建一个列表,列表内部是1-100的正数,但是不能存在7 或7的倍数,数字中也不能含有7

list7 = []
for i in range(1, 101):
    if i % 7 != 0:
        if '7' not in str(i):
            list7.append(i)

print(list7)

# 使用推导式完成
list8 = [i for i in range(1, 101) if i % 7 != 0 if '7' not in str(i)]

print(list8)

# 除了列表推导式  还有集合 和字典推导式
# 获取1-10中所有偶数的平方放入集合中
set1 = {i ** 2 for i in range(1, 10) if i % 2 == 0}

print(set1)
# set集合要注意无序不重复的特性,所set推导式其实在开发中很少使用


# 字典推导式

key_list = ['name', 'age', 'gender']

value_list = ['xiaoming', 18, '男']

# 两个列表合并为一个字典
dict1 = {key_list[i]: value_list[i] for i in range(len(key_list))}

print(dict1)

# 需求: 变量1-10 的数字,创建一个字典,键为1-10的值,值为其平方
dict2 = {i: i ** 2 for i in range(1, 11)}

print(dict2)

# 注意没有元组推导式

