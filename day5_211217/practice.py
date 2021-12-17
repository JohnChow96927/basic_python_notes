# def print_triangle(n: int):
#     result = 0
#     for i in range(1, n + 1):
#         result += i
#         print('*' * i)
#     return result
#
#
# n = int(input('请输入打印行数：'))
# print(print_triangle(n))
# result = [f'page{i}' for i in range(1, 11)]
# print(result)

# def run():
#     print('我在跑步')
#     print('管住嘴，迈开腿')
#
#
# for i in range(1000):
#     run()
#
# def my_max(a, b):
#     return a if a > b else b

# def sum_random(m, n):
#     if 1 <= m <= 100 and 1 <= n <= 100:
#         print(m + n)
#     else:
#         print('输入错误!')
#
#
# sum_random(1, 3)
#
# def run_year_or_not(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print(f'{year}年是闰年')
#     else:
#         print(f'{year}年不是闰年')

# def my_sum_again(a, b):
#     if a + b > 20:
#         print('超过10的加法太难了')

# def cut_str(s: str, a1: int, a2: int):
#     return s[:a1 - 1] + s[a1+a2 - 1:]
#
# print(cut_str('123456789',2,4))

# def not_sure(*args):
#     print(args)
#
#
# not_sure(1, 2, 3, 4, 5)
import sys


def print_triangle():
    print('''
    *
    **
    ***
    ****
    *****
    ''')


def print_square():
    print('''
    *****
    *****
    *****
    *****
    ''')


user_choice = int(input('打印三角形请输入1，打印矩形请输入2：'))
if user_choice == 1:
    print_triangle()
elif user_choice == 2:
    print_square()
else:
    print('您输入的有误！')
