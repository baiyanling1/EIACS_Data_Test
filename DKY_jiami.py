import hashlib
from gmssl import sm2, func


plaintext=b'hello'
plaintext = 'Hello, world!'
message_bytes = plaintext.encode('utf-8')
hash_obj = hashlib.new('sm3')
hash_obj.update(message_bytes)
hash_value = hash_obj.digest()
plaintext_with_digest = plaintext + '##' + hash_value.hex()
print(plaintext_with_digest)
plaintext_with_digest=plaintext_with_digest.encode()
sm2_pubkey_str = 'd9c07b1e2856875b5681de56306a459856b46859a754067c8d532a7f9b9cde9ecffbb87f9fe51660cc872c367edf1d3ff45125a6a221449ac18fc99de11ffc20'

sm2_crypt=sm2.CryptSM2(private_key='',public_key=sm2_pubkey_str)
ciphertext= sm2_crypt.encrypt(plaintext_with_digest)
print('Ciphertext:', ciphertext.hex())