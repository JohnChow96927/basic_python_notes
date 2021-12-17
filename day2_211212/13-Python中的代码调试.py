# bug:计算机中出现的程序错误
# 常见的bug
# NameError: name 'a' is not defined
# print(a)

# TypeError: can only concatenate str (not "int") to str
# print('1' + 2)

# IndentationError: unexpected indent
# if True:
#     print(1)
#         print(2)

# SyntaxError: unexpected EOF while parsing
# print('abc'

# ZeroDivisionError: division by zero
# print(1 / 0)

# 在Pycharm中给我们提供了一种debug模式用于调试代码
# 我们可以在代码中打断点,打断点后,我们使用debug模式调试代码时,代码会停滞在断点代码执行之前
# step over  向下执行一行


print('hello chuanzhi')
print('hello bigdata')
print('hello python')


i = 0
while i < 5:
    j = 0
    while j < 5-i:
        print('*', end=' ')
        j += 1
    print()
    i += 1
