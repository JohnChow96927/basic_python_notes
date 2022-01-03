def print_info():
    """打印功能菜单"""
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def choose_option(option):
    """选择要执行的功能"""
    if option == '1':
        add_student()
    elif option == '2':
        delete_student()
    elif option == '3':
        modify_student()
    elif option == '4':
        search_student()
    elif option == '5':
        show_all_students()
    elif option == '6':
        exit_program()


def add_student():
    """添加学员"""
    # 思考:学员信息用什么数据类型来存储?? 字典
    # 多个学员信息用什么数据类型来存储???  列表
    # 所以我们需要使用列表嵌套字典的方法来保存多个学员的数据信息
    # 我们需要使用一个全局变量,来保存学员数据,因为我们需要在多个函数中引用这个学员信息

    # 1.先要获取用户添加学员的学号
    stu_id = input('请输入您要添加学员的学号:')
    # 2.查询该学号是否存在
    # 3.判断
    for student_info in student_info_list:
        # 如果学号存在,则提示,学员已存在
        if student_info['stu_id'] == stu_id:
            print('该学员已经存在')
            break
    else:
        # 如果学号不存在,则添加新学员
        name = input('请输入您要添加学员的姓名:')
        age = input('请输入您要添加学员的年龄:')
        # 创建一个字典储存学员信息
        stu_info = {'stu_id': stu_id, 'name': name, 'age': age}
        # 将字典整体存入学员信息列表中
        student_info_list.append(stu_info)
        # 打印列表查看是否添加成功(临时)
        # print(student_info_list)


def delete_student():
    """删除学员"""
    # 1.获取要删除学员的id
    stu_id = input('请输入您要删除学员的id:')
    # 2.遍历查询是否存在这个学员id
    for student_info in student_info_list:
        # 如果id存在,就删除学员
        if student_info['stu_id'] == stu_id:
            student_info_list.remove(student_info)
            # 打印列表查看是否删除成功(临时)
            # print(student_info_list)
            break
    else:
        # 如果id不存在,就输出该学员不存在
        print('您要删除的学员不存在')


def modify_student():
    """修改学员"""
    # 1.获取要修改学员的id
    stu_id = input('请输入要修改学员的id:')
    # 2.判断被修改学员是否存在
    for student_info in student_info_list:
        if student_info['stu_id'] == stu_id:
            # 如果存在就修改
            student_info['name'] = input('请输入您要修改为的姓名:')
            student_info['age'] = input('请输入您要修改为的年龄:')
            # 打印列表查看是否修改成功(临时)
            # print(student_info_list)
            break
    else:
        # 如果不存在就提示该学员不存在
        print('要修改的学员不存在!')


def search_student():
    """查询学员"""
    # 1.获取要查询学员的id值
    stu_id = input('请输入要查询学员的id:')
    # 2.循环遍历判断学员你是否存在
    for student_info in student_info_list:
        # 3.如果存在,则输出学员信息
        if student_info['stu_id'] == stu_id:
            print(f"学员的学号是{student_info['stu_id']}, "
                  f"学员的姓名是{student_info['name']}, "
                  f"学员的年龄是{student_info['age']}")
            break
    else:
        # 如果不存在,则输出此学员不存在
        print('您要查询的学员不存在')


def show_all_students():
    """展示所有学员"""
    # 循环遍历所有学员,依次打印学员信息
    for student_info in student_info_list:
        print(f"学员的学号是{student_info['stu_id']}, "
              f"学员的姓名是{student_info['name']}, "
              f"学员的年龄是{student_info['age']}")


def exit_program():
    """退出程序"""
    # Process finished with exit code 0 退出码为0 证明是正常结束 非0 为异常结束
    # print(a)
    exit('程序结束')


# 创建一个学员列表,保存所有学员的信息
student_info_list = [{'stu_id': '001', 'name': '小明', 'age': '18'}]

while True:
    # 1.展示功能列表(由于需要循环处理数据,只有执行6命令时才能退出,所以需要死循环,展示功能列表可以封装函数)
    print_info()

    # 2.获取用户输入的指令
    option = input('请输入您要执行的功能:')

    # 3.根据用户的输入,判断要执行的功能
    choose_option(option)

    # 添加一个阻塞函数,方便查看输出效果
    input()
