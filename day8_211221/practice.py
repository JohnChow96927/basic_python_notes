# try:
#     file = open('123.txt', 'r', encoding='utf8')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError as error:
#     print(error)
#     file = open('123.txt', 'w', encoding='utf8')
#     file.write('Python+大数据40期基础班')
#     file.close()
# print('程序结束')
# 异常传递
# try:
#     file = open('java.txt', 'r', encoding='utf8')
#     try:
#         print(file.read())
#         print(a)
#     except NameError:
#         print('数据类型错误')
# except FileNotFoundError as error:
#     print(error)
#     print('该文件不存在')
#     open('java.txt', 'w', encoding='utf8')
# except Exception as e:
#     print(e)
#     print('出现未知异常')
# else:
#     print('牛逼')
# import sys
#
# for s in sys.path:
#     print(s)
# from my_package import *
#
# print(my_module1.gogo)
if __name__ == '__main__':
    print()