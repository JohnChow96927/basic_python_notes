# 全局变量
# list1 = [1, 2, 3]
#
#
# def func1():
#     # 我们此处并没有修改list1 的引用地址,而是使用了其引用地址,并不需要使用global进行声明
#     # 当对全局变量使用等号赋值时,才需要使用global进行声明
#     # list1 = [1, 2, 3, 4]
#     list1.append(5)
#
#
# func1()
#
# print(list1)


list1 = [1, 2, 3, 4]


# def func1(num_list):
#     num_list.append(5)
#     num_list.append(8)
#
#
# func1(list1)
#
# print(list1)


def func2(num_list):
    num_list = [1, 2, 3, 5]
    num_list.append(6)
    num_list.append(8)


func2(list1)
print(list1)

# 练习: 有一个字典中有姓名和年龄两个键值对
# 创建一个函数,将该字典传入,在函数内增加性别和id键值对,修改完成后在外部打印字典,查看修改效果

dict1 = {'name': 'xiaoming', 'age': 18}


def func3(stu_info):
    stu_info['gender'] = '男'
    stu_info['id'] = 16


func3(dict1)

print(dict1)
