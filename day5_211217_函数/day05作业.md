## 每日练习

### 推导式练习：

练习题:

1、使用列表推倒式生成一个[0,5 ,10,15,20,. …50]的列表

```python
result = [i for i in range(51) if i % 5 == 0]
```

2、使用列表推到式生成一个[page1, page2,page3. . . .page10]的列表

```python
result = [f'page{i}' for i in range(1, 11)]
```

### 题目1 （实操题）

#### 题干

定义一个简单的函数run，函数的功能是输出"我在跑步" 以及 “管住嘴，迈开腿”，并调用此函数。

#### 训练目标

1. 如何定义一个函数
2. 调用函数的方式

#### 训练提示

1.  定义函数的形式是什么？声明函数的关键字是什么？
2.  怎么让函数运行？

#### 参考方案

1. 用def关键字定义函数
2. 用函数名+小括号的方式来调用函数


#### 操作步骤

1. def  run():  .......
2. run()

#### 参考答案

``` python
def run():
    print('我在跑步')
    print('管住嘴，迈开腿')
run()
```

### 题目2

#### 题干

在第一题中，我们已经用函数run实现了一些功能，如果我们想run函数做的操作执行1000遍，怎么实现代码？

#### 训练目标

1. 让同学们知道应用函数的好处

#### 训练提示

1. 我们用run函数来实现一个功能，实现一次功能就调用一次run函数，那么实现1000遍怎么实现呢？

#### 参考方案

1. 执行1000遍函数，可以调用1000次函数
2. 可以用for循环来实现1000次调用

#### 参考答案

``` python
def run():
    print('我在跑步')
    print('管住嘴，迈开腿')
for i in range(1000):
    run()
```

### 题目3

  定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值

  ##### 训练提示

  第一步：定义一个函数max

  第二步：定义两个形参

  第三步：通过比较这两个参数返回其中较大的

**参考答案**

  ```Python
def my_max(a, b):
    return a if a > b else b
  ```

### 题目4

  定义一个函数 sum_random 接收二个参数 m, n ，在函数中计算 m + n 的值，并打印结果，要求 m 和 n 是 1 -- 100 之间的数

  ##### 训练提示

  第一步：定义函数并接收两个参数

  第二步：判断这两个参数是都在1-100之间，如果在，将这两个数相加值保存，如果不在则提示输入错误

  第三步：调用函数

  ##### 参考答案

  ```python
def sum_random(m, n):
    if 1 <= m <= 100 and 1 <= n <= 100:
        print(m + n)
    else:
        print('输入错误!')
sum_random(1, 3)
  ```

### 题目5

  用函数实现一个判断用户输入的年份是否是闰年的程序，在函数中打印结果。


  ##### 训练提示

  1.能被400整除的年份
  2.能被4整除，但是不能被100整除的年份
  以上2种方法满足一种即为闰年

  ##### 参考答案

  ```python
def run_year_or_not(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year}年是闰年')
    else:
        print(f'{year}年不是闰年')
  ```

### 题目6

  定义一个函数，计算两个数之和。调用者在得到结果的时候需要判断是否大于20，如果大于则输出，超过10的加法太难了

  ##### 训练提示

  第一步：定义一个函数并接收两个参数

  第二步：对这两个参数进行相加

  第三步：判断相加的结果是否大于20，并输出结果

  ##### 参考答案

  ```python
def my_sum_again(a, b):
    if a + b > 20:
        print('超过10的加法太难了')
  ```

### 题目7

  定义一个函数cut_str，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1-1开始的a2个字符删除，并把结果返回

  例如：

  ```python
  s = "123456789", a1 = 2, a2 = 4 结果为: "16789"
  ```

  ##### 训练提示

  1、函数的定义

  2、函数的参数

  3、字符串的切割

  ##### 参考答案

  ```python
def cut_str(s: str, a1: int, a2: int):
    return s[:a1 - 1] + s[a1+a2 - 1:]
  ```

### 题目8

请定义两个函数，一个函数打印正方形，一个函数打印三角形，并且可以从键盘输入值来决定打印矩形还是打印三角形以及决定是否退出程序

##### 训练提示

1、函数的定义

2、函数的调用

3、逻辑判断以及循环

思路提示 ：定义两个函数，一个函数打印三角形，一个函数打印矩形，通过判断用户输入来决定调用哪个函数

##### 参考答案

```python
def print_triangle():
    print('''
    *
    **
    ***
    ****
    *****
    ''')


def print_square():
    print('''
    *****
    *****
    *****
    *****
    ''')


user_choice = int(input('打印三角形请输入1，打印矩形请输入2：'))
if user_choice == 1:
    print_triangle()
elif user_choice == 2:
    print_square()
else:
    print('您输入的有误！')
```

### 题目9

定义一个函数，这个函数需要接收的参数不确定多少个，请实现

##### 训练提示

python中有 args 参数可以接收不确定长度的参数

##### 参考答案

```python
def not_sure(*args):
    print(args)
not_sure(1, 2, 3, 4, 5)
```
