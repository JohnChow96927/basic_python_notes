# list1 = []
# print(list1)
# list1.pop()
# print(list1)
# list3 = [1, 2, 3, 3, 3, 1, 2]
# print(list3)
# # 删除list3中所有的3
# x = int(input("请输入您想删除的数："))
# while x in list3:
#     list3.remove(3)
# print(list3)
#
# print((5, 6, 7,) + (8,))
# set1 = {'1', '2', '4', '5', '6', '3', '3'}
# print(set1)

# stu_dict = {'name': 'john', 'age': '25', 'gender': '男'}
# stu_dict.update(学号='z5233652')
# print(stu_dict)
# stu_dict.update(age=18)
# print(stu_dict)
# stu_dict.pop('age')
# print(stu_dict)
# for k, v in stu_dict.items():
#     print(f'键为{k},值为{v}')

# print(stu_dict.keys())
# print(stu_dict.values())
# print(stu_dict.items())

# list7 = [i for i in range(1, 101) if '7' not in str(i) and i % 7 != 0]
# print(list7)

# list1 = [11, 45, 34, 51, 90]
# list2 = [34, 4, 16, 23, 0, 90]
# new_list = list(set(list1 + list2))
# new_list.sort(reverse=True)
# print(new_list)
# tuple1 = (2)
# tuple2 = (2,)
# print(type(tuple1))
# print(type(tuple2))
# my_list = ["spring", "look", "strange", "curious", "black", "hope"]
# i = 0
# while i < len(my_list):
#     if my_list[i][0] == "s":
#         my_list.remove(my_list[i])
#         continue
#     i += 1
# my_list[0] = 'joke'
# my_list.insert(1, my_list[-1])
# print(my_list)
# tuple1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# # 法一
# one = tuple1[2]
# print(one)
# # 法二
# two = tuple1[2:3][0]
# print(two)
# # 法三
# for i in tuple1:
#     if i == 'alisi':
#         print(i)
# typle1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# print(len(typle1))

# dict1 = {'name': 'python'}
# dict1.update(name='chuanzhi')
# print(dict1)

# dict1 = {'name': 'chuanzhi', 'age': 18}
# del dict1['age']
# print(dict1)
# dict1.clear()
# print(dict1)

# dict1 = {'name': 'chuanzhi', 'age': 18}
# for k in dict1.keys():
#     print(k)
# for v in dict1.values():
#     print(v)
# for k, v in dict1.items():
#     print(k, ':', v)

# product = [
#     {"name": "电脑", "price": 7000},
#     {"name": "鼠标", "price": 30},
#     {"name": "usb电动小风扇", "price": 20},
#     {"name": "遮阳伞", "price": 50},
# ]
# price_sum = 0
# for p in product:
#     for k in p.keys():
#         if k == 'price':
#             price_sum += p[k]
# if price_sum > 8000:
#     print('不能')
# else:
#     print('能')
