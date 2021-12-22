def func1():
    file = open('student.txt', 'w', encoding='utf8')
    while True:
        option = input('请输入数字（0表示关闭程序；1表示输入）：')
        if option == '1':
            name = input('请输入姓名')
            major = input('请输入专业')
            grade = input('请输入年级')
            m_class = input('请输入班级')
            file.write('姓名：%s，专业：%s，年级：%s，班级：%s\n' % (name, major, grade, m_class))
        elif option == '0':
            break
        else:
            print('只能输入0或1，请重新输入！')
            continue
    file.close()


def func2():
    file = open('student.txt', 'r', encoding='utf8')
    print(file.read())
    file.close()


func1()
func2()
