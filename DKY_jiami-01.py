import binascii
import datetime

# 导入国密算法sm4包
from gmssl import sm4, sm3, sm2, func
import pandas as pd

def sm3_hash(message: bytes):
    """
    国密sm3加密
    :param message: 消息值，bytes类型
    :return: 哈希值
    """

    msg_list = [i for i in message]
    hash_hex = sm3.sm3_hash(msg_list)
    # print(hash_hex)
    return hash_hex

    # bytes2hex(hash_hex);

    # hash_bytes = bytes.fromhex(hash_hex)
    # print(hash_bytes)

    # return bytes.hash
    # return hash


def bytes2hex(bytesData):
    hex = binascii.hexlify(bytesData)
    print(hex)
    print(hex.decode())
    return hex

def SM2_encrypt(data):
    message = data.encode()
    sm3_sig = sm3_hash(message)
    print("sm3计算摘要的结果：", sm3_sig)

    # 拼接原始数据和摘要
    sm2_text = data + "##" + sm3_sig
    print("拼接结果：", sm2_text)
    public_key_str = 'd9c07b1e2856875b5681de56306a459856b46859a754067c8d532a7f9b9cde9ecffbb87f9fe51660cc872c367edf1d3ff45125a6a221449ac18fc99de11ffc20'

    sm2_crypt = sm2.CryptSM2(public_key=public_key_str, private_key='464364564564645646456', mode=1, asn1=True)
    # print(sm2_crypt.public_key)
    result = sm2_crypt.encrypt(sm2_text.encode('utf-8'))

    print("最终结果：", '04' + result.hex().upper())
    return '04' + result.hex().upper()

# main
if __name__ == '__main__':
    ##########传入原始文件，生成加密后的文件####################
    print("main begin");
    now = datetime.datetime.now()
    formatted_time = now.strftime('%Y%m%d%H%M%S')
    #需要加密的原始文件路径
    df = pd.read_csv('/Users/hejian/Downloads/电力5G综合管控平台_1685090995187_码号录入.csv')

    df['ki'] = df['ki'].apply(lambda x: SM2_encrypt(x))
    df['opc'] = df['opc'].apply(lambda x: SM2_encrypt(x))
    #保存加密后的文件为新的文件
    df.to_csv('/Users/hejian/Downloads/SM2_encrypt_output-'+ str(
        formatted_time) +'.csv', index=False)
    ##之后给平台导入新的文件即可

    #########传入要加密的值data，打印加密后的结果############
    # data='00000000000000000000004863976BE0'
    # SM2_encrypt(data)
    ###########################################