# # 文件备份时, 我们要做哪些事情
#
# # 1.将待备份的文件打开
# # 让用户键入要备份的文件名称
# old_file_name = input('请输入您要备份的文件:')
# # 打开文件
# old_file = open(old_file_name, 'r')
#
# # 2.读取待备份的文件
# content = old_file.read()
#
# # 3.打开新文件
# # 获取一个新文件名称
# # new_file_name = old_file_name.replace('.', '[副本].')
# # 将旧文件名按照从右至左的查找顺序,按照.拆分成两个字符串
# str_list = old_file_name.rsplit('.', 1)
# # 使用'[副本].'将刚才拆分好的字符串进行拼接
# new_file_name = '[副本].'.join(str_list)
# # print(new_file_name)
# new_file = open(new_file_name, 'w')
#
# # 4.写入新文件
# new_file.write(content)
#
# # 5.关闭新文件  关闭旧文件
# new_file.close()
# old_file.close()


# 二进制文件的备份
# 二进制文件读写时,不能使用encoding
# 文件备份时, 我们要做哪些事情

# 1.将待备份的文件打开
# 让用户键入要备份的文件名称
old_file_name = input('请输入您要备份的文件:')
# 打开文件
old_file = open(old_file_name, 'rb')

# 2.读取待备份的文件
# 二进制文件如果是视频或者音频,以及高清图片,文件比较庞大一般我们会使用循环读取的方式
content = old_file.read()

# 3.打开新文件
# 获取一个新文件名称
# new_file_name = old_file_name.replace('.', '[副本].')
# 将旧文件名按照从右至左的查找顺序,按照.拆分成两个字符串
str_list = old_file_name.rsplit('.', 1)
# 使用'[副本].'将刚才拆分好的字符串进行拼接
new_file_name = '[副本].'.join(str_list)
# print(new_file_name)
new_file = open(new_file_name, 'wb')

# 4.写入新文件
new_file.write(content)

# 5.关闭新文件  关闭旧文件
new_file.close()
old_file.close()