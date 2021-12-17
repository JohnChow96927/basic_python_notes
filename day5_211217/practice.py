def print_triangle(n: int):
    result = 0
    for i in range(1, n + 1):
        result += i
        print('*' * i)
    return result


n = int(input('请输入打印行数：'))
print(print_triangle(n))
