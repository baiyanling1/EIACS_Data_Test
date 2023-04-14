import random
import string

import requests


serviceTypes=['SIGN;AUTH', 'SIGN;AUTH;CONTROL', 'AUTH;CONTROL']
def get_location(address, api_key):
    url = "https://restapi.amap.com/v3/geocode/geo"
    params = {
        "key": api_key,
        "address": address
    }
    response = requests.get(url, params=params)
    data = response.json()
    location = data["geocodes"][0]["location"]
    longitude, latitude = location.split(",")

    # 将经纬度转换成度、分、秒的形式
    degree_l = int(float(longitude))
    minute_l = int((float(longitude) - degree_l) * 60)
    second_l = round(((float(longitude) - degree_l) * 60 - minute_l) * 60, 2)

    degree_w = int(float(latitude))
    minute_w = int((float(latitude) - degree_w) * 60)
    second_w = round(((float(latitude) - degree_w) * 60 - minute_w) * 60, 2)

    # 将经纬度格式化成"北纬/东经：XX度XX分XX秒"的形式
    lng_str = "东经：{}度{}分{:.2f}秒".format(degree_l, minute_l, second_l)
    lat_str = "北纬：{}度{}分{:.2f}秒".format(degree_w, minute_w, second_w)
    return (lng_str, lat_str)

#获取随机URL
def generate_random_url():
    letters = string.ascii_lowercase
    url = "http://"
    for i in range(10):
        url += random.choice(letters)
    url += ".com"
    return url
#获取随机省份
def generate_random_province():
    provinces = ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省', '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省', '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区']
    return random.choice(provinces)
#随机生成企业名称
def generate_random_university_name():
    first_words = ['北京', '清华', '复旦', '浙江', '南京', '武汉', '华中', '中南', '东南', '南开', '上海', '同济', '交通', '中山', '厦门', '山东', '西安', '电子', '哈尔滨', '吉林', '东北', '湖南', '湖北', '四川', '西南', '华南', '广东', '海南', '西北', '兰州', '青海', '宁夏', '新疆', '内蒙古', '河北', '河南', '辽宁', '安徽', '江苏', '江西', '福建', '广西', '贵州', '云南', '北京航空航天大学', '北京理工大学', '北京大学', '中国人民大学', '中国科学技术大学', '南京大学', '浙江大学', '上海交通大学', '复旦大学', '武汉大学']
    second_words = ['大学', '工业大学', '师范大学', '医科大学', '理工大学', '农业大学', '林业大学', '财经大学', '政法大学', '外国语大学', '艺术学院', '音乐学院', '体育学院', '航空航天学院', '海洋学院', '石油化工学院', '交通学院', '电子科技学院', '信息工程学院']
    return random.choice(first_words) + random.choice(second_words)

#调取接口注册企业
def register_enterprise(num):
    api_key = "883a45c1d6f12398498f4d53b4f306f9"
    address = generate_random_province()
    lng_lat = get_location(address, api_key)
    url = generate_random_url()
    enterpriseName = generate_random_university_name()
    rquest_url = 'http://10.18.40.20:9212/rest/er/unified-op-mgmt-service/api/v1/enterprise/register'
    data = {
        "enterpriseName": enterpriseName,
        "province": address,
        "serviceTypes": random.choice(serviceTypes),
        "lat": lng_lat.lat_str,
        "lng": lng_lat.lng_str,
        "url": url
    }
    response = requests.post(rquest_url, json=data)
    return response.status_code, response.text

if __name__ == '__main__':
    api_key = "883a45c1d6f12398498f4d53b4f306f9"
