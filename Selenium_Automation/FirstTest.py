from selenium import webdriver
from selenium.webdriver.common.by import By
# เรียกใช้งาน Firefox WebDriver
browser = webdriver.Firefox()
browser.get("http://selenium.dev/")  # เปิดเว็บไซต์
browser.maximize_window()  # ทำให้เบราว์เซอร์เต็มหน้าจอ

# ดึงชื่อ Title ของหน้าเว็บ
title = browser.title
print("Page Title:", title)

#เพิ่มข้อความเพื่อแจ้งข้อผิดพลาด
assert "Selenium123" in title, f"Expected 'Selenium123' in title, but got '{title}'"
browser.findElement(By.xpath("#APjFqb"))