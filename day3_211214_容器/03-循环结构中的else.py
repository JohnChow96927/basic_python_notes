# 循环结构中的else,在循环正常结束后,会执行else中所控制的代码块
# 循环异常结束时,else中的代码不会被执行(break 会造成循环异常结束, continue不会造成循环的异常结束)

# 当循环条件不成立时会自动跳出循环并执行else中的命令,但是使用break 不会执行到循环条件不成立的时候,所以不会执行else
# i = 1
#
# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# else:
#     print('数字输入完成')
#
#
# for i in range(0, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print('数字输入完成')


i = 1

while i <= 5:
    print(i)
    if i == 3:
        i += 1
        continue
    i += 1
else:
    print('数字输入完成')

# 循环结构中的else 的应用

# 需求: 输入账号密码, 验证是否正确,如果正确,则提示登录成功跳出循环,如果不正确,则重新输入,如果三次输入错误,则提示登录失败

username = 'chuanzhi'
password = 'qwer'

# input_username = input('请输入您的用户名:')
# input_password = input('请输入您的密码:')

# # 如果想让其重新输入,要么重新书写判断代码,要么循环
# i = 1
# while i <= 3:
#     # 如果将获取用户名和密码的代码写在循环体之外,会输入一次用户名和密码,判断多次,如果对永远对,如果错,永远错
#     # 我们需要每次判断之前,先输入用户名和密码
#     input_username = input('请输入您的用户名:')
#     input_password = input('请输入您的密码:')
#
#     if username == input_username and password == input_password:
#         print('登录成功')
#         break
#     else:
#         print('用户名或密码错误,请重新输入')
#     i += 1
# # 三次都没有输入正确,则登录失败
# else:
#     print('登录失败')


# 需求: 下载文件,一共十个,如果所有文件下载完成,就输出'文件全部下载成功'
# 如果中途有文件下载失败,则退出并提示下载失败.

for i in range(1, 11):
    if i == 5:
        print('网络故障,文件下载失败')
        break
    print(f'第{i}个文件下载完成')
else:
    print('文件全部下载完成')















