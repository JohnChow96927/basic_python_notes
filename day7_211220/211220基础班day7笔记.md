# 1. 复习

- ##### 拆包与解包：

  - 接收集合时顺序不固定
  - a, b = b, a

- ##### 引用：只有使用id才能判断两个数据是否相等(引用地址指向同一内存空间)

- ##### 可变数据类型：列表集合字典

- ##### 不可变数据类型：字符串元组整型浮点型布尔值

- ##### 变量传递实际是引用地址的传递

- ##### lambda表达式：lambda 参数列表：返回值表达式

- ##### 三目运算符

- ##### 学生管理系统

# 2. 递归(非重点，了解即可)

- ##### 在函数内部调用函数本身

- ##### 将一个复杂问题拆解为多个相同或者相似的简单问题的思维方式

- ##### 递归要有明确的跳出条件

- ##### 递归不能超出最大调用深度(默认1000)

- ##### 算力消耗大，容易出错

# 3. 文件读取操作

```python
file = open('sample.txt', 'r', encoding='utf8')
print(file.read())
file.close()
```

- ### 打开文件

  ```python
  file = open('sample.txt', 'r', encoding='utf8')
  ```

  ##### open('文件路径'，'读写模式(r读取，w写入，a追加)')

  - 如果打开文件不存在则报错
  - 读写模式的缺省值为读取模式(r)

- ### 读取文件

  ```python
  file.read()	# 读取全部内容
  file.read(4)	# 读取4个字符
  file.read(4)	# 再次读取会接着上一次读取的内容进行继续读取
  ```

  - 在开发中一般较大文件读取，都会使用read循环读取

    ```python
    str1 = ''
    while True:
      content = file.read(4)	# 括号中的数据一般写1024*n
      str1 += content
      if not content:
        break
    ```

  - 按行读取，并且多次读取，按序继续读取

    ```python
    content = file.readline()
    print(content)
    content = file.readline()
    print(content)
    ```

  - 一次读取多行，将每一行作为一个元素存放赛列表中进行返回

    ```python
    content = file.readlines()
    print(content)
    ```

- ### 关闭文件

  ```python
  file.close()
  ```

  原因：

  1. 一个进程最多打开1024个文件，防止后续文件无法打开，所以使用完成后必须关闭
  2. 如果不关闭文件，在内存使用量较大时，会选择不需要的文件连接自动删除，可能造成数据不安全
  3. 不手动关闭文件可能会造成句柄无法释放
  4. 不关闭文件，会一直占用内存资源

# 4. 编码格式

- ##### ASCII码
- ##### Unicode码：前128位为ASCII码，可以和ASCII码兼容，==**utf8**==
- ##### GBK码：国标码

# 5. 文件写入操作

- ##### 通过写入操作(w)，进行文本输入，会先将文件清空，再写入指定内容

- ##### 如果被写入的文件不存在，就新建一个被打开文件名称的新文件

  ```python
  file = open('静夜思.txt', 'w', encoding='utf8')
  poem_list = ['窗前明月光\n', '疑是地上霜\n', '举头望明月\n', '低头思故乡\n']
  for s in poem_list:
      file.write(s)
  file.close()
  ```

# 6. 文件追加操作

```python
file = open('静夜思.txt', 'a', encoding='utf8')
file.write('静夜思by李白')
file.close()
```

- 如果被追加的文件不存在，则新建一个文件

# 7. 文件读写模式

- ##### 三大类：r、w、a

- ##### 四种：x, x+, xb, xb+(x取r、w、a其中之一)

# 8. 文件备份

```python
# 文件备份
def backup_file(f_name):
    """
    1. 将待备份文件打开
    2. 读取待备份文件
    3. 打开新文件
    4. 写入新文件
    5. 关闭两个文件
    """
    o_file = open(f_name, 'r', encoding='utf8')
    content = o_file.read()
    new_file_name = ('（备份）.'.join(f_name.rsplit('.', 1)))
    b_file = open(new_file_name, 'w', encoding='utf8')
    b_file.write(content)
    o_file.close()
    b_file.close()

file_name = input('请输入要备份的文件名：')
backup_file(file_name)
```

# 9. 二进制文件备份

```python
# 图片备份
def backup_binary_file(f_name):
    """
    1. 将待备份文件打开
    2. 读取待备份文件
    3. 打开新文件
    4. 写入新文件
    5. 关闭两个文件
    """
    o_file = open(f_name, 'rb')
    content = o_file.read()
    new_file_name = ('（备份）.'.join(f_name.rsplit('.', 1)))
    b_file = open(new_file_name, 'wb')
    b_file.write(content)
    o_file.close()
    b_file.close()

file_name = input('请输入要备份的文件名：')
backup_file(file_name)
```

- ##### 二进制文件要使用rb，wb，不需要使用encoding参数

- ##### 二进制文件比较大(视频，音频，高清图片)，一般使用循环读取

# 10. 文件及文件夹操作

- ##### os模块：包含操作系统层级的一些功能，如创建文件，创建文件夹等

- ##### 文件路径

  - 相对路径：从当前路径开始查找
    - ./代表当前目录（可以省略），../代表上一级目录
  - 绝对路径：从根目录或者盘符开始查找

- ##### os.mkdir(文件夹名)：创建文件夹，已经存在则报错

- ##### os.rmdir(文件夹名)：删除文件夹，只能删除空文件夹

- ##### os.remove(文件路径)：删除文件

- ##### os.getcwd()：获取当前工作目录绝对路径

- ##### os.chdir(新工作目录路径)：更改工作目录

- ##### os.listdir(相对路径)：获取指定目录的文件（夹）列表，如果括号内什么也不写，就是获取当前工作目录中的文件列表

- ##### os.rename(旧文件名，新文件名)：如果旧文件名不存在则报错

# 11. 批量修改文件名案例

- 如果要频繁修改一个文件目录中的文件内容，最好先切换工作目录
- 操作文件时，不能光想着文件名称，还要注意文件路径

```python
import os
try:
    os.mkdir('chuanzhi')
    for i in range(1, 11):
        open(f'chuanzhi/讲义{i}.txt', 'w')
except FileExistsError:
    pass

file_list = os.listdir('chuanzhi')
os.chdir('chuanzhi')
for file_name in file_list:
    os.rename(file_name, '黑马出品 ' + file_name)
os.chdir('../')
```

