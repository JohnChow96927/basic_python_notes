# 字符串的定义

# 1.一对单引号
str1 = '床前明月光'
# 2.一对双引号
str2 = "疑是地上霜"
# 3.三对单引号
str3 = '''举头望明月'''
# 4.三对双引号
str4 = """低头思故乡"""


# 获取数据类型
print(type(str1))  # <class 'str'>
print(type(str2))  # <class 'str'>
print(type(str3))  # <class 'str'>
print(type(str4))  # <class 'str'>


# 在Python中单双引号不敏感,但是要注意不能混用,单双引号要成对出现

# 一对引号和三对引号的区别是什么??
# 在三对引号中可以随意换行,输出时保留换行格式.

# print("""
# 123
# 345
# 456
# 567
# """)

# print('12'
#       '345\n6789')

# 为什么在Python中要设置这么多种字符串的符号??? 方便数据处理
# 需求: 输出     鲁迅说:"I'm a 周树人"

print('鲁迅说:\"I\'m a 周树人\"')

# print('我又去了公园游玩，到池塘一带的时候看到池塘里的水很混浊，我有些不解：“明明 前几年，池塘里的水很清的，如今这水为何这么混浊？”看着这池塘我仿佛听到了池塘妹 妺的诉苦：“咳！咳！咳！可恶的人类，每个人来我这里时都把垃圾扔在我身上，都把我 美丽的衣裳给弄脏了，咳！咳！唉，好怀念以前。“我仔细看，可不是！满池的垃圾：有 饮料舾、塑料袋、零食袋好多垃圾，旁边明明有垃圾箱，却还往池塘里扔，如今人们 的环保意识逐渐降低了，比如：有道不走却图近在草坪上踩过去，让小草去承受百般的痛 苦。以前鸟鸣阵阵，现在，鸟鸣寥寥无几。')

# 在Python中可以不使用转义字符而输出或者传递文章中的引号
# 在Python中使用不同的符号定义字符串,在字符串内部就可以随意使用印好了,
# 比如想在内部使用单引号,字符串就用双引号定义,如果在内部想使用单引号和双引号,就在外部使用三对引号定义.
print('''"鲁迅说:"I'm a 周树人""''')