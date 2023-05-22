import csv
import random
import datetime
import string
import time


def random_token():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(32))
def generate_id():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(16))

# def generate_imsi():
#     return '4600' + ''.join(random.choice('0123456789') for _ in range(10))
def generate_imsi():
    mcc = '460'
    mnc = ''.join(random.choice('0123456789') for _ in range(2))
    msin = ''.join(random.choice('0123456789') for _ in range(10))
    return mcc + mnc + msin

def generate_iccid():
    return '8986' + ''.join(random.choice('0123456789') for _ in range(14))

def generate_msisdn():
    return '86' + ''.join(random.choice('0123456789') for _ in range(11))

def generate_eid():
    return '80' + ''.join(random.choice('0123456789ABCDEF') for _ in range(14))

def generate_imei():
    return ''.join(random.choice('0123456789') for _ in range(15))

def generate_impu():
    return 'sip:' + ''.join(random.choice('0123456789') for _ in range(10)) + '@example.com'

def generate_impi():
    return ''.join(random.choice('0123456789') for _ in range(10))

def generate_province_code():
    return random.choice(['110000', '120000', '130000', '140000', '150000'])

def generate_eparchy_code():
    return random.choice(['110100', '120100', '130100', '140100', '150100'])

def generate_nickname():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))

def generate_sim_type():
    return random.choice([1, 2])

def generate_parent_imsi():
    return generate_imsi() if generate_sim_type() == 1 else None

def generate_companion_terminal_id():
    return ''.join(random.choice('0123456789') for _ in range(15))

def generate_activate_code():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

def generate_smdp_address():
    return 'https://' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)) + '.example.com/smdp'

def generate_create_at():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def generate_update_at():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def generate_imsi_update_at():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def generate_data(num,account_data_num):
    now = datetime.datetime.now()
    formatted_time = now.strftime('%Y%m%d%H%M%S')
    with open('/Users/hejian/Desktop/ES/STC升级验证/性能测试数据/auth_data_' + str(num/2) + '_' + str(
            formatted_time) + '.csv', mode='w', newline='') as auth_file, open('/Users/hejian/Desktop/ES/STC升级验证/性能测试数据/account_data_' + str(account_data_num) + '_' + str(
            formatted_time) + '.csv', mode='w', newline='') as account_file:
        writer = csv.writer(account_file)
        writer2 = csv.writer(auth_file)
        writer2.writerow(
            ['id', 'imsi', 'imei', 'token', 'msisdn', 'user_agent', 'interface_type', 'create_at', 'update_at'])
        writer.writerow(['id', 'imsi', 'iccid', 'msisdn', 'eid', 'imei', 'impu', 'impi', 'province_code', 'eparchy_code', 'nickname', 'sim_type', 'parent_imsi', 'attach_sim_status', 'terminal_type', 'companion_terminal_id', 'activate_code', 'smdp_address', 'create_at', 'update_at', 'imsi_update_at'])

        parent_imsi = None
        for i in range(num):
            sim_type = 1 if i % 2 != 0 else 2
            imsi = generate_imsi()
            msisdn = generate_msisdn()
            if sim_type == 1:
                parent_imsi = imsi
                writer2.writerow([
                    str(i),
                    imsi,
                    '',
                    random_token(),
                    msisdn,
                    '',
                    'APPLE',
                    generate_create_at(),
                    generate_update_at()
                ])
            if i< account_data_num:
                writer.writerow([
                    str(i),
                    imsi,
                    generate_iccid(),
                    msisdn,
                    generate_eid() if sim_type == 2 else None,
                    generate_imei() if sim_type == 2 else None,
                    'SIP:+8613888800000@Huawei.com' if sim_type == 2 else 'CQ',
                    'SIP:460080000000001@Huawei.com' if sim_type == 2 else '83',
                    '',
                    '',
                    generate_nickname() if sim_type == 2 else None,
                    sim_type,
                    parent_imsi if sim_type == 2 else None,
                    random.choice(["ACTIVE", "INACTIVE"]) if sim_type == 2 else None,
                    'ipad' if sim_type == 2 else '',
                    '',
                    '',
                    '',
                    generate_create_at(),
                    generate_update_at(),
                    generate_imsi_update_at()
                ])

if __name__ == '__main__':
    print(generate_imsi())
    time_start = time.time()
    print("start time: ", time.strftime('%Y-%m-%d %H:%M:%S'))
    #auth_num为需要生成的auth_data数据数据量，account_num为需要生成的account_data数据量
    auth_num=450000
    account_num=30000
    generate_data(auth_num*2, account_num)
    time_end = time.time()
    print("finish time: ", time.strftime('%Y-%m-%d %H:%M:%S'))
    print("cost time: ", time_end - time_start)