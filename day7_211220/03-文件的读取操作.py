# 文件读取操作,其实就是从文件中读取数据到内存中的一个过程

# 1.打开文件
# 格式:open('文件路径', '读写模式(r读取, w写入, a追加)')
# FileNotFoundError: [Errno 2] No such file or directory: 'chuanzh.txt'
# 如果被读取模式打开的文件不存在,则报错
# file = open('chuanzh.txt', 'r')
# 如果不书写读写模式呢? 如果省略,默认就是读取模式
file = open('chuanzhi.txt')

# 2.读取文件
# 读取全部内容
# print(file.read())

# 读取指定的字符数
# 我们可以在read的括号内,填写数字进行读取
# print(file.read(4))
# 再次读取,将会接着上一次读取的内容进行继续读取
# print(file.read(4))

# 在开发中一般较大文件读取,我们都会使用read循环读取
# str1 = ''
# while True:
#     content = file.read(4) # 括号中的数据一般写1024*n
#     str1 += content
#     # 如果所有的字符都读取完成,将会返回空字符串
#     if not content:
#         # 如果返回内容为空,则跳出循环
#         break
# print(str1)

# 可以按行读取,并且多次读取,按序继续读取
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)

# 依次读取多行
# 将文件一次性读取出来,将每一行作为一个元素放到了列表当中进行返回
content = file.readlines()
print(content)

# 3.关闭文件
file.close()

# 为什么要关闭文件呢???
# 1.一个进程,最多打开1024个文件,防止后续文件无法打开,所以使用完成后必须 关闭
# 2.如果不关闭文件,在内存使用量较大时,会选择不需要文件连接自动删除,可能造成数据不安全
# 3.不手动关闭文件,可能会让句柄无法释放.
# 4.不关闭,会一直占用内存资源


# 练习: 创建一个文件 在文件中书写<<静夜思>> 打开并按行读取文件内容,全部读取完
# 1.打开文件
# 在读取文件时,或写入文件时,需要指定编码格式
# mac 和linux 系统中默认是utf8格式,  windows 默认是gbk
file = open('gushi.txt', 'r', encoding='utf8')
# 2.读取文件
str1 = ''
while True:
    content = file.readline()
    str1 += content
    if not content:
        break
print(str1)
# 3.关闭文件
file.close()

# 编码格式:
# 1.ascii
# 2.unicode码
# 3.GBK:国标码


