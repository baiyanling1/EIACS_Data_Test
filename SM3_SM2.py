from Crypto.Hash import SM3
from Crypto.Hash import MD2
from Crypto.PublicKey import SM2
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad


# import sys
# sys.path.append('/usr/local/Cellar/openssl@3/3.1.0')
print("kdkd")
# 待加密的字符串
plaintext = 'hello world'

# 计算SM3摘要
sm3_hash = SM3.new()
sm3_hash.update(plaintext.encode('utf-8'))
sm3_digest = sm3_hash.digest()

# 将原始字符串和SM3摘要拼接起来
plaintext_with_digest = plaintext + '##' + sm3_digest.hex()

# SM2加密公钥
sm2_pubkey_str = 'd9c07b1e2856875b56'
from Crypto.Hash import MD2
from Crypto.PublicKey import SM2
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SM3
from Crypto.Util.Padding import pad, unpad


# import sys
# sys.path.append('/usr/local/Cellar/openssl@3/3.1.0')
print("kdkd")
# 待加密的字符串
plaintext = 'hello world'

# 计算SM3摘要
sm3_hash = SM3.new()
sm3_hash.update(plaintext.encode('utf-8'))
sm3_digest = sm3_hash.digest()

# 将原始字符串和SM3摘要拼接起来
plaintext_with_digest = plaintext + '##' + sm3_digest.hex()

# SM2加密公钥
sm2_pubkey_str = 'd9c07b1e2856875b5681de56306a459856b46859a754067c8d532a7f9b9cde9ecffbb87f9fe51660cc872c367edf1d3ff45125a6a221449ac18fc99de11ffc20'
sm2_pubkey_bytes = bytes.fromhex(sm2_pubkey_str)
sm2_pubkey = SM2.import_key(sm2_pubkey_bytes)

# 使用SM2公钥加密原始字符串和SM3摘要的拼接结果
cipher = PKCS1_OAEP.new(sm2_pubkey)
encrypted_data = cipher.encrypt(plaintext_with_digest.encode('utf-8'))

print('加密后的结果:', encrypted_data.hex())
sm2_pubkey_bytes = bytes.fromhex(sm2_pubkey_str)
sm2_pubkey = SM2.import_key(sm2_pubkey_bytes)

# 使用SM2公钥加密原始字符串和SM3摘要的拼接结果
cipher = PKCS1_OAEP.new(sm2_pubkey)
encrypted_data = cipher.encrypt(plaintext_with_digest.encode('utf-8'))

print('加密后的结果:', encrypted_data.hex())