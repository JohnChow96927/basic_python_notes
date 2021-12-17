# 题目1
print('hello world！')   # 输出 'hello world' 到控制台
"""
注释的作用是起到解释说明程序代码的作用，便于程序员理解代码功能。
Python中的注释有单行注释与多行注释
第一行代码后的内容就是一个位于句尾的单行注释，以# 开头，快捷键为command + /(Windows系统为ctrl + /)
只对同一行内#号后的内容生效
而这就是一个多行注释，包含在三对引号（单引号或双引号）中，不能与代码行写在同一行
其没有快捷键，如果想要同时注释多行代码可以选中要注释的代码行然后使用单行注释快捷键
"""

# 题目2
'''
step1. 打开pycharm后选择'New Project...'
step2. 将项目名称命名为'zhengyuan'
step3. 在下方选择适宜版本的Python解释器
step4. 点击窗口右下角 'create' 按钮完成项目新建
step5. 在工程文件上右键点击，选择new->Python file，命名为 'hello_py'
step6. 键入以下代码
step7. 右键点击->run
'''

print('人生苦短，我用Python')  # 向控制台输出'人生苦短，我用Python'

# 题目3
name = "老王"     # 姓名
age = 30    # 年龄
weight = 166.6    # 体重

'''
将定义的三个变量分行输出到控制台
'''
print(name)
print(age)
print(weight)

# 题目4
name = "老冀"     # 姓名
age = 20    # 年龄
weight = 166.6    # 体重

print('姓名：%s，年龄：%d岁，体重：%.2f斤' % (name, age, weight))

# 题目5
user_name = str(input('请输入用户名：'))   # 定义一个变量名为user_name的变量用来存储阻塞程序等待用户输入的用户名
password = input('请输入密码：')  # 定义一个变量名为password的变量用来存储阻塞程序等待用户输入的密码
print('您输入的用户名为%s' % user_name)     # 使用%格式化输出用户名
print(f'您输入的密码为{password}')     # 使用f-string格式化输出密码

# 题目6
x = int(input('请输入一个数字x：'))     # 从控制台读取用户输入的一个整数并转换数据类型到int用变量x存储
y = int(input('请输入另一个数字y：'))    # 从控制台读取用户输入的另一个整数并转换数据类型到int用变量y存储
sum_result = x + y     # 将x与y的值相加并储存到变量sum_result中
print(sum_result)
