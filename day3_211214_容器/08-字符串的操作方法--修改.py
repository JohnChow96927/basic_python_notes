# replace 在目标字符串中将子字符串替换为新内容
# replace(self(不用传值), old(旧值), new(新值), count(替换次数))
str1 = 'hello  python'
# 使用该方法可以替换字符串
print(str1.replace('python', 'bigdata'))
# 如果count不赋值,则默认将所有相同的字符串全部替换.
print(str1.replace('o', '$'))
# 如果给count赋值,则只替换从左至右指定个数的子字符串.
print(str1.replace('o', '$', 1))


# split: 将字符串按照指定的分隔符拆分为多个子字符串,放入一个列表中.
# split(self(不用传值), sep(间隔符), maxsplit(最大拆分次数))
str2 = 'hello python and               java ,data is ve\try b\nig'
# 按照什么字符进行拆分,什么字符就会消失.
# 有多少个分隔符,就差分成分隔符数量+1份
print(str2.split('o')) # ['hell', ' pyth', 'n and java ,data is very big']

# 如果括号内什么也不写会按照什么分隔符进行拆分??  空白
# 制表位, 换行符, 空格都属于空白可以用于拆分
print(str2.split())

# 如果规定了最大拆分次数会怎样??
# 如果规定最大拆分次数为3次,则从左至右开始拆分,拆分三次后停止,此时数据变为4份
print(str2.split(' ', 3)) # ['hello', 'python', 'and', '              java ,data is ve\try b\nig']


# strip: 去除字符串左右两侧的指定字符
str3 = '   传智  播客  教育  有限公司    '
print(str3.strip(' '))

str4 = '112233python112233'
print(str4.strip('11'))

# join 合并 join 可以列为split 的逆运算
# join 就是使用分隔符,将容器中的子字符串拼接到一起的方法
# 分隔符.join(self(不需要传值), iterable(可迭代类型,就是要求一个容器中储存多个子字符串,我们要将这个容器中的所有字符串拼接在一起))
list1 = ['hello', 'python', 'and', 'java', ',data', 'is', 've', 'ry', 'b', 'ig']

print('❤'.join(list1)) # hello❤python❤and❤java❤,data❤is❤ve❤ry❤b❤ig











