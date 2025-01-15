import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# เปิด Firefox browser
browser = webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
browser.maximize_window()
time.sleep(5)

# เลื่อนหน้าจอไปด้านล่างเพื่อให้ checkbox มองเห็นได้
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# ดึง Checkboxes ทั้งหมด
checkboxes = browser.find_elements(By.XPATH, value="//input[@type='checkbox']")

# ตรวจสอบและคลิกแต่ละ checkbox
for checkbox in checkboxes:
    browser.execute_script("arguments[0].click();", checkbox)
    time.sleep(1)
checked_count=0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count +=1
excepted_checked_count = 7
if checked_count == excepted_checked_count:
    print("Checkbox count verified")
else:
    print("Checkbox count mismatch")
time.sleep(5)
browser.close()