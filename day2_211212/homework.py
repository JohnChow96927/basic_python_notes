# # 水果单价
# apple_price = 6.6
# orange_price = 5
# apple_weight = float(input('请输入苹果斤数：'))
# orange_weight = float(input('请输入橘子斤数：'))
# result = apple_price * apple_weight + orange_price * orange_weight
# print(f'您购买的水果总价为:{result}')

# age = int(input('请输入您的年龄：'))
# if age > 120 or age < 0:
#     print('您输入的年龄有误！')
# elif age >= 60:
#     print('可以退休了！')
# else:
#     print('小伙子，加油干！')

# age = int(input('请输入您的年龄：'))
# if age < 0:
#     print('您输入的年龄有误！')
# elif age in range(18):
#     print(f'您的年龄是{age}: 青少年')
# elif age < 35:
#     print(f'您的年龄是{age}: 青年')
# elif age < 60:
#     print(f'您的年龄是{age}: 中年')
# else:
#     print(f'您的年龄是{age}: 老年')

# # ticket取值为1表示有票，取值为0表示无票
# ticket = 1
# # seat取值为1表示有座位，取值为0表示无座位
# seat = 1
# if ticket == 1:
#     print('有票，可以上车')
#     if seat == 1:
#         print('有座，可以坐下')
#     else:
#         print('无座，请站立~')
# else:
#     print('无票，不予上车')

# user_pwd_dict = {'aaa': '123456'}
# default_verification_code = 'qwer'
# user_name = input('请输入用户名：')
# password = input('请输入密码：')
# verification_code = input('请输入验证码：')
# if verification_code == default_verification_code:
#     if user_name in user_pwd_dict.keys():
#         if password == user_pwd_dict[user_name]:
#             print('登陆成功！')
#         else:
#             print('密码或用户名输入错误！')
#     else:
#         print('用户名或密码输入错误！')
# else:
#     print('验证码输入错误！')
# import sys
#
# chinese_mark = int(input('请输入您的语文成绩：'))
# if chinese_mark not in range(101):
#     print('成绩输入有误')
#     sys.exit()
# math_mark = int(input('请输入您的数学成绩：'))
# if math_mark not in range(101):
#     print('成绩输入有误')
#     sys.exit()
# english_mark = int(input('请输入您的英语成绩：'))
# if english_mark not in range(101):
#     print('成绩输入有误')
#     sys.exit()
# average_mark = int((chinese_mark + math_mark + english_mark) / 3)
# if average_mark < 60:
#     print('不及格')
# elif average_mark > 90:
#     print('优秀')
# else:
#     print('良')

# year = int(input('请输入一个年份：'))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year}年是闰年')
# else:
#     print(f'{year}年不是闰年')

# user_height = float(input('请输入您的身高（m)：'))
# user_weight = float(input('请输入您的体重（kg）：'))
# user_bmi = user_weight / (user_height ** 2)
# if user_bmi < 18.5:
#     print('过轻')
# elif user_bmi < 25:
#     print('正常')
# elif user_bmi < 28:
#     print('超重')
# elif user_bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# i = 0
# while i < 5:
#     print('hello world')
#     i += 1

# i = 1
# sum_result = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum_result += i
#     i += 1


