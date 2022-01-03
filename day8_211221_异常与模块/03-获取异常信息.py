# 捕获异常时获取异常信息
# 抛出异常后在控制台的输出中:之前是异常类,:之后是异常信息
'''
获取异常信息的方式:
try:
    可能出现异常的代码
except 异常类型 as 异常信息(对象):
    可以使用print输出异常信息
    print(异常信息)
'''

# try:
#     print(a)
# except NameError as error:
#     print(error) # name 'a' is not defined

# 如果有多个异常类组成的元组我们需要怎么做

try:
    # print(a)
    print(1/0)
# 有多个异常类时,最多只能捕获一个异常信息,所以对于元组使用一个as 就可以了
except (NameError, ZeroDivisionError) as a:
    print(a)


# 练习:
# 尝试打开一个文件,读取其中的数据
# 如果文件存在,就读取内部数据
# 如果文件不存在,就新建文件,并在内部书写'Python+大数据40期基础班'

try:
    file_name = input('请输入您要打开的文件名称:')
    file = open(file_name, 'r', encoding='utf8')
    print(file.read())
    file.close()
except FileNotFoundError as error:
    print(error)
    file = open(file_name, 'w', encoding='utf8')
    file.write('Python+大数据40期基础班')
    file.close()

