# 1.打开文件
# 追加操作打开文件时,不会讲源文件清空,在写入数据时,会在文本末尾进行追加
# file = open('gushi.txt', 'a', encoding='utf8')
# 如果被追加的文件不存在则新建一个文件
file = open('python.py', 'a', encoding='utf8')
# 2.追加文本
file.write('\n疑是地上霜')
# 3.关闭文件
file.close()

