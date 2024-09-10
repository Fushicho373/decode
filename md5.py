import hashlib


def calculate_md5(input_string):
    md5_hash = hashlib.md5(input_string.encode())
    return md5_hash.hexdigest()

sign_1 = "ffabdaee7410f518776845d3e7b6d017"
symbol = "SSJ"
time = 1721979387
token_id = "10000001"

# 示例用法
input_string = f"token_id{token_id}symbol{symbol}time{time}actpass@2022"
sign = calculate_md5(input_string)
print(f"MD5哈希值: {sign}")
