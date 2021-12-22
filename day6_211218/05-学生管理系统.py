# 分析:
# 学生管理系统的执行步骤
# 1.展示功能列表
# 2.用户选择要执行的功能
# 3.执行指定功能


# 1.展示功能列表(由于需要循环处理数据,只有执行6命令时才能退出,所以需要死循环,展示功能列表可以封装函数)

while True:
    print('-' * 20)
    print('欢迎登录学员管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)

    # 2.获取用户输入的指令
    option = input('请输入您要执行的功能:')

    # 3.根据用户的输入,判断要执行的功能
    if option == '1':
        print('添加学员')
    elif option == '2':
        print('删除学员')
    elif option == '3':
        print('修改学员')
    elif option == '4':
        print('查询学员')
    elif option == '5':
        print('展示所有学员')
    elif option == '6':
        print('退出程序')
    # 添加一个阻塞函数,方便查看输出效果
    input()
