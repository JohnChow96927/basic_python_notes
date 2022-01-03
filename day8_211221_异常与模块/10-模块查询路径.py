# 为什么,我们自己写的模块会覆盖系统模块呢???
import sys

print(sys.path)
# 这个path是一个列表,在导入模块时,会从这个列表中的路径中查询有没有对应的模块
# 从第一个开始查询,如果存在则使用该模块,如果不存在,则继续向下查找

# ['/Users/jizhengguo/Desktop/上海Python+大数据基础40期/day08/03-代码', # 文件所在目录
# '/Users/jizhengguo/Desktop/上海Python+大数据基础40期/day08/03-代码', # 工程目录
# '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
# '/Users/jizhengguo/Library/Python/3.8/lib/python/site-packages',
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages',
# '/Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend']