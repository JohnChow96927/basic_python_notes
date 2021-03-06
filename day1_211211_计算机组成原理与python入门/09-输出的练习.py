'''
义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！

定义整数变量 student_no ，输出 我的学号是 000001

定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元

定义⼀个⼩数 scale ，输出 数据⽐例是 10.00%

编写代码完成以下名片的显示

    ==========我的名片==========
    姓名: itheima
    QQ:xxxxxxx
    手机号:185xxxxxx
    公司地址:北京市xxxx
    ===========================

'''

# 义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！
name = '小明'
print(f'我叫{name},请多多关照')

# 定义整数变量 student_no ，输出 我的学号是 000001

student_no = 1
print('我的学号是%06d' % student_no)

# 定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元
price = 9.00
weight = 5.00
money = price * weight
print(F'苹果单价 {price:.2f} 元／⽄，购买了 {weight:.2f} ⽄，需要⽀付 {money:.2f} 元')

# 定义⼀个⼩数 scale ，输出 数据⽐例是 10.00%
scale = 10.00
# ValueError: incomplete format
# 在字符格式化时,如果使用的是%拼接,则在前边的字符串内不能出现单独的%,系统会认为是占位符,并且没有写完整
# 如果想要输出% 则使用% 对%进行转译
# print('数据⽐例是%.2f%' % scale)
print('数据⽐例是%.2f%%' % scale)
# 不能使用反斜杠转译%
# print('数据⽐例是%.2f\%' % scale)
# 如果在字符串后边没有%进行字符串拼接,则在字符串中可以随意使用%
print('数据⽐例是 10.00%')

# 编写代码完成以下名片的显示
#
    # ==========我的名片==========
    # 姓名: itheima
    # QQ:xxxxxxx
    # 手机号:185xxxxxx
    # 公司地址:北京市xxxx
    # ===========================

name = 'xiaoming'
QQ_num = 123321
phone_num = 13733723456
address = '北京市海淀区'

print(f'==========我的名片==========\n'
      f'姓名: {name}\n'
      f'QQ:{QQ_num}\n'
      f'手机号:{phone_num}\n'
      f'公司地址:{address}\n'
      f'===========================' )

#扩展 输出字符串可以使用三对引号,引号内部可以换行,换行效果保留
# 在三对引号中换行,输出结果也会换行 同时使用一个f可以修饰多行
print(
    f'''
    ==========我的名片==========
    姓名: {name}
    QQ:{QQ_num}
    手机号:{phone_num}
    公司地址:{address}
    ===========================
'''
)