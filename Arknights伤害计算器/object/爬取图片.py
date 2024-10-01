from lxml import etree
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "https://prts.wiki/w/%E6%8E%A2%E7%B4%A2%E8%80%85%E7%9A%84%E9%93%B6%E5%87%87%E6%AD%A2%E5%A2%83/%E4%BB%AA%E5%BC%8F%E7%94%A8%E5%93%81%E7%B4%A2%E5%BC%95"
# 启动浏览器

driver = webdriver.Chrome()
driver.get(url)




# 设置等待时间，最多等待10秒钟
wait = WebDriverWait(driver, 60)
# 等待页面加载完成，直到 footer 元素可见
footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
# 模拟慢慢滑动到页面最底部
body = driver.find_element(By.TAG_NAME, 'body')
while True:
    body.send_keys(Keys.DOWN)
    time.sleep(0.001)  # 模拟滚动的速度，可以根据需要调整
    # 检查是否已经到达页面底部
    if driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.scrollHeight"):
        break

img_elements = driver.find_elements(By.TAG_NAME, 'img')
print(img_elements)