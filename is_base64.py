import base64

def is_base64(s):
    try:
        base64.b64decode(s)
        return True
    except base64.binascii.Error:
        return False

# 示例
encoded_str = "Ek6G8c6n7HmBVfbjhU5HpwJdkiuAeU44ZghYj5MaNFM="
if is_base64(encoded_str):
    print("The string is Base64 encoded.")
else:
    print("The string is not Base64 encoded.")
