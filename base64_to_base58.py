import base64
import base58

def base64_to_base58(base64_str):
    # 解码Base64编码的字符串为二进制数据
    decoded_bytes = base64.b64decode(base64_str)
    # 将二进制数据编码为Base58编码的字符串
    base58_str = base58.b58encode(decoded_bytes)
    return base58_str.decode('utf-8')  # 返回解码的字符串

# 示例
base64_encoded_str = "2adb9a3d-a019-4a2c-88f1-043e049ff84b"
base58_encoded_str = base64_to_base58(base64_encoded_str)
print("原Base64 encoded string:", base64_encoded_str)
print("转Converted to Base58:", base58_encoded_str)
