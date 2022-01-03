# def sum_recur(n):
#     if n == 1:
#         return 1
#     return sum_recur(n - 1) + n
#
#
# print(sum_recur(100))

# file = open('静夜思.txt', 'w', encoding='utf8')
# poem_list = ['窗前明月光\n', '疑是地上霜\n', '举头望明月\n', '低头思故乡\n']
# for s in poem_list:
#     file.write(s)
# file.close()
#
# file = open('静夜思.txt', 'r', encoding='utf8')
# for s in file.readlines():
#     print(s, end='')
# file.close()

# file = open('静夜思.txt', 'a', encoding='utf8')
# file.write('''静夜思
# 李白
# ''')
# file.close()


# # 文件备份
# def backup_file(f_name):
#     """
#     1. 将待备份文件打开
#     2. 读取待备份文件
#     3. 打开新文件
#     4. 写入新文件
#     5. 关闭两个文件
#     """
#     o_file = open(f_name, 'r', encoding='utf8')
#     content = o_file.read()
#     new_file_name = ('（备份）.'.join(f_name.rsplit('.', 1)))
#     b_file = open(new_file_name, 'w', encoding='utf8')
#     b_file.write(content)
#     o_file.close()
#     b_file.close()
#
#
# file_name = input('请输入要备份的文件名：')
# backup_file(file_name)
#
#
# # 图片备份
# def backup_binary_file(f_name):
#     """
#     1. 将待备份文件打开
#     2. 读取待备份文件
#     3. 打开新文件
#     4. 写入新文件
#     5. 关闭两个文件
#     """
#     o_file = open(f_name, 'rb')
#     content = o_file.read()
#     new_file_name = ('（备份）.'.join(f_name.rsplit('.', 1)))
#     b_file = open(new_file_name, 'wb')
#     b_file.write(content)
#     o_file.close()
#     b_file.close()
#
#
# file_name = input('请输入要备份的文件名：')
# backup_file(file_name)

# import os
# try:
#     os.mkdir('chuanzhi')
#     for i in range(1, 11):
#         open(f'chuanzhi/讲义{i}.txt', 'w')
# except FileExistsError:
#     pass
#
# file_list = os.listdir('chuanzhi')
# os.chdir('chuanzhi')
# for file_name in file_list:
#     os.rename(file_name, '黑马出品 ' + file_name)
# os.chdir('../')

import os

try:
    os.mkdir('视频')  # 创建目录
    os.chdir('视频')  # 更改工作目录
    for i in range(1, 6):
        open(f'{i}.mp4', 'wb')  # 循环创建新文件
    # 添加前缀
    for f_name in os.listdir():
        os.rename(f_name, '视频' + f_name)
    os.mkdir('../视频2')  # 创建新文件夹，注意和'视频'文件夹平级
    for new_file_name in os.listdir():
        o_file = open(new_file_name, 'rb')
        content = o_file.read()
        n_file = open('../视频2/' + new_file_name, 'wb')
        copied_content = n_file.write(content)
        o_file.close()
        n_file.close()
except FileExistsError as e:
    print(e)
