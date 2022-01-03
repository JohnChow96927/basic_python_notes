# 批量创建文件
import os

# # 创建一个chuanzhi文件件
# os.mkdir('chuanzhi')
#
# # 批量创建文件 讲义1.txt-讲义10.txt
# for i in range(1, 11):
#     open(f'chuanzhi/讲义{i}.txt', 'w')

# 需求:批量给文件添加或删除前缀
# 给文件名添加[黑马出品]前缀

# 1.获取文件列表
# file_list = os.listdir('chuanzhi')
# # print(file_list)
# # 2.遍历文件列表,获取每一个文件的文件名称
# for file_name in file_list:
#     # 3.使用rename方法将旧文件名改为新文件名
#     # FileNotFoundError: [Errno 2] No such file or directory: '讲义10.txt' -> '[黑马出品]讲义10.txt'
#     # 添加前缀
#     # os.rename('chuanzhi/'+ file_name, 'chuanzhi/[黑马出品]' + file_name)
#     # 删除前缀
#     # os.rename('chuanzhi/' + file_name, 'chuanzhi/' + file_name.replace('[黑马出品]', ''))


# 如果我们需要频繁操作一个目录下的文件,我们可以修改工作目录位置

# 批量创建文件
import os

# # 创建一个chuanzhi文件件
# os.mkdir('chuanzhi')
#
# # 批量创建文件 讲义1.txt-讲义10.txt
# for i in range(1, 11):
#     open(f'chuanzhi/讲义{i}.txt', 'w')

# 切换工作目录
# os.chdir('chuanzhi')

# 获取chuanzhi目录下的文件列表
# file_list = os.listdir()
#
# # 遍历文件列表,修改名称
# for file_name in file_list:
#     # 修改名称
#     os.rename(file_name, '[黑马出品]' + file_name)

# 练习: 在"视频"文件夹中创建 视频1.mp4-视频5.mp4 五个文件
# 给文件添加前缀,并复制到'视频2'目录下,不用改名
# 创建视频目录
# os.mkdir('视频')
# 将工作目录切换到视频目录中
# os.mkdir('视频2')
#
# os.chdir('视频')
# # 循环遍历,创建文件
# for file_name in [f'视频{i}.mp4' for i in range(1, 6)]:
#     open(file_name, 'w')

# # 添加前缀
# for file_name in os.listdir():
#     # 定义变量保存被修改后的文件名称
#     file_name_px = '[传智出品]' + file_name
#     # 修改名称
#     os.rename(file_name, file_name_px)
#     # 复制到视频2目录下
#     # 打开旧文件
#     old_file = open(file_name_px, 'rb')
#     # 读取旧文件
#     content = old_file.read()
#     # 打开新文件
#     new_file= open('../视频2/'+file_name_px, 'wb')
#     # 写入新文件
#     new_file.write(content)
#     # 关闭文件
#     new_file.close()
#     old_file.close()


# 添加前缀
for file_name in os.listdir():
    # 定义变量保存被修改后的文件名称
    file_name_px = '[传智出品]' + file_name
    # 修改名称
    os.rename(file_name, file_name_px)

# 备份
os.mkdir('视频2')
# 备份方式和上述方式一致

