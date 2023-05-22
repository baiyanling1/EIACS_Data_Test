import requests
from faker import Faker
import time

# 构造请求参数
key = "883a45c1d6f12398498f4d53b4f306f9"

# 创建Faker对象，用于随机生成地址信息
fake = Faker()

# 发送请求获取经纬度
locations = []
for i in range(20):
    # 随机生成美国的地址信息
    state = fake.state_abbr()
    city = fake.city()
    district = fake.city_suffix()
    street = fake.street_name()
    street_number = fake.building_number()

    # 构造地址字符串
    address = f"{state}{city}{district}{street}{street_number}"

    # 构造请求参数
    params = {
        "key": key,
        "address": address,
    }

    # 发送请求
    url = "https://restapi.amap.com/v3/geocode/geo"
    response = requests.get(url, params=params)

    # 解析响应，获取经纬度信息
    if response.status_code == 200:
        result = response.json()
        if result["status"] == "1":
            geocodes = result["geocodes"]
            if geocodes:
                # 随机选择一个经纬度
                location = geocodes[0]["location"]
                locations.append((address, location))
                print(f"{i+1}. Generated address: {address}")
                print(f"    Location: {location}")
            else:
                print(f"{i+1}. No geocodes found for address: {address}")
        else:
            print(f"{i+1}. Failed to get geocodes for address: {address}")
    else:
        print(f"{i+1}. Request failed for address: {address}")

    # 休眠1秒，避免请求过于频繁
    time.sleep(1)

print(f"Got {len(locations)} locations.")
print(locations)