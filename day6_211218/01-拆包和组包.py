# 拆包:将数据容器拆分为一个个的元素
# 组包:就是将零散的元素组合成一个容器

# 拆包(解包):
# 将等号右侧的容器拆分后,依次赋值给等号左侧的变量就是拆包的提现
# 拆包时,等号右侧中容器内的元素数量要等于等号左侧变量的数量,否则报错
a, b = (3, 4)
# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = (3, 4)
# ValueError: too many values to unpack (expected 2)
# a, b = (2, 3, 4)
print(a)
print(b)

# 只要是容器类型就能用拆包
char1, char2 = '12'
print(char1)
print(char2)

# set集合也能拆包,但是赋值顺序无法控制
a, b, c = {'bob', 'tom', 'rose'}
print(a)
print(b)

# dict 将字典拆包,获得的是字典的键key
dict1 = {'a': 1, 'b': 2}
a, b = dict1
print(a)
print(b)

# 组包(打包):
# 将多个数据自动打包为一个容器的过程就是组包
a = 1, 2, 3, 4

# 数值交换
a = '牛奶'
b = '可乐'
# 交换
c = a
a = b
b = c
print(a)
print(b)

# 交换方法二
# 首先将b, a 组包成一个元组,组包过程中使用的是b,a两个变量中的数据值
# 再将元组进行拆包,值分别按序赋值给a, b,从而完成了交换
a, b = b, a

print(a)
print(b)
