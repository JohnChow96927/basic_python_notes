# 列表的定义
# 格式: 变量 = [元素1, 元素2, 元素3.....]
# 理论上列表中可以存储无限多个元素,但是实际上有硬件上限
list1 = [1, 2, 3, 4]

# 列表中可以储存各种数据类型,但是一般情况下,我们在列表中储存的数据,都是同种数据类型,方便进行分析处理.
list2 = [False, 1, '123', [1, 2, 3]]

# 打印列表
print(list1)
print(list2)

# 定义(了解)
# TypeError: list expected at most 1 argument, got 5
# a_list = list(1,2,3,4,5)
a_list = list((1,2,3,4,5))
print(a_list)

