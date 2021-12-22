# 文件的读取

# file = open('gushi.txt', 'r', encoding='utf8')
#
# print(file.read())
#
# # io.UnsupportedOperation: not writable
# # r模式是只读模式,不能进行写入操作
# file.write('\n举头望明月')
#
# file.close()


file = open('gushi.txt', 'r+', encoding='utf8')
# 一般我们不要这样使用,因为涉及游标seek问题
file.write('\n举头望明月')

print(file.read())

file.close()

