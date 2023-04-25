

import re

regex = r"^1(3\d|4[5-9]|5[0-35-9]|6[2567]|7[0-8]|8\d|9[0-35-9])\d{8}$"
phone_num = "15452188332"
match = re.match(regex, phone_num)
if match:
    print("该号码是有效的中国大陆手机号码")
else:
    print("该号码不是有效的中国大陆手机号码")