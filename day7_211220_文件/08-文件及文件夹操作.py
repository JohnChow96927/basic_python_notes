# os模块: 这里边有操作系统层级的一些功能,如创建文件,创建文件夹等

# 文件路径
# 相对路径:从工作目录开始出发,查找指定目标文件所使用的路径
# 绝对路径:从根目录或者盘符开始,查找指定目标文件所使用的路径

import os

# 创建文件夹mkdir
# FileExistsError: [Errno 17] File exists: 'bigdata'
# 如果文件夹已经存在,则报错
# os.mkdir('bigdata')

# 删除文件夹
# 只能删除空文件夹
# os.rmdir('bigdata')
# 删除文件
# os.remove('bigdata/xiaoniao[副本].jpg')
# os.rmdir('bigdata')

# os.getcwd 获取当前工作目录的绝对路径
# /Users/******/day07/03-代码
print(os.getcwd())

# os.chdir 修改当前工作目录
os.chdir('./bigdata')
print(os.getcwd())

# 打开bigdata 目录下的python.txt文件进行读取
# FileNotFoundError: [Errno 2] No such file or directory: './bigdata/python.txt'
# 由于我们上边切换了工作目录,所以下边查找文件的时候要从工作目录开始查找
file = open('./bigdata.123')
print(file.read())
file.close()

# 获取指定目录的文件列表
# os.listdir()
# 如果括号内什么也不写,就是获取当前工作目录中的文件列表
print(os.listdir()) # ['python.txt']
print(os.listdir('../')) # ['02-文件读写操作的体验.py', '04-文件的写入操作.py', '.DS_Store', 'xiaoniao.jpg', '03-文件的读取操作.py', '06-文件的读写模式.py', '05-文件的追加操作.py', 'itcast.txt', '08-文件及文件夹操作.py', 'gushi[副本].txt', '00-作业讲解.py', 'python.py', 'gushi.txt', 'chuanzhi.txt', '01-递归.py', 'bigdata', '.idea', '07-文件备份.py']

# rename 可以修改文件名, 并且文件不存在时,报错
# FileNotFoundError: [Errno 2] No such file or directory: 'bigdata.py' -> 'bigdata.123'
# os.rename('bigdata.py', 'bigdata.123')




