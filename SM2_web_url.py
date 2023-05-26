import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


#通过https://chromedriver.chromium.org/downloads 下载浏览器对应版本的驱动，
# 创建一个 Service 对象，指定 ChromeDriver 的路径
#'/Users/hejian/Downloads/chromedriver_mac64 (1)/chromedriver'替换为下载的驱动的路径
chromedriver_path = "/Users/hejian/Downloads/chromedriver_mac64 (1)/chromedriver"
service = Service(executable_path=chromedriver_path)

# 创建一个 Chrome WebDriver 对象，传递 Service 对象
driver = webdriver.Chrome(service=service)
#SM3摘要
# 打开网页
driver.get("https://iyn.me/use/websm3/")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'btn_SM3')))

# 输入明文：原始数据
plaintext = '0000000000000000000000000000F33C'
plaintext_box = driver.find_element(By.ID, 'textarea_SM3')
plaintext_box.clear()
plaintext_box.send_keys(plaintext)

#点击计算SM3摘要
encrypt_button = driver.find_element(By.ID, 'btn_SM3')
encrypt_button.click()

time.sleep(5)

#获取摘要值
ciphertext_box = driver.find_element(By.ID, "result_SM3")
ciphertext = ciphertext_box.text
print("原始数据：", plaintext)
print("SM3摘要：", ciphertext)

#拼接摘要和原始数据
sm3_dig=plaintext+"##"+ciphertext
print("SM3拼接结果：", sm3_dig)



#SM2加密过程
# 打开网页
driver.get("https://the-x.cn/zh-cn/cryptography/Sm2.aspx")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='SM2公钥加密']")))

# 输入公钥
key_text = '-----BEGIN PUBLIC KEY-----\r\nMFkwEwYHKoZIzj0CAQYIKoEcz1UBgi0DQgAE2cB7HihWh1tWgd5WMGpFmFa0aFmnVAZ8jVMqf5uc3p7P+7h/n+UWYMyHLDZ+3x0/9FElpqIhRJrBj8md4R/8IA==\r\n-----END PUBLIC KEY-----\r\n'
plaintext_box = driver.find_element(By.NAME, 'key')
plaintext_box.clear()
plaintext_box.send_keys(key_text)

# 输入明文
plaintext = sm3_dig
plaintext_box = driver.find_element(By.NAME, 'src')
plaintext_box.clear()
plaintext_box.send_keys(plaintext)

##设置输出类型为HEX
# 找到名为"outType"的select元素
outType = Select(driver.find_element(By.NAME, "outType"))
# 将其值设置为"hex-16"
outType.select_by_value("hex-16")

# 点击公钥加密按钮
encrypt_button = driver.find_element(By.CSS_SELECTOR,"input[value='SM2公钥加密']")
encrypt_button.click()

time.sleep(5)

# 获取密文
ciphertext_box = driver.find_element(By.ID, "output")
ciphertext = ciphertext_box.get_attribute('value')

# 关闭浏览器
driver.quit()
# 输出结果
# print("明文：", plaintext)
# print("密文：", ciphertext)

# 将文本内容按行分割，并获取第3行开始的数据
output_lines = ciphertext.split("\n")
output_text = "".join(output_lines[2:])

# 去除空格
output_text = output_text.replace(" ", "")
# 打印结果
print("SM2最终的加密结果：", output_text)