import base64
import binascii

def base64_to_hex(base64_data):
    # 解码 Base64 数据
    binary_data = base64.b64decode(base64_data)
    # 将二进制数据转换为十六进制字符串
    hex_string = binascii.hexlify(binary_data)
    return hex_string.decode('utf-8')  # 返回十六进制字符串

# 示例输入
base64_data = "2adb9a3d-a019-4a2c-88f1-043e049ff84b"  # Base64 编码的数据
hex_data = base64_to_hex(base64_data)
print("转换后的十六进制数据:", hex_data)
