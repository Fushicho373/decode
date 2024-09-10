import base58

def is_base58(s):
    try:
        base58.b58decode_check(s)
        return True
    except ValueError:
        return False

# 示例
encoded_str = "ipBwJo/PG1+NDiIc8MJxabcdjGReqAxzxF40QZlIe5MveOUY7PQ/Mfzk4qg6jqUM3vS/sDlsWN9Ei8Kkq5uXCg=="
if is_base58(encoded_str):
    print("The string is Base58 encoded.")
else:
    print("The string is not Base58 encoded.")

