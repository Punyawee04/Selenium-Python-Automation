import time
from selenium import webdriver

viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]  # แก้ไขรายการให้เป็น list ธรรมดา
driver = webdriver.Chrome()

try:
    driver.get('https://www.google.com/')  # เปิดเว็บไซต์
    for width, height in viewports:
        driver.set_window_size(width, height)  # ปรับขนาดหน้าต่าง
        time.sleep(4)  # รอ 4 วินาที
finally:
    driver.close()  # ปิดเบราว์เซอร์
