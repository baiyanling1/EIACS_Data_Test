import ipaddress
import random

# 生成1000个IP地址段
ip_ranges = []
for i in range(1000):
    # 随机生成一个IP地址，并将最后一位设置为1到254之间的随机数
    ip = ipaddress.IPv4Address(random.randint(0, 2**32-2) + 1 + random.randint(1, 254))
    # 随机生成一个网络掩码长度
    netmask_len = random.randint(16, 24)
    print(str(ip)+'/'+str(netmask_len))
    # 将IP地址和网络掩码长度组合成一个IP地址段对象
    ip_range = ipaddress.IPv4Network((ip, netmask_len), strict=False)
    # 将IP地址段对象添加到列表中
    ip_ranges.append(ip_range)

# # 打印生成的IP地址段CIDR格式
# for ip_range in ip_ranges:
#     print(ip_range)