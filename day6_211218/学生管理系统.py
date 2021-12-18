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
