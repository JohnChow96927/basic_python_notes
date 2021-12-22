from random import randint

m = randint(1, 9)
sum_q1 = 0
count_q1 = 0
for i in range(m, 22):
    if i % 2 == 1:
        sum_q1 += i
        count_q1 += 1
print(f'''随机数m为：{m}
随机数8到21的奇数个数为：{count_q1}
随机数8到21的奇数总和为：{sum_q1}''')
