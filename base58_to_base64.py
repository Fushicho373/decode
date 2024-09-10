import base64
import base58

def base58_to_base64(base58_str):
    # 解码Base58编码的字符串为二进制数据
    decoded_bytes = base58.b58decode(base58_str)
    # 将二进制数据编码为Base64编码的字符串
    base64_str = base64.b64encode(decoded_bytes)
    return base64_str.decode('utf-8')  # 返回解码的字符串

# 示例
base58_encoded_str = "Lqr7x56LhN3YFGo8i7C1M536iNUE3KMNz"
base64_encoded_str = base58_to_base64(base58_encoded_str)
print("原Base58:", base58_encoded_str)
print("转Base64:", base64_encoded_str)