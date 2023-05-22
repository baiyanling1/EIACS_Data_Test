import csv
import random
import string
import datetime

# 生成随机字符串
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# 生成随机IMSI
def random_imsi():
    mcc = random.choice(['460']) # 中国移动国家码
    mnc = random.choice(['00', '01', '02', '03', '05', '06']) # 移动网络码
    msin = ''.join(random.choice(string.digits) for i in range(10)) # 移动用户识别码
    return mcc + mnc + msin

# 生成随机IMEI
def random_imei():
    tac = '86' + ''.join(random.choice(string.digits) for i in range(6)) # 型号核准号码
    sn = ''.join(random.choice(string.digits) for i in range(6)) # 序列号
    cd = ''.join(random.choice(string.digits) for i in range(1)) # 校验位
    return tac + sn + cd

# 生成随机Token
def random_token():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(32))

# 生成随机MSISDN
def random_msisdn():
    prefix = random.choice(['130', '131', '132', '133', '134', '135', '136', '137', '138', '139']) # 手机号码前缀
    return prefix + ''.join(random.choice(string.digits) for i in range(8))

# 固定Interface Type为"APPLE"
def fixed_interface_type():
    return "APPLE"

# 固定User Agent为空字符串
def fixed_user_agent():
    return ""

# 生成随机创建时间
def random_create_at():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# 生成随机更新时间
def random_update_at():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def get_auth_data(num):
    # 生成数据并写入CSV文件
    now = datetime.datetime.now()
    formatted_time = now.strftime('%Y%m%d%H%M%S')
    with open('/Users/hejian/Desktop/ES/STC升级验证/性能测试数据/auth_data_'+str(num) +'_'+ str(
            formatted_time) + '.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['id', 'imsi', 'imei', 'token', 'msisdn', 'user_agent', 'interface_type', 'create_at', 'update_at'])
        for i in range(num):
            writer.writerow([
                i + 1,
                random_imsi(),
                random_imei(),
                random_token(),
                random_msisdn(),
                fixed_user_agent(),
                fixed_interface_type(),
                random_create_at(),
                random_update_at()
            ])
if __name__ == '__main__':
   get_auth_data(450000)