# 定义元组的方法

tuple1 = (1, 2, 3, 4)
print(type(tuple1))  # <class 'tuple'>
print(tuple1)  # (1, 2, 3, 4)

# 如果元组中只有一个元素怎样定义?
tuple2 = (10)
print(tuple2)  # 10
print(type(tuple2))  # <class 'int'>

# 括号是提升算数运算符优先级的
# (5 + 5) ==> (10)

# 单元素元组定义时,在元素右边添加一个逗号,告诉计算机,我这个数据是一个元组
tuple3 = (10,)
print(tuple3)  # (10,)
print(type(tuple3))  # <class 'tuple'>

# 空元组怎么定义?  ()
tuple4 = ()
tuple5 = tuple()

print(type(tuple4))  # <class 'tuple'>
print(tuple5)  # ()
print(type(tuple5))  # <class 'tuple'>

# 了解: 在定义元组时,括号可以省略,系统会帮我们自动补全括号
tuple6 = 12, 14, 16, 18
print(tuple6) # (12, 14, 16, 18)
print(type(tuple6)) # <class 'tuple'>

tuple7 = 12,
print(tuple7) # (12,)
print(type(tuple7))  # <class 'tuple'>