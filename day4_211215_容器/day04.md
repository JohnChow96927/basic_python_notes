
## 每日练习

### 题目1 （实操题）

#### 题干

将下列两个列表合并，将合并后的列表去重，之后降序并输出

list1 = [11, 45, 34, 51, 90]
list2 = [34, 4, 16, 23, 0, 90]


#### 训练目标

列表操作方法的使用

#### 训练提示

1， 列表直接可以直接拼接，元素会合并到同一个列表中
2， 可以使用sort对列表进行排序

#### 参考方案

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

#### 操作步骤

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

#### 参考答案

``` python
list1 = [11, 45, 34, 51, 90]
list2 = [34, 4, 16, 23, 0, 90]
new_list = list(set(list1 + list2))
new_list.sort(reverse=True)
print(new_list)
```

### 题目9 （实操题）

#### 题干

有如下两行代码：
tuple1 = (2)
tuple2 = (2,)
请问tuple1与tuple2有什么不同

#### 训练目标

让学生知道含有元素的元组的定义的方式

#### 训练提示

通过肉眼能看到的只是一个逗号的区别，那么在python里面他是怎么理解的呢？

#### 参考方案

用type（）方法来分别对这两个变量进行区别

#### 操作步骤

用type(tuple1),与type(tuple12)的结果进行比较

#### 参考答案

``` python
tuple1 = (2)
tuple2 = (2,)
print(type(tuple1))	# <class 'int'>
print(type(tuple2))	# <class 'tuple'>
```

### 题目3（实操题）

#### 题干

给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且并且把最后一个元素复制一份，放在joke的后边

my_list = ["spring", "look", "strange", "curious", "black", "hope"]

#### 训练目标

 列表包含的操作
 列表的相关操作


#### 训练提示

1. 通过for循环遍历列表，获取到每一个元素
2. 通过列表的操作方法对列表进行修改


#### 参考方案

1. 通过for循环获取每一个元素
2. 通过remove删除列表中的元素
3. 通过insert函数在指定位置插入元素

#### 操作步骤

1. 通过for循环获取每一个元素，并使用startswith方法判断是否以某字符串开头
2. 如果条件成立，则通过remove删除选中的元素
3. 获取到最后一个元素，通过insert将元素放在指定的位置上

#### 参考答案

``` python
my_list = ["spring", "look", "strange", "curious", "black", "hope"]
i = 0
while i < len(my_list):
    if my_list[i][0] == "s":
        my_list.remove(my_list[i])
        continue
    i += 1
my_list[0] = 'joke'
my_list.insert(1, my_list[-1])
print(my_list)
```


### 题目4 （实操题）

#### 题干

将下列两个列表合并，将合并后的列表去重，之后降序并输出

list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]


#### 训练目标

列表操作方法的使用

#### 训练提示

1， 列表直接可以直接拼接，元素会合并到同一个列表中
2， 可以使用sort对列表进行排序

#### 参考方案

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

#### 操作步骤

1，使用 +  对列表进行拼接
2，使用set方法将列表转变成集合，以便于去重，
3，使用sort函数，参数reverse=True对列表进行倒序排序

#### 参考答案

``` python
list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]
new_list = list(set(list1 + list2))
new_list.sort(reverse=True)
print(new_list)
```

### 题目5（实操）

#### 题干

现有：``tuple1 = ("tom","kaisa","alisi","xiaoming","songshu")``
我想获得“alisi”这个内容，你能否想到三种方法来做？

#### 训练目标

元组按下标取值
元组的切片操作
元组的遍历操作

#### 训练提示

1. 在元组里面，可以按照下标来取值
2. 在元组里面，也是可以支持切片（与字符串类似）操作的
3. 在元组里面，可以通过遍历取到每一个元素


#### 参考方案

1. 用元组取下标为2的值
2. 可以利用切片从下标2开始取到下标3之前
3. 可以用for循环来遍历所有的值，判断，如果有一个是alisi，那就输出

#### 操作步骤

1. typle1[2]
2. typle1[2:3]
3. for x in typle1先执行遍历，再进行判断

#### 参考答案

``` python
tuple1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# 法一
one = tuple1[2]
print(one)
# 法二
two = tuple1[2:3][0]
print(two)
# 法三
for i in tuple1:
    if i == 'alisi':
        print(i)
```

### 题目6（实操题）

#### 题干

有如下元组：
``typle1 = ("tom","kaisa","alisi","xiaoming","songshu")``
求出他的长度

#### 训练目标

