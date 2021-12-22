# 方法六: import 包名
import demo

# 直接导入包,如果有__all__ 则可以使用其中的所有模块

# 直接导入包会运行__init__中的代码,所以在__init__中导入的模块,在import 报名时也能使用

demo.func1()