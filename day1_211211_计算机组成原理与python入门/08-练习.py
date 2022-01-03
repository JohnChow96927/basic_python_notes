# 1. 定义字符串变量 name ，输出 我的名字叫 ⼩明，请多多关照！
name = "小明"
print("我的名字叫%s,请多多关照!" % name)

# 2. 定义整数变量 student_no ，输出 我的学号是 000001
student_no = "000001"
print("我的学号是%s" % student_no)
student_no = 1
print("我的学号是%06d" % student_no)

# 3. 定义⼩数 price 、 weight 、 money ，输出 苹果单价 9.00 元／⽄，购买了 5.00 ⽄，需要⽀付 45.00 元
price = 9.00
weight = 5.00
money = 45.00
print("苹果单价 %.2f 元／⽄，购买了 %.2f ⽄，需要⽀付 %.2f 元" % (price, weight, money))

# 4. 定义⼀个⼩数 scale ，输出 数据⽐例是 10.00%
scale = 10.00
print("数据⽐例是 %.2f%%" % scale)
scale = 10.00
print("数据⽐例是 %.2f" % scale, end="\n")


# ==========我的名片==========
# 姓名: itheima
# QQ:xxxxxxx
# 手机号:185xxxxxx
# 公司地址:北京市xxxx
# ===========================
name = 'John'
qq = '312649598'
cell_phone = '13333323333'
co_address = '南京市长江大桥'
print(f"==========我的名片========== \n姓名:{name}\nQQ:{qq} \n手机号:{cell_phone} \n公司地址:{co_address} \n=========================== ")