1. 元组中内置方法len的使用

#### 训练提示

1. 对于这个题目要求，我们可以用到自己学过的知识，比如遍历这个元组，并且同时记录元素个数
2. 但是对于我们强大的python来说，有没有什么最直接的方式呢？

#### 参考方案

1. 参考len用法

#### 操作步骤

1. 直接将元组放入len（）中即可

#### 参考答案

``` python
typle1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
print(len(typle1))
```

### 题目7（实操题）

#### 题干

现有字典``dict1 = {'name':'python'}``，将键为``'name'的值更改为'chuanzhi'``

#### 训练目标

字典中键值对的更改操作

#### 训练提示

1. 已经有了一个键值对，要对其进行更改值
2. 此时只需要使用'='来执行赋值操作就行

#### 参考方案

1. 先指定要更改的键
2. 使用“=”符号，给这个键赋值一个值为python的字符串

#### 操作步骤

1. dict1["name"]来指定键的名称，用‘=’来赋值要更改的值（'chuanzhi'）

#### 参考答案

``` python
dict1 = {'name': 'python'}
dict1.update(name='chuanzhi')
print(dict1)
```

### 题目8（实操题）

#### 题干

现有字典``dict1 = {'name':'chuanzhi','age':18}``
  要求：

​	1.删除age：18这个键值对

​	2.将整个字典里面的所有键值对，清空

#### 训练目标

1. 对于字典中删除的操作
2. del的使用
3. clear() 的使用

#### 训练提示

1. 有给定的字典，我们要怎么来完成删除操作？
2. 在删除操作中，del与clear有怎么样的区别？

#### 参考方案

1. 删除一个指定的键值对，要用到del。
2. 清空整个字典，要用到clear（）方法。

#### 操作步骤

1. del 要删除的键
2. 调用字典字典的clear的方法即可。

#### 参考答案

``` python
dict1 = {'name': 'chuanzhi', 'age': 18}
del dict1['age']
print(dict1)
dict1.clear()
print(dict1)
```

### 题目 9（实操题）

#### 题干

现有字典``dict1 = {'name':'chuanzhi','age':18}``
要求：

​	1.使用循环将字典中所有的键输出到屏幕上
​    2.使用循环将字典中所有的值输出到屏幕上
​    3.使用循环将字典中所有的键值对输出到屏幕上
​      输出方式：  

​				name：chuanzhi
​                age:18

#### 训练目标

1. for循环的使用复习
2. 学会如何获取字典所有的键
3. 学会如何获取字典所有的值
4. 学会如何获取字典所有的键值对

#### 训练提示

1. 用for来实现循环
2. 用字典.keys()来获取所有的键
3. 用字典.values()来获取所有的值
4. 用字典.items()来获取所有的键值对

#### 参考方案

用for来实现循环，让字典.keys()取到所有的键并控制循环次数，依次打印出每一个值，值与键值对同理；

#### 操作步骤

1. 让字典.keys()获取所有的值，将所有的值进行循环遍历，并依次print（）
2. 让字典.keys()获取所有的值，将所有的值进行循环遍历，并依次print（）
3. 让字典.items()获取所有的值，将所有的值进行循环遍历，并依次print（key, ":", value）

#### 参考答案

``` python
dict1 = {'name': 'chuanzhi', 'age': 18}
for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)
for k, v in dict1.items():
    print(k, ':', v)
```

### 题目10 (实操题)

#### 题干

有这样的一个列表

```python
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
```

然后小明一共有8000块钱，那么他能不能买下这所有商品？
如果能，请输出“能”，否则输出“不能”

#### 训练目标

if判断语句的复习使用
列表与字典的复合使用
遍历列表与遍历字典的使用

#### 训练提示

题目中给了“能不能”三个字，那么这时候用什么语句来实现呢？
题目中数据是用列表来套字典来存储的，那么获取数据是不是要遍历呢？
在判断能不能买下的时候，那么要用那两个数据进行判断呢，这两个数据分别是什么？

#### 参考方案

使用双层for循环来遍历每一个数据，找到价格进行累计，之后判断

#### 操作步骤

1. 双层for循环来循环数据
2. 在每一层循环中来判断并累计所有的价格
3. 在循环结束之后，用总价格进行与总钱数进行比较

#### 参考答案

``` python
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
price_sum = 0
for p in product:
    for k in p.keys():
        if k == 'price':
            price_sum += p[k]
if price_sum > 8000:
    print('不能')
else:
    print('能')
```

