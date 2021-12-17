# 如果不给while设置结束条件 就会产生死循环
i = 0

while i <= 10:
    print(i)
    i += 1

for i in range(11):
    print(i)

j = 1
result = 1
while j <= 30:
    if j % 2 == 0:
        print(f'{result} * {j} = {result * j}')
        result *= j

    j += 1
print(result)

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
i = 0
while i < 5:
    j = 0
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 1

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''
i = 0
while i < 5:
    j = 4
    while j >= i:
        print('*', end=' ')
        j -= 1
    print()
    i += 1

'''
      * 
    * * *
  * * * * * 
* * * * * * * 
'''
n = int(input("请输入您想打印的行数n："))
for i in range(n):
    print('  ' * (n - i - 1) + '* ' * (2 * i + 1))
