# 使用列表的索引即可修改列表中元素的值

name_list = ['xiaoming', 'xiaohuang', 'xiaohui']

name_list[0] = 'huangxiaoming'

print(name_list)  # ['huangxiaoming', 'xiaohuang', 'xiaohui']

# sort 排序
num_list = [2, 3, 6, 1, 4, 5]
num_list.sort()

# 如果括号内什么也不写,就是按照元素值的大小升序排列
print(num_list)  # [1, 2, 3, 4, 5, 6]

# 如果括号内填写reverse=True 就会让排序规则发生变化,变为从大到小降序排列
num_list.sort(reverse=True)
print(num_list)  # [6, 5, 4, 3, 2, 1]

# reverse 反转
list1 = [1, 4, 3, 2]
list1.reverse()

# reverse不会进行排序,只是单纯的反转列表
print(list1)  # [2, 3, 4, 1]
