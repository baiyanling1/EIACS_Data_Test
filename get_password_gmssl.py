from gmssl import sm2, func, sm3

def sm2_encrypt(plaintext, sm2_pubkey_str):
    # 计算SM3摘要
    sm3_hash = sm3.sm3_hash(func.bytes_to_list(plaintext.encode('utf-8')))
    # sm3_digest = sm3_hash.encode('utf-8')
    sm3_digest = sm3_hash.encode('utf-8')

    # 将原始字符串和SM3摘要拼接起来
    plaintext_with_digest = plaintext + '##' + sm3_digest.hex()

    # SM2加密公钥
    sm2_pubkey = sm2.CryptSM2(public_key=bytes.fromhex(sm2_pubkey_str))

    # 使用SM2公钥加密原始字符串和SM3摘要的拼接结果
    encrypted_data = sm2_pubkey.encrypt(plaintext_with_digest.encode('utf-8'))

    return encrypted_data.hex()
if __name__ == '__main__':
    plaintext = 'hello world'
    sm2_pubkey_str = 'd9c07b1e2856875b5681de56306a459856b46859a754067c8d532a7f9b9cde9ecffbb87f9fe51660cc872c367edf1d3ff45125a6a221449ac18fc99de11ffc20'

    encrypted_data = sm2_encrypt(plaintext, sm2_pubkey_str)
    print('加密后的结果:', encrypted_data)