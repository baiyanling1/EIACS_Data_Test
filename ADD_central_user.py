import base64
import hashlib
import json
import random
import csv
import time
import uuid

import Crypto
import requests
import redis

import warnings
import requests
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# 禁用警告
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

pre_token='b48fbb06d6a314db02e8a9bb7ff4c635e0bb33e388e4dd021fcb68ba6fd7ebdd'
REDIS_IP='10.18.40.20'
REDIS_PORT=6379
REDIS_PWD='redtea.123'

avatar="data:image/png;base64,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"
# 生成随机用户名
def random_username():
    prefix = ['happy', 'lucky', 'cool', 'crazy', 'funny', 'smart', 'smooth', 'wild', 'zealous', 'brave', 'bright', 'calm', 'clever', 'daring', 'dynamic', 'eager', 'fierce', 'gentle', 'graceful', 'honest', 'humble', 'jolly', 'kind', 'loyal', 'merry', 'noble', 'polite', 'proud', 'quick', 'quiet', 'rich', 'silly', 'sincere', 'strong', 'sunny', 'sweet', 'tender', 'tough', 'vivid', 'warm', 'wise', 'witty', 'wonderful', 'young', 'zesty']
    suffix = ['cat', 'dog', 'monkey', 'tiger', 'lion', 'panda', 'bear', 'fox', 'wolf', 'bird', 'deer', 'elephant', 'giraffe', 'horse', 'kangaroo', 'leopard', 'otter', 'rabbit', 'squirrel', 'zebra', 'crocodile', 'dolphin', 'fish', 'octopus', 'shark', 'turtle', 'whale', 'butterfly', 'dragonfly', 'eagle', 'falcon', 'hawk', 'owl', 'parrot', 'peacock', 'penguin', 'swan', 'bee', 'ant', 'butterfly', 'caterpillar', 'spider', 'worm', 'snail', 'ladybug']
    return random.choice(prefix) + random.choice(suffix)

# 生成随机手机号
def random_phone():
    prefix = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '153', '155', '156', '157', '158', '159', '166', '170', '171', '173', '175', '176', '177', '178', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '198', '199']
    return random.choice(prefix) + ''.join(random.choice('0123456789') for i in range(8))

# 生成随机邮箱地址
def random_email():
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'icloud.com']
    username = random_username() + str(random.randint(1, 100))
    return username + '@' + random.choice(domain)



def encrypt_password(password: bytes, public_key: str) -> str:
    # 将公钥字符串解析为公钥对象
    public_key_obj = RSA.import_key(public_key)

    # 使用公钥加密密码
    cipher = PKCS1_OAEP.new(public_key_obj)
    encrypted_password = cipher.encrypt(password)

    # 将加密后的密码转换为十六进制字符串并返回
    return encrypted_password.hex()

def ADD_Central_User(num):
    headers = {
        "request-id": str(uuid.uuid4()),
        "timestamp": str(int(time.time())),
        "Sign-Method": "SHA256",
        "Signature": "wweew",
        "Access-Key": "wwwww",
        "token": pre_token,
        "content-type": "application/json"
    }
    for i in range(0, num):
        username = random_username()
        phone = random_phone()
        email = random_email()
        rquest_url = 'https://10.18.40.20:39443/rest/er/mgmt-gateway/api/v1/user/add'
        data = {
            "username":username,
            "avatar":avatar,
            "address":"",
            "nickName":"",
            "mobile":phone,
            "email":email,
            "roleId":8,
            "description":""
        }
        response = requests.post(rquest_url, json=data,headers=headers, verify=False)
        # data = response.json()
        print(response.content)
        print(response.status_code)
        print("用户创建成功："+ username)
        return data['data']['id']

def Get_PK():
    headers = {
        "request-id": str(uuid.uuid4()),
        "timestamp": str(int(time.time())),
        "Sign-Method":"SHA256",
        "Signature":"wweew",
        "Access-Key":"wwwww"
    }
    get_pk_url = "https://10.18.40.20:39443/rest/er/mgmt-gateway/api/v1/security/getPk"
    response = requests.get(get_pk_url, headers=headers, verify=False)
    data = response.json()
    # print(data['data']['pk'])
    # print(data['data']['alias'])
    return data['data']['alias'],data['data']['pk']
def Resetpassword(id):
    headers = {
        "request-id": str(uuid.uuid4()),
        "timestamp": str(int(time.time())),
        "Sign-Method": "SHA256",
        "Signature": "wweew",
        "Access-Key": "wwwww",
        "token": pre_token,
        "content-type": "application/json"
    }
    data ={"userId":id}
    modifyPass_url = "https://10.18.40.20:39443/rest/er/mgmt-gateway/api/v1/user/resetLowerUserPassword"
    response = requests.post(modifyPass_url, json=data, headers=headers, verify=False)
    data = response.json()
    return data['data']['token']
