try:
    score = int(input("请输入您的得分："))
    if 100 >= score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 70:
        print("中等")
    elif score >= 60:
        print("合格")
    elif score >= 0:
        print("不及格")
    else:
        print("你输入的分数有误")
except ValueError as e:
    print("您输入的内容有误，请输入一个数字！" + str(e))


