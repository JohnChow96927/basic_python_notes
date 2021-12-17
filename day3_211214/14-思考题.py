#

'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
# 分析: 每一行*的个数是多少? 1 3 5 7 9   2*行数 - 1

# 一共5行

# 每一行空格的数量是多少? 4 3 2 1 0   行数+空格数 = 5  空格数 = 5 - 行数

# 一共5行,循环5次
for i in range(1, 6):
    # 先画空格
    for j in range(1, 6 - i):
        print(' ',end='')
    # 再画*
    for k in range(1, 2*i):
        print('*',end='')
    print()



# 一共5行,循环5次
for i in range(1, 6):
    # 先画空格
    for j in range(1, i):
        print(' ',end='')
    # 再画*
    for k in range(1, 2*(6-i)):
        print('*',end='')
    print()