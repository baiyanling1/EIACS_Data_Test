import gmssl
from gmssl import sm2, func, sm3
import binascii

def sm2_encrypt(message, sm2_pubkey_str):
    # 使用SM3计算字符串摘要
    sm3_hash = gmssl.sm3.sm3_hash(bytes(message, encoding="utf8"))

    # 将字符串和摘要进行拼接
    data = message + "##" + sm3_hash

    # 将SM2公钥转换为gmssl库的对象
    sm2_pubkey = gmssl.sm2.PublicKey.from_public_bytes(bytes.fromhex(sm2_pubkey_str))

    # 使用SM2公钥对拼接后的字符串进行加密
    cipher_text = sm2_pubkey.encrypt(bytes(data, encoding="utf8"))

    # 将加密结果转换为十六进制字符串并返回
    return binascii.hexlify(cipher_text).decode("utf8")
message = "Hello World"
sm2_pubkey_str = "d9c07b1e2856875b5681de56306a459856b46859a754067c8d532a7f9b9cde9ecffbb87f9fe51660cc872c367edf1d3ff45125a6a221449ac18fc99de11ffc20"
cipher_text = sm2_encrypt(message, sm2_pubkey_str)
print(cipher_text)