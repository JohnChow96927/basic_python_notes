# 将函数进行一定程度的抽取
# 1.抽取函数,要注意,函数中一般保存的都是完整的功能
# 2.能抽取出来的功能,我们最好抽取出来,分支语句中如果一个分支抽取了函数,就尽量都抽取
# 3.绝大多数情况下, 函数的定义,要写在业务代码之前

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
        # print('添加学员')
        add_student()
    elif option == '2':
        # print('删除学员')
        delete_student()
    elif option == '3':
        # print('修改学员')
        modify_student()
    elif option == '4':
        # print('查询学员')
        search_student()
    elif option == '5':
        # print('展示所有学员')
        show_all_students()
    elif option == '6':
        # print('退出程序')
        exit_program()


def add_student():
    print('添加学员')


def delete_student():
    print('删除学员')


def modify_student():
    print('修改学员')


def search_student():
    print('查询学员')


def show_all_students():
    print('展示所有学员')


def exit_program():
    print('退出程序')


while True:
    # 1.展示功能列表(由于需要循环处理数据,只有执行6命令时才能退出,所以需要死循环,展示功能列表可以封装函数)
    # print('-' * 20)
    # print('欢迎登录学员管理系统')
    # print('1: 添加学员')
    # print('2: 删除学员')
    # print('3: 修改学员信息')
    # print('4: 查询学员信息')
    # print('5: 显示所有学员信息')
    # print('6: 退出系统')
    # print('-' * 20)
    print_info()

    # 2.获取用户输入的指令
    option = input('请输入您要执行的功能:')

    # 3.根据用户的输入,判断要执行的功能
    # if option == '1':
    #     print('添加学员')
    # elif option == '2':
    #     print('删除学员')
    # elif option == '3':
    #     print('修改学员')
    # elif option == '4':
    #     print('查询学员')
    # elif option == '5':
    #     print('展示所有学员')
    # elif option == '6':
    #     print('退出程序')
    choose_option(option)

    # 添加一个阻塞函数,方便查看输出效果
    input()
