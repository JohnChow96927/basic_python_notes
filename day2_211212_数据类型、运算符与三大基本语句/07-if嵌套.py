ticket = 1  # 用1代表有车票，0代表没有车票
seat = 0  # 用1代表有座位,用0代表没有座位

if ticket == 1:
    print('赶紧上车吧,大哥,里边有大座')
    if seat == 1:
        print('赶紧坐下不然被人占了')
    else:
        print('别坐啦,马上到站了')
else:
    print('跟着车跑吧,穷鬼!')


if ticket == 1 and seat == 1:
    print('赶紧上车吧,大哥,里边有大座')
    print('赶紧坐下不然被人占了')
elif ticket == 1 and seat == 0:
    print('赶紧上车吧,大哥,里边有大座')
    print('别坐啦,马上到站了')
else:
    print('跟着车跑吧,穷鬼!')

# 建议: 没有if嵌套,也能使用分支语句解决上述问题,但是,通过if嵌套让逻辑简化了
# if嵌套可以将复杂的判断逻辑,简化为及格简单的判断逻辑