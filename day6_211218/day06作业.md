### 题目1

有变量 a = 10 和 b = 20 ，请使用至少两种方法交换两个变量的值。

  ##### 训练提示

  思路1：借助第三变量存储数据，定义一个中间变量temp

  思路2：预习明天课程，学习新的python语法

  ##### 参考答案

  ```python
# 方法一
a = 10
b = 20
temp = a
a = b
b = temp
# 方法二
a = 10
b = 20
a, b = b, a
  ```



### 题目2

分别定义一个字符串类型的全局变量、列表类型的全局变量。定义函数func2，在函数中分别添加global关键字修改，和不添加global关键字修改，总结有什么区别。



##### 训练提示

本题为总结性题目，按照题目要求熟悉些代码，观察他们的不同之处



##### 参考答案

```python
  用global关键字修饰后可以对全局变量进行修改，否则无法修改
```

### 题目3

完成一个函数，给定三个值。判断你给的值是否可以组成一个三角形


##### 训练提示

​	三角形成立必须两边之和大于第三边

​	第一步：定义函数，并接受三个参数

​	第二步：任意相加其中的两条边判断是否大于第三边，要保证三条边中任意两边之和都大于第三边

##### 参考答案

```python
def triangle_or_not(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    return True
  else:
    return False
```

### 题目4

定义函数find_all_pos，实现找出列表中某个元素所有位置的起始下标，要求返回符合要求的所有位置的起始下标，如`[3, 6, 1, 4, 1, 5, 6, 1, 3, 6, 2]`，需要找出里面所有的`1`的位置，最后将返回一个元组`(2, 4, 7)`

##### 训练提示

思路：通过循环遍历每个元素，如果这个元素为查找的元素，把对应的下标追加到一个新列表，最后，把新列表转换为元组返回

##### 参考答案

```python
def find_all_pos(a: list, b):
    result = []
    for i in range(len(a)):
        if a[i] == b:
            result.append(i)
    return tuple(result)
```

### 题目5

斐波那契数列：1，1，2，3，5，8... 即前两个数字是1, 从第三个数字开始，每个数字是前两个数字之和，编写函数，输出n个数的斐波那契数列

##### 训练提示

思路：本题主要找出斐波那契数列的规律，从第三个数字开始，每个数字是前两个数字的和，用代码完成这个规律的循环

考查知识点：交换两个变量的值

##### 参考答案

``` python
def fibonacci(n: int):
    result = [1, 1]
    if n == 1 or n == 2:
        print(n * [1])
    else:
        for i in range(2, n):
            result.append(result[i - 2] + result[i - 1])
        print(result)
```

### 题目6

完成学生管理系统的基本搭建

基本功能包括 1、添加学生  

​						2、修改学生信息

​						3、删除学生

​						4、查询学生

​						5、显示所有学生

​						6、退出

##### 训练提示

​		学生管理系统的基本骨架要求实现打印菜单功能，提示用户输入对应数字，完成对应操作的功能

​		第一步： 菜单功能是提示用户此系统有哪些可选操作（可通过print 打印来提示用户）

​		第二步：接收用户的输入

​		第三步： 根据用户的输入，判断用户选择的是什么功能，打印即将要执行的功能



##### 参考答案

```python
stu_info = []


def print_info():
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def add_info():
    """ 添加学员 """
    # 接收用户输入学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 声明stu_info是全局变量
    global stu_info

    # 检测用户输入的姓名是否存在，存在则报错提示
    for i in stu_info:
        if new_id == i['id']:
            print('该用户已经存在！')
            return

    # 如果用户输入的id不存在，则添加该学员信息
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}

    # 将这个学员的字典数据追加到列表
    stu_info.append(info_dict)

    print(stu_info)


def del_info():
    """删除学员"""
    # 1. 用户输入要删除的学员的姓名
    del_id = input('请输入要删除的学员的id：')

    global stu_info
    # 2. 判断学员是否存在:如果输入的姓名存在则删除，否则报错提示
    for i in stu_info:
        if del_id == i['id']:
            stu_info.remove(i)
            break
    else:
        print('该学员不存在')

    print(stu_info)


# 修改函数
def modify_info():
    """修改函数"""
    # 1. 用户输入要修改的学员的姓名
    modify_id = input('请输入要修改手机号的学员的id：')

    global stu_info
    # 2. 判断学员是否存在：如果输入的姓名存在则修改手机号，否则报错提示
    for i in stu_info:
        if modify_id == i['id']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

    print(stu_info)


# 查询学员
def search_info():
    """查询学员"""
    # 1. 输入要查找的学员姓名：
    search_id = input('请输入要查找的学员id：')

    global stu_info
    # 2. 判断学员是否存在：如果输入的姓名存在则显示这位学员信息，否则报错提示
    for i in stu_info:
        if search_id == i['id']:
            print('查找到的学员信息如下：----------')
            print(f"该学员的学号是{i['id']}, 姓名是{i['name']}, 手机号是{i['tel']}")
            break
    else:
        print('该学员不存在')


def print_all():
    """ 显示所有学员信息 """
    print('学号\t姓名\t手机号')
    for i in stu_info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')


while True:
    print_info()
    user_num = input('请选择您需要的功能序号：')
    if user_num == '1':
        add_info()
    elif user_num == '2':
        del_info()
    elif user_num == '3':
        modify_info()
    elif user_num == '4':
        search_info()
    elif user_num == '5':
        print_all()
    elif user_num == '6':
        exit_flag = input('确定要退出吗？yes or no：')
        if exit_flag == 'yes':
            break
    else:
        print('您输入的信息有误！请重新输入：')
    # # 添加阻塞函数查看输出效果
    # input()
```

