# 1. 复习

- ##### 函数增强代码复用率，方便后期迭代和维护

- ##### 函数参数：形参、实参：实参与形参一一对应

- ##### 函数的返回值：缺省返回None

- ##### 在函数内部调用函数

- ##### 函数的文档注释：`""" """`

- ##### 变量的作用域

  - 全局变量：global
  - 局部变量
  - nonlocal

- ##### LEGB原则：local、edge、global、built-in

- ##### 返回值进阶：return后所有代码不会执行，本质上只能返回一个数据，用逗号隔开打包成一个元组

- ##### 函数参数进阶：

  - 位置不定长参数：*args
  - 关键字不定长参数：**kwargs
  - 顺序赋值f(x)、关键字赋值f(x=1)

- ##### 参数的规范顺序：位置参数 > 位置不定长参数(*args) > 缺省参数 > 关键字不定长参数（**kwargs）

# 2. 拆包组包和数值交换

- ##### 拆包：将数据容器拆分为一个个的元素

  ```python
  # 将等号右侧的容器拆分后依次赋值给等号左侧变量
  # 拆包时，等号右侧容器内的元素数量要等于等号左侧变量数量，否则报错
  a, b = (3, 4)
  # 只要是容器类型就能拆
  char1, char2 = '12'
  # set拆包顺序不固定
  name1, name2 = {'John', 'Lisa'}
  # 字典拆包获得字典的key
  ```

- ##### 组包：将零散的元素组合成一个容器

  ```python
  # 将多个数据自动打包为一个容器的过程
  a = 1, 2, 3, 4
  ```

- ##### 交换：a, b = b, a

  - 首先将b, a组包成一个元组，组包过程中使用b, a两个变量中的数据值，再将元组进行拆包分别赋值给a, b，完成交换

# 3. 引用

- ##### 引用地址 id：id相同的数据一定是同一个数据，因为引用地址相同，指向的内容空间就相同

- ##### 数据类型相等的三个维度：

  - 数据类型
  - 数据的值
  - **引用地址（唯一标识）**

- 数据类型相同不一定是同一个数据

- 数据的值相同不一定是同一个数据

- 上两者都相同不一定是同一个数据

- 引用地址相同一定是同一个数据

- ##### == 判断的是值相等

- ##### print(id(list1) == id(list2))

- ##### 变量中存储的是数据的引用地址，相当于一个指向内存空间的箭头

- ##### a is b等效于id(a) == id(b)

- ##### 引用就是通过引用地址，建立变量和数据之间关系的一个过程

  ```python
  a = 1
  b = 1
  a is b 	# True
  c = [1,2,3]
  d = [1,2,3]
  c is d	# False
  ```

  ```python
  list1 = [1,2,3]
  list2 = [3,4,5]
  list1 = list2
  list2.append(6)
  list1.remove(3)
  list1	# [4,5,6]
  list2	# [4,5,6]
  ```

- ##### 当使用变量进行赋值时，其实传递的是引用地址

- ##### （不）可变数据类型：数据存储空间中的数据（不）可以被修改，叫做（不）可变数据类型

  - 可变数据类型：列表、字典、集合
  - 不可变数据类型：字符串、元组、整型、浮点型、布尔值

- ##### 不可变数据类型如果值相同，就是统一数据空间

# 3. 引用当做参数进行传递

- ##### 函数中当对全局变量使用等号赋值时，才需要使用global进行声明

- ##### 将变量传入函数内，实际上是将引用地址传入函数，而不是值传递


# 4. 匿名函数

- ##### lambda关键词

  ```python
  # lambda匿名函数的作用就是快速定义一个匿名函数
  # 格式：lambda 参数列表：返回值表达式
  # lambda的调用格式
  # 格式1：（lambda表达式）（参数1，参数2，……）(只能调用一次)
  print((lambda num1, num2: num1 + num2)(2, 3))
  # 格式2: (可以调用多次)
  sum2 = lambda num1, num2: num1 + num2
  print(sum2(2, 3))
  # lambda作用
  # 1.简化代码
  # 2.当做参数进行传递
  list2 = [(2, 3), (4, 1), (3, 5), (6, 2)]
  list2.sort(key=lambda x: x[1])
  ```

  ##### lambda的缺点：

  ##### 1. 不能书写复杂函数：变量定义、循环语句等都不支持

  ##### 2. 可读性较差，稍微长一点的语句就不容易读懂

- 三目运算符：条件成立时返回的值 if 条件 else 条件不成立时返回的值

# 5. 函数抽取

- 抽取函数时，函数中一般保存的都是完整的功能
- 能抽取出来的功能，尽量抽取出来，分支语句中如果一个分支抽取了函数，其他分支尽量都抽取
- 绝大多数情况下，函数的定义要写在业务代码之前

# 6. 学生管理系统

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
        if new_name == i['name']:
            print('该用户已经存在！')
            return

    # 如果用户输入的姓名不存在，则添加该学员信息
    info_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}

    # 将这个学员的字典数据追加到列表
    stu_info.append(info_dict)

    print(stu_info)


def del_info():
    """删除学员"""
    # 1. 用户输入要删除的学员的姓名
    del_name = input('请输入要删除的学员的姓名：')

    global stu_info
    # 2. 判断学员是否存在:如果输入的姓名存在则删除，否则报错提示
    for i in stu_info:
        if del_name == i['name']:
            stu_info.remove(i)
            break
    else:
        print('该学员不存在')

    print(stu_info)


# 修改函数
def modify_info():
    """修改函数"""
    # 1. 用户输入要修改的学员的姓名
    modify_name = input('请输入要修改的学员的姓名：')

    global stu_info
    # 2. 判断学员是否存在：如果输入的姓名存在则修改手机号，否则报错提示
    for i in stu_info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
    else:
        print('该学员不存在')

    print(stu_info)


# 查询学员
def search_info():
    """查询学员"""
    # 1. 输入要查找的学员姓名：
    search_name = input('请输入要查找的学员姓名：')

    global stu_info
    # 2. 判断学员是否存在：如果输入的姓名存在则显示这位学员信息，否则报错提示
    for i in stu_info:
        if search_name == i['name']:
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
    # 添加阻塞函数查看输出效果
    input()
```

# 7. PEP8语法规范

- ##### 缩进使用4个空格，不允许混用空格制表符

- ##### 每一行最大长度限制在79个字符内

- ##### 代码中可以直接换行，但是在换行末尾会加一个转译字符，证明和下行是同一行代码，或者可以将朝上代码用括号包裹起来，此时可以随意换行

- ##### 换行不能拆分变量或关键词短语

- ##### 函数、类之间隔两行

- ##### 不单独使用'I/l/O'

- ##### 类名使用大驼峰命名法

- ##### 函数名小写使用下划线分割法

- ##### 函数参数名与已有关键词冲突，使用同义词或加别的内容以示区别

- ##### 更多请见https://www.python.org/dev/peps/pep-0008

