age = 0
# 且 and : 多个条件同时成立
if (age >= 18) and (age < 50) and (age != 44):
    print("喜相逢")

# 或 or : 多个条件只要有一个成立即可
if age == 23 or age == 33 or age == 43:
    print("喜相逢")

# not 取反:
if not age >= 18:
    print("喜相逢")
