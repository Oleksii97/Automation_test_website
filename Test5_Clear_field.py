
import datetime
import time# біблиотека для стоп-часу, без неї не працює
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Phyton\\python_selenium\\chromedriver.exe")

base_url="https://www.saucedemo.com/"
driver.get(base_url)

login="standard_user"
password_all="secret_sauce"

driver.maximize_window()
username=driver.find_element("id","user-name")
print("input login")
username.send_keys(login)
time.sleep(2)
username.clear()





time.sleep(1000)
driver.close