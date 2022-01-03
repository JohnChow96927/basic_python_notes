# 函数的定义
def find_all_pos(src_list, sub):
    """
    :param src_list: 原始列表的数据
    :param sub: 需要查找的元素
    :return: 符合要求的所有位置的起始下标，以元组方式返回
    """
    pos_list = []
    start_pos = 0
    for i in range(src_list.count(sub)):
        # index 每次都获取从左至右第一个指定元素,所以我们需要规定查询范围
        index = src_list.index(sub, start_pos)
        pos_list.append(index)
        start_pos = index + 1

    return tuple(pos_list)


test_list = [3, 6, 1, 4, 1, 5, 6, 1, 3, 6, 2]

# 函数调用，在test_list找1所有位置的下标
ret = find_all_pos(test_list, 1)
print(ret)
