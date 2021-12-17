# f-string字符串
# 在Python3.6之后才有f-string字符串
# 是一种字符串的格式化方式,比 % 拼接方式更为灵活

name = 'jack'
age = 12
height = 1.85

# % 拼接方式
print('我儿子的名字叫%s, 我儿子的年龄是%d, 我儿子的身高是%f' % (name, age, height))
# f-string
# 格式'要输出的内容{变量}'
# f-string字符串在定义时,引号之前要使用f 或者F进行修饰
print(f'我儿子的名字叫{name}, 我儿子的年龄是{age}, 我儿子的身高是{height}')
print(F'我儿子的名字叫{name}, 我儿子的年龄是{age}, 我儿子的身高是{height}')

# 精度设置
# % 拼接方式
print('我儿子的名字叫%s, 我儿子的年龄是%d, 我儿子的身高是%.2f' % (name, age, height))
# f-string
# 保留n位小数{变量:.nf}
# 占用n位,不足位用0补齐{变量:0nd}
print(f'我儿子的名字叫{name}, 我儿子的年龄是{age:06d}, 我儿子的身高是{height:.1f}')

# f-string内部可以添加表达式
print(f'我儿子的名字叫{name}, 我儿子的年龄是{age*2:06d}, 我儿子的身高是{height:.1f}')
