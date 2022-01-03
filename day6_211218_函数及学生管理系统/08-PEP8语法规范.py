# 缩进最好是4的正数倍
# if 1 < 2:
#   print('123')
#   print('data')

# 每一行限定在79个字符以内
# 超过79个字符可以进行换行
# 字符串可以随意换行
print('hello Python  hell world  hell bigdata '
      'hello Python  hell world  hell bigdata hello'
      ' Python  hell world  hell bigdata')

# 代码中可以直接换行,但是在换行末尾会增加一个转义字符,证明和下方是同一行代码
# 或者可以将超长代码用括号包裹起来,此时可以随意换行,但是不能拆分变量或单词短语
a = 1
b = 2
if a > 1 and b < 2 and b < 2 and b < 2 and b < 2 and \
        b < 2 and b < 2 and b < 2 and b < 2 and b < 2 and \
        b < 2 and b < 2 and b < 2 and b < 2 and b < 2 and b < 2:
    print('123')

if (a > 1 and b < 2
        and b < 2 and b < 2 and
        b < 2 and b < 2 and b < 2 and
        b < 2 and b < 2 and b < 2 and b
        < 2 and b < 2 and b < 2 and b < 2 and b < 2 and b < 2):
    print('123')

if a == 1:
    print(123)
