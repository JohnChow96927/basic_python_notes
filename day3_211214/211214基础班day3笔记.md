#  1. 复习

- ##### 数据类型转换

  - int,float,str互转

- ##### 运算符

  - 算术运算符

    - +-*/

  - 逻辑运算符

    - and、or、not

  - 复合赋值运算符

    - +=、-= ……

  - 比较运算符

    - >、<、>=、<=

- ##### 分支语句(if)

- ##### 猜拳游戏：random模块(左闭右闭)

- ##### while循环

  - 循环变量不是必要条件(死循环)

- ##### for循环

  - range()函数，左闭右开

- ##### 代码调试

  - 打断点debug

  - Step over：向下执行一步

  - Resume Program：执行到下一个断点

# 2. break和continue

- ##### break

  - 跳出当前循环，让循环异常终止

  - 在一个循环中，break之后的所有代码将不会继续执行

- ##### continue

  - 结束本次循环，直接进行下一次循环

  - 在while中使用continue时一定要在continue前进行循环变量的调整

- ##### break和continue只能在循环体中使用

- ##### break和continue只能控制自身所在的循环

- ##### break和continue是==循环控制关键字==

# 3. 循环结构中的else

- ##### 循环结构中的else，在循环正常结束后，会执行else中所控制的代码块

- ##### 循环异常结束时，else中的代码不会被执行

  ```python
  i = 1
  while i <= 5:
    print(i)
    i += 1
  else:
    print('数字输入完成')
    
  for j in range(5):
    print(j)
  else:
    print('数字输入完成')
  ```

- ##### continue不会造成循环的异常结束

# 4. 容器类型

- ##### 在一个数据类型中存放多个数据，这种数据类型称为容器类型

- ##### Python中常见的容器类型为：列表（list）、元组（tuple）、集合（set）、字典（dict）、字符串（str）

# 5. 字符串的定义

1. ##### '一对单引号'

2. ##### "一对双引号"

3. ##### '''三对单引号'''

4. ##### """三对双引号"""

- ##### 在Python中，单、双引号不敏感，但不能混用

- ##### 三对引号中可以随意换行，输出时保留换行格式

- ##### 在Python中可以不使用转译字符而输出或者传递文章中的引号

- ##### 在Python中使用不同的符号定义字符串，在字符串内部就可以了随意使用引号了。

# 6. 字符串下标

- ##### 为了获取指定位置元素，也是为了指定位置元素的增删改查做准备

- ##### 正数下标从0开始，从左至右依次递增

- ##### 字符串中还有负数下标，从-1开始从右至左依次递减，下标-n指向字符串中==**倒数**==第n个字符

# 7. 字符串的切片

- ##### 通过一定的操作，获取字符串中一部分数据的方式

- ##### 前提是有下标，否则无法找到截取位置

- ##### 只有通过下标能获取到元素的容器才能进行切片

- ##### 切片区间为左闭右开

  ```python
  # 切片的格式：字符串[起始位置：结束位置：步长]
  ```

- ##### 步长：每次获取数据的间隔

- ##### 正数步长从左至右，负数步长从右至左取值

- ##### 起始和终止位置，左闭右开(包含起始不包含终止)

- ##### 取值从起始位置开始

- ##### 排序一般从0开始，因为排序给机看；统计一般从1开始，因为统计给人看。

- ##### 经常使用切片进行字符串反转([::-1])、复制([:])

# 8. 字符串的常见操作方法

- 1. ##### 查找

     ```python
     str1 = 'chuanzhiboke'
     ```

     - str.find(self，子字符串，起始位置，终止位置)：

       ```python
       # 起始位置和终止位置可以省略，省略后自动在整个字符串中查找
       print(str1.find('c'))	# 0
       print(str1.find('i'))	# 7
       ```

       ```python
       # 有重复字符则只获取从左至右第一次出现的元素索引值
       print(str1.find('h'))	# 1
       ```

       ```python
       # 不存在目标元素则返回-1
       print(str1.find('y'))	# -1
       ```

       ```python
       # 规定查询范围后获取的索引值是从字符串开始位置计数
       print(str1.find('h', 3, -1))	# 6
       ```

     - str.index():与find()不同处：

       - 如果没找到子字符串，则会报错(ValueError)

     - str.rfind():从右至左查询

     - str.rindex():从右至左查询

     - str.count():查询指定子字符串在目标字符串中出现的次数

     - len(str):获取字符串中元素个数，与`str.__len__()`等价

     - ………………

  2. ##### 修改

     - str.replace(self, old, new, count):在目标字符串中将子字符串替换为新内容：

       ```python
       str1 = 'hello python'
       # 如果count不赋值，则默认将所有相同字符串全部替换
       print(str1.replace('o', '$'))	# 'hell$ pyth$n'
       ```

     - str.split():

       ```python
       str2 = 'hello python and java, data is very big'
       # 按照什么字符进行拆分，什么字符就会消失
       # 有多少个分隔符，就拆分成(分隔符数量 + 1)份
       print(str2.split('o'))	# ['hell', ' pyth', 'n and java, data is very big']
       ```

       - 缺省值为按照空白进行拆分(制表位、换行符、空格)

     - str.strip():去除字符串左右两侧的指定字符

       ```python
       str3 = '   传智 播客    '
       print(str3.strip(' '))	# '传智 播客'
       ```

     - str.join():

       ```python
       strs = ['1', '2', '4']
       print('$'.join(strs))	# '1$2$4'
       ```

  3. ##### 判断

     - str.isspace()

     - str.isupper()

     - str.islower()

     - str.isidentifier()

       ```python
       str2 = '22abc'
       # 返回字符串是否符合标识符的命名规则
       print(str2.isidentifier())	# false
       str3 = ''
       ```

     - str.isalnum()

     - str.isnumeric(): 校验编码形式更丰富，只要有点(.)就不是纯数字

     - str.isdecimal()

     - str.isdigit()

     - str.isalpha()

     - str.isnumeric()

     - str.isprintable()

     - str.startswith()

     - str.endswith()

     - ………………

# 9. 列表

- ##### 格式：变量 = [元素1，元素2，元素3……]

- ##### 列表中可以储存各种数据类型，但是一般情况下一个列表中储存同种数据类型，方便进行分析数据

- ##### 列表的索引和字符串的索引基本相同

- ##### list可以通过索引修改元素值，字符串不能通过索引修改元素值

- ##### 遍历：使用for或while循环遍历列表，从前到后依次获取列表中的元素，如果元素下标的值在列表中不存在，则报错

- ##### enumerate：在遍历列表的同时，可以给列表一个序号，序号默认从0开始，正好与下标值相同：

  ```python
  name_list = ['John', 'Raina']
  for item in enumerate(name_list, 100)：
  	print(item)	# (100, 'John') 换行 (101, 'Raina')
  ```

# 10. 列表的操作

- ##### 增

  - append：在列表的末尾追加一个元素(最常用)

  - insert：在指定索引位置插入一个元素

    ```python
    name_list = ['a', 'b', 'c']
    name_list.insert(1, 'ab')
    print(name_list)	# ['a','ab', 'b', 'c']
    ```

    append插入数据比insert更安全，开发中使用更多

  - extend：在指定容器后面追加一个容器

    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)	# [1, 2, 3, 4, 5, 6]
    print(list2)	# [4, 5, 6]
    ```

- ##### 删

- ##### 改

- ##### 查

