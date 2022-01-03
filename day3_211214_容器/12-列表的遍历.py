# 使用for循环遍历列表
name_list = ['Jack', 'Rose', 'Tom', 'Bob']

# for循环中的临时变量,可以修改名称
for name in name_list:
    print(name)

# for 循环的逻辑,就是依次获取容器中的每一个元素,如果元素全部获取完,则跳出循环.

# 使用while循环遍历列表
# 列表索引超出范围
# IndexError: list index out of range
# 获取列表中的元素,如果元素下标的值 在列表中不存在,则报错
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# enumerate : 在遍历列表的同时,可以给列表一个序号,序号从0开始,正好与下标值相同
# for item in enumerate(name_list, 100):
#     print(item)
# '''
# (0, 'Jack')
# (1, 'Rose')
# (2, 'Tom')
# (3, 'Bob')
# '''

for index, name in enumerate(name_list):
    print(index, name)

'''
0 Jack
1 Rose
2 Tom
3 Bob
'''


print('123', '456', '678')


