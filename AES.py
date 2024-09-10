from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# 给定的加密数据
data = '2012cdee703fd95b811751ddbe91d1fd72292a807b0b19c62e980f0401a6a29a'


# 固定的密钥和 IV（这里的 IV 是假设的值，实际上应该从加密数据中提取）
def decode(info):
    data = binascii.unhexlify(info)
    # 提取 IV 和加密数据
    iv = data[:AES.block_size]
    encrypted = data[AES.block_size:]

    # 从 Authorization 提取密钥
    decodeKey = 'ae26fe5b4ce38925e6f13a7167fed3ea'[:16]
    key = decodeKey.encode('utf-8')

    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
        return decrypted.decode('utf-8')
    except ValueError:
        return "Padding is incorrect or data is corrupted."


# 测试解密
decoded_info = decode(data)
print(f"Decoded info: {decoded_info}")
