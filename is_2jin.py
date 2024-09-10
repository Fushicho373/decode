def is_binary(data):
    # 判断是否包含不可打印字符
    for char in data:
        if char < ' ' or char > '~':
            return True
    return False

# 示例输入
input_data = "0x8a3faaf776ac77ae28f56b12589be2ef11885680"  # 输入文本数据
if is_binary(input_data):
    print("输入数据是二进制数据")
else:
    print("输入数据不是二进制数据")