def encrypt_rsa(public_key_str, password):
    # 从公钥字符串中加载公钥
    pk_pkcs1 = "\n".join(["-----BEGIN PUBLIC KEY-----",public_key_str, "-----END PUBLIC KEY-----"])
    rsakey = RSA.importKey(pk_pkcs1)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    newPassword = base64.b64encode(cipher.encrypt(str.encode(password))).decode('utf-8')
    # 返回加密结果
    return newPassword

def modifyPassWithoutOld(alias,token):
    headers = {
        "request-id": str(uuid.uuid4()),
        "timestamp": str(int(time.time())),
        "Sign-Method": "SHA256",
        "Signature": "wweew",
        "Access-Key": "wwwww",
        "token": token,
        "content-type": "application/json"
    }
    newPassword=encrypt_rsa(alias[1],'Redtea@123')
    # pk_pkcs1 = "\n".join(["-----BEGIN PUBLIC KEY-----", alias[1], "-----END PUBLIC KEY-----"])
    # rsakey = RSA.importKey(pk_pkcs1)
    # cipher = Cipher_pkcs1_v1_5.new(rsakey)
    # newPassword = base64.b64encode(cipher.encrypt(str.encode('Redtea@123'))).decode('utf-8')

    data={"alias":alias[0],"token":token,"newPassword":newPassword}
    json_data = json.dumps(data)
    modifyPass_url = "https://10.18.40.20:39443/rest/er/mgmt-gateway/api/v1/user/modifyPassWithoutOld"
    response = requests.post(modifyPass_url, data=json_data, headers=headers, verify=False)
    return response.status_code
def GET_token_redis(username):
    client = redis.Redis(host=REDIS_IP, port=REDIS_PORT, password=REDIS_PWD, db=1)
    # 构建键名
    key = f'TOKEN_CACHE_BY_USERNAME#{username}'
    # 获取键的值
    value = client.get(key)
    string_data = value.decode('utf-8')
    print(string_data)
    return string_data


def ADD_Central_User_modifyPassWithoutOld(num):

    for i in range(0,num):
        username = random_username()
        phone = random_phone()
        email = random_email()
        rquest_url = 'https://10.18.40.20:39443/rest/er/mgmt-gateway/api/v1/user/add'
        headers = {
            "request-id": str(uuid.uuid4()),
            "timestamp": str(int(time.time())),
            "Sign-Method": "SHA256",
            "Signature": "wweew",
            "Access-Key": "wwwww",
            "token": pre_token
        }
        data = {
                "username":username,
                "avatar":avatar,
                "address":"",
                "nickName":"",
                "mobile":phone,
                "email":email,
                "roleId":8,
                "description":""
        }
        response = requests.post(rquest_url, json=data,  headers=headers, verify=False)
        print("用户" + username + "创建成功，初始化状态")
        token = GET_token_redis(username)
        alias = Get_PK()
        code=modifyPassWithoutOld(alias, token)
        print("用户"+ username+"秘密重置成功，返回结果"+str(code))
        time.sleep(1)

if __name__ == '__main__':
    # 生成100条数据
    #ADD_Central_User 添加user返回id
    #通过redis获取token
    #Get_PK 获取公钥alias
    #modifyPassWithoutOld(alias,token)重置密码成功
    ADD_Central_User_modifyPassWithoutOld(100)
    # Resetpassword("57")
    # ADD_Central_User(1)
    # public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAi9QuRSQ4KPfkwtByuVEaF024JtnLEcIGo5vMVrJkP3G6zL0fuxkGkuK9QneAXSB+am87PWLjAM+XpsEiRQ0KIgcchOAcP3JoqWMi/n3vn+jrkLU/RrQ9ErEEGnenA/6kf9E8H2v9W/fSAEMqX5ohhphR3inOtWnSacItBD0xk+8SayMIcNNGFRxbJc19ZEYAZMdOY/nVfHEm9Bu57DUctmbk7nORM7yDO5PndVg5dSHgjy4Ns4pXopKcF/O9vwEesk4DVLwf02Dmt1QqNTymj6JupSAUuCo5IS6o47PaeGIpfo35AHC0EnZ+xLqQfr6KQzGF0xrPF5Xqctah9kFNPwIDAQAB"
    # public_key_bytes = base64.b64decode(public_key)
    # print(encrypt_password(b'Redtea@123',public_key_bytes))
