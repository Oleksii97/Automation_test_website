import time# біблиотека для стоп-часу, без неї не працює
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver=webdriver.Chrome(executable_path="D:\\Phyton\\python_selenium\\chromedriver.exe")

base_url="https://www.saucedemo.com/"
driver.get(base_url)

login="standard_user"
password_all="secret_sauce"

driver.maximize_window()
username=driver.find_element("id","user-name")
username.send_keys(login)
print("input login")
#time.sleep(2)
username.send_keys(Keys.BACKSPACE)
#time.sleep(2)
username.send_keys(Keys.BACKSPACE)
#time.sleep(2)
username.send_keys("er")

pas=driver.find_element("id","password")
pas.send_keys(password_all)
pas.send_keys(Keys.ENTER)
print("input password")

filter=driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
filter.click()
time.sleep(2)
filter.send_keys(Keys.DOWN)
time.sleep(2)
filter.send_keys(Keys.RETURN)

time.sleep(1000)
driver.close