import random

# 全国区域代码
AREA_CODES = ['11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
             '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '81', '82', '83']

# 闰年和非闰年的每个月的天数
DAYS_IN_MONTH = {
    True: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    False: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
}

def generate_id_number():
    # 随机生成身份证号码
    str_id = []
    province_code = random.choice(AREA_CODES)
    city_code = str(random.randint(1000, 9999))
    year = str(random.randint(1950, 2010))
    month = str(random.randint(1, 12)).zfill(2)
    days = str(random.randint(1, DAYS_IN_MONTH[is_leap_year(int(year))][int(month) - 1])).zfill(2)
    rand_num = str(random.randint(100, 999)).zfill(3)
    check_num = generate_check_digit(province_code + city_code + year + month + days + rand_num)

    # 拼接身份证号码并返回
    str_id.append(province_code)
    str_id.append(city_code)
    str_id.append(year)
    str_id.append(month)
    str_id.append(days)
    str_id.append(rand_num)
    str_id.append(check_num)
    return ''.join(str_id)

def is_leap_year(year):
    # 判断是否为闰年
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def generate_check_digit(id_number):
    # 生成身份证号码的校验码
    weight_factors = [int(x) for x in '7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2'.split()]
    check_codes = '10X98765432'
    sum = 0
    for i in range(len(id_number)):
        sum += int(id_number[i]) * weight_factors[i]
    return check_codes[sum % 11]