price = input("请输入单价:")
weight = input("请输入重量:")

price = int(price)
weight = int(weight)

money = price * weight
print(f"苹果单价{price}元／⽄，购买了{weight}⽄，需要⽀付{money}元")
