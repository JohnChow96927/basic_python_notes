# while循环的嵌套其实就是在while的循环体中嵌套另外一个循环体

# 需求: 做运动: 跑三圈,做一次蹲起,为一组运动,每天要做五组运动

# i = 0
# while i < 3:
#     print('我再跑步,跑了%d圈' % (i+1))
#     i += 1
# print('完成一次蹲起')

# i = 0
# while i < 5:
#     j = 0
#     while j < 3:
#         print('我再跑步,跑了%d圈' % (j + 1))
#         j += 1
#     print('完成一次蹲起')
#     print(f'第{i+1}组运动已经完成')
#     i += 1


# 循环嵌套应用
'''
打印一个*阵  五行五列
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
'''

# i = 0
# while i < 5:
#     # 使用print输出数据内容时, 内容输出完成会自动执行换行,所以我们想让* 在一行输出
#     # 需要将print的结束符改掉,end = ' '
#     print('*', end=' ')
#     i += 1

# 分析: 外层循环控制的是输出图形的行数,内层循环控制的是输出图形的列数
# i = 0
# while i < 5:
#     j = 0
#     while j < 5:
#         print('*', end=' ')
#         j += 1
#     print()
#     i += 1

'''
打印三角形
* 
* * 
* * * 
* * * *  
* * * * *
'''
# 分析: 一共五行, 一共几列,第一行1列, 第二行2列....
# i = 0
# while i < 5:
#     j = 0
#     # 当i=0的时候是第一行,如果想让内层循环执行一次,?应该等于几??? 1
#     # 当i=1的时候,是第二行, 如果想让内层循环执行2次, ? 应该等于??? 2
#     # 当i=2...............................................3
#     # 当i=3...............................................4
#     # 当i=4...............................................5
#     while j < i+1:
#         print('*', end=' ')
#         j += 1
#     print()
#     i += 1

# 练习: 根据上方的三角形打印打印一个倒三角
'''
打印三角形
* * * * *
* * * * 
* * * 
* * 
* 
'''
# 分析:一共5行外层循环执行5次, 内层第一行执行5次,第二行执行4次........
i = 0
while i < 5:
    j = 0
    # 第一行 i = 0   打印5个*  ? = 5
    # 第二行 i = 1   打印4个*  ? = 4
    # 第三行 i = 2   打印3个*  ? = 3
    # 第三行 i = 3   打印2个*  ? = 2
    # 第三行 i = 4   打印1个*  ? = 1
    # i+? = 5   ? = 5-i
    while j < 5-i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

# 思考题,打印正三角形
'''
    *
   ***
  *****
 *******
*********
'''





















