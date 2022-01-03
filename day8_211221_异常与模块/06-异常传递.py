# 异常穿透(异常传递):
# 1.有异常捕获的嵌套(try中嵌套了另外的一个try)
# 2.内层try无法捕获到指定异常,外层try会继续捕获

# try:
#     file = open('python.txt', 'r')
#     try:
#         print(file.read())
#         print(a)
#     except TypeError:
#         print('数据类型错误')
# except FileNotFoundError as e:
#     print(e)
#     print('该文件不存在')
# except Exception as e:
#     print(e)
#     print('出现了未知异常')

# 内层try没有捕获到指定异常,传递到中层try.中层也没有捕获到指定异常,则传递到最外层
try:
    try:
        file = open('python.txt', 'r')
        try:
            print(file.read())
            print(a)
        except TypeError:
            print('数据类型错误')
    except FileNotFoundError as e:
        print(e)
        print('该文件不存在')
except NameError as e:
    print(e)
    print('出现了名称错误')

# 异常捕获时,从内向外一层层的传递没有捕获成功的异常的过程叫做异常传递,或者异常穿透