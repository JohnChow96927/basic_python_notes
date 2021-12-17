# # import numpy as np
# #
# # file_count = int(input('请输入需要下载的文件数量：'))
# # for i in range(file_count):
# #     random_seed = np.random.random()
# #     if random_seed < 0.1:
# #         print(f'第{i + 1}个文件下载失败！{random_seed}')
# #         print('文件下载失败！')
# #         break
# #     print(f'第{i + 1}个文件下载成功！')
# #     i += 1
# # else:
# #     print('文件全部下载成功')
# str1 = 'abcdefg'
# print(str1.find('efg'))

# i = 1
# while i <= 100:
#     if i % 7 == 0:
#         print("哈~")
#         i += 1
#         continue
#     print(i)
#     i += 1
#
# a = "itheima"
# char_to_find = input('请输入一个字母：')
# for ch in a:
#     if ch == char_to_find:
#         print('找到了')
#         break
# else:
#     print('查无此字母')

# dest = int(input("请输入一个数："))
# sum_result = 0
# for i in range(dest + 1):
#     sum_result += i
# print(f"从0到{dest}的累加和为{sum_result}")
# user_username = input("请输入用户名：")
# user_password = input("请输入密码：")
# if len(user_username) not in range(5, 16):
#     print("用户名长度不符合要求（5-15位）")
# if len(user_password) not in range(6, 21):
#     print("密码长度不符合要求（6-20位）")
# if len(user_password) in range(5, 16) and len(user_password) in range(6, 21):
#     print(f'您输入的用户名是：{user_username}，密码为：{user_password}')

# words_by_xun = '鲁迅说："我没有说过这句话"'
# print(words_by_xun)

# user_name = input("请输入您的姓名：")
# user_age = int(input("请输入您的年龄："))
# user_hobby = input("请输入您的爱好：")
# print('您的姓名是%s, 您的年龄是%p，您的爱好是%s。' % (user_name, user_age, user_hobby))

# words = "abcdefghi"
# result = words[2:7:2]
# print(result)
import re
original_document = """
   Maybe they are simply great enough to receive without misgiving. Most think that they are above being supported by the town; but it often happens that they are not above supporting themselves by dishonest means, which should be more disreputable. Cultivate poverty like a garden herb, like sage.
"""

word_to_find = input("请输入您想查找的单词：")
result = ''
if word_to_find in original_document:
    result = original_document.replace(word_to_find, word_to_find + 's')
else:
    print(f"{word_to_find}不在该字符串中")
result = result.lower()
result = result.title()
result = result.strip()
print(result)

