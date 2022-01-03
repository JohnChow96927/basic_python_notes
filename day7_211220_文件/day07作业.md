### 题目[加强训练]

### 题干

编程实现向文件a.txt中书写`好好学习，天天向上`的内容。

### 训练目标

1.  文件操作练习

### 训练提示

1.  python 中如何操作文件？
2.  如何向文件中书写内容？

### 参考方案

1.  打开文件使用 open 函数
2.  向文中书写内容使用 write 函数
3.  关闭文件用 close 函数

### 操作步骤

1.  打开文件
2.  向文件中写入内容
3.  关闭文件

### 参考答案

```python
# 1. 打开文件
f = open("a.txt", 'w', encoding="utf-8")

# 2. 向文件中写入内容
f.write("好好学习，天天向上")

# 3. 关闭文件
f.close()

```

# 文件操作

## 题目1 [加强训练]

### 题干

使用文件操作，向`movie.txt`文件中写入一下内容：

```python
功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥
```
### 训练目标

* 文件的写操作

### 训练提示

* 如何往一个文件里面写入数据
* 写入的数据换行使用什么方法

### 参考方案

* 打开文件`open()`，打开方式为`"w"`
* 写入文件`write()`
* 换行使用`"\n"`
* 也可以使用`""" """`三个引号的形式，可以直接在代码里书写换行

### 操作步骤

* 打开文件，创建对象
* 写入信息
* 关闭文件

### 参考答案

* 第一种方式

~~~python
# 因为编码格式的问题，我们为了防止出现乱码，需要在这里设置encoding="utf8"
f = open("movie.txt","w", encoding="utf8")
f.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神，徐峥")
f.close()
~~~

* 第二种方式

~~~python
f = open("movie.txt","w",encoding="utf8")
f.write("""功夫，周星驰
一出好戏，黄渤
我不是药神，徐峥""")
f.close()
~~~



## 题目2 [加强训练]

### 题干

将第一题创建好的文件打开，并读取内容， 要求如下：

* 一次全部读取
* 每次读取一行

### 训练目标

* 文件的读操作

### 训练提示

* 如何读取文件内容？
* 读取全部内容的方法？
* 每次读取一行的方法？

### 参考方案

* 打开文件open，打开方式为“r”
* 读取文件read()
* 读取一行readline()
* 读取所有行readlines()

### 操作步骤

* 打开文件（使用r方式打开，如果不写那么默认是只读方式打开）
* 读取信息
* 关闭文件（每次操作完文件后要关闭文件）

### 参考答案

* 第一种方式

  ~~~python
  # 注意编码格式问题
  f = open("movie.txt",'r',encoding="utf8")
  content = f.read()
  f.close()
  print(content)
  ~~~

* 第二种方式

  ~~~python
  f = open("movie.txt",'r',encoding="utf8")
  content = f.readlines()
  f.close()
  # 读取后的内容是一个列表，注意列表中的数据中有一个"\n"。如果使用需要处理
  print(content)
  ~~~

* 第三种方式

  ~~~python
  f = open("movie.txt",'r',encoding="utf8")
  # 因为readline 每次读取一行，需要我们使用循环读取
  while True:
      content = f.readline()
      # 当我们读取的内容是空字符的时候跳出循环
      if content == "":  # if content:
          break
      print(content)
  f.close()
  ~~~




## 题目4 [综合训练1]

### 题干

编写一段代码以完成两份文件之间的相互备份

* 提示用户输入文件名。例：gailun.txt

- 创建以用户输入的名字的文件

- 打开文件写入如下信息

  ​	功夫，周星驰

  ​	一出好戏，黄渤

  ​	我不是药神，徐峥

- 将输入的数据输出到终端上

- 在文件夹中创建gailun副本.txt文件

- 将gailun.txt文件中的数据写入gailun副本.txt文件中

- 打开文件，查看文件中内容

### 训练目标

* 文件的综合使用

### 训练提示

* 每次操作完文件需要关闭
* 在windows系统中注意编码格式问题
* 需要自己重新定义一个新的文件名

### 参考方案

### 操作步骤

* 操作步骤一
  * 提示用户输入文件名
  * 打开文件
  * 写入信息
  * 关闭文件
  * 打开文件
  * 读取文件中的信息
* 操作步骤二
  * 提取文件名的后缀
  * 组建新的文件名
* 操作步骤三
  * 打开新组建的文件名字的文件
  * 写入文步骤一中读取到的信息写入到新的文件中
  * 关闭文件
* 操作步骤四
  * 打开新的文件
  * 读取文件中的内容
  * 关闭文件

### 参考答案

~~~python
# 提示输入文件
oldFileName = input("请输入要创建的文件名:")
# 以写的方式打开文件
oldFile = open(oldFileName, 'w', encoding="utf8")
oldFile.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神，徐峥")
oldFile.close()
# 打开文件
f = open(oldFileName, 'r', encoding="utf8")
#读取文件内容
context = f.readlines()
print(context)
f.close()

# 提取文件名的后缀
fileFlagNum = oldFileName.rfind('.')
# 确定文件名中有没有后缀, rfind() 找到内容返回正数下标,没有找到,返回-1
if fileFlagNum > 0:
    fileFlag = oldFileName[fileFlagNum:]

# 组织新的文件名字
newFileName = oldFileName[:fileFlagNum] + '复本' + fileFlag

# 创建新的文件副本
newFile = open(newFileName, 'w',encoding="utf8")
for lineContent in context:
    print(lineContent)
    newFile.write(lineContent)
newFile.close()

# 打开写入的新文件
f = open(newFileName, "r", encoding="utf8")
# 读取内容
context = f.read()
# 输入到终端
print(context)
# 关闭文件
f.close()
~~~




