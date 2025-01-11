from selenium import webdriver
from selenium.webdriver.common.by import By
# เรียกใช้งาน Firefox WebDriver
driver = webdriver.Firefox()
driver.maximize_window()  # ทำให้เบราว์เซอร์เต็มหน้าจอ
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/v1/"
driver.get(login_url)


username_field = driver.find_element(By.ID,value="user-name")
password_field = driver.find_element(By.ID,value="password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID,value="login_button")
assert login_button.get_attribute("disabled")
login_button.click()

success_element = driver.find_element(By.CSS_SELECTOR,valu=".title")
assert success_element.text == "Productss"