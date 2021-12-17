# 余额
money = int(input("请输入余额:"))

# 位置
if money > 2:
    print('上车了')

    # 在if判断中嵌套了一个 input()
    site = input("请输入有没有空位 yes/no")

    if site == "yes":
        print("坐下来了")
    else:
        print("站着")
 