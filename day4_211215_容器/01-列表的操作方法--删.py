# 列表中的删除方法
list1 = [1, 2, 3, 4]
# list1.clear()
# clear() 清空列表:将列表中的所有元素移除,使列表变为一个空列表
# clear没有产生新的容器,而是在原容器上进行了修改
print(list1.clear())  # None
print(list1)  # []

# list1.remove()
# remove()  移除指定值的元素,但是remove只能删除从左至右遇到的第一个该值元素
list2 = [1, 2, 3, 3, 2, 1, 1, 1, 1]
# list2.remove(2)
# print(list2)

# list1.pop()
# pop() 根据索引值,移除指定元素
# 使用pop可以将被删除的运算返回,使用变量接收在之后在做使用
# 如果pop 后边什么也不加,则默认删除最后一个元素
# list1.pop(2)
print(list2.pop(2))
# 删除后,会在原容器中删除指定元素
print(list2)
list2.pop()
list2.pop()
list2.pop()
list2.pop()
print(list2)

# 思考题:
list3 = [1, 2, 3, 3, 3, 1, 2]
# 删除list3中所有的3
# for循环  while循环  循环逻辑一样么?
# for 依次(按照索引顺序)从容器中取值
# while 按照循环条件进行循环

# 如果使用insert可能会改变索引值
# pop  remove  会不会呢?????  也会

# for i in list3:
#     if i == 3:
#         list3.remove(3)
#
# print(list3)

# 方法一: 删除时要避免对索引进行处理
# for i in range(0, list3.count(3)):
#     list3.remove(3)
# print(list3)

# 方法二: 删除元素时,索引值不变
# i = 0
# while i < len(list3):
#     if list3[i] == 3:
#         list3.remove(3)
#         continue
#     i += 1
#
# print(list3)