# 前置知识: 引用地址  id
# id 相同的数据,一定是同一个数据,因为引用地址相同,指向的内容空间就相同

# 判断一个数据是否相等有几个纬度???  数据类型  数据的值  引用地址(唯一标识)

# 数据类型相同不一定是同一个数据? 不一定

# 数据的值相同一定是同一个数据么? 不一定
# False  0
# == 判断的是值相等
print(False == 0)  # True

# 数据类型相同,数据的值也相同 一定是同一数据么?  不一定
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(type(list1) == type(list2))  # True
print(list1 == list2)  # True
# 引用地址相同一定是同一数据么??  一定
print(id(list1) == id(list2))  # False

# 在数据传递过程中,我们怎么判断传递的数据就是原来的数据

a = list1
b = a

print(id(a) == id(b))  # True
# 判断两个变量中的数据是否为同一数据还可以使用is判断

print(a is b)  # True

# 如果想要判断两个数据为同一数据,或者指向同一内存空间则需要判断其id值是否相同

# 引用:变量中保存数据时,保存的是数据的引用地址,相当于一个箭头,指向了某个内存空间,调用变量时其实调用的是内存空间中的数据

# 引用其实就是通过引用地址,建立变量和数据之间关系的一个过程

a = 1  # 此时可以称之为a变量引用了1这个数据
b = 1

print(a is b)  # True

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a is b)  # False

# 思考:

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# list1 = list2
# list2.append(6)
# list1.remove(3)
# print(list1)
# print(list2)


# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list1.append(4)
# list2.append(5)
# list2 = list1
# print(list1)
# print(list2)

# 当使用变量进行赋值的时候,其实传递的是引用地址

str1 = '12345'
str2 = '1234'
str1.replace('12', '21')
str2.split()
str1 = str2
print(str1)
print(str2)

# 可变数据类型: 数据存储空间中的数据可以被修改,叫做可变数据类型.(列表, 字典, 集合)
# 不可变数据类型:数据存储空间中的数据不可以被修改的叫做不可变数据类型.(字符串, 元组, 整型, 浮点型, 布尔值)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 is list2)  # False

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 is tuple2)  # True

str1 = '123'
str2 = '123'

print(str1 is str2)  # True

# 在Python中能够修改一个数据引用地址的方式只有赋值 =
