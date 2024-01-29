import time# біблиотека для стоп-часу, без неї не працює
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Phyton\\python_selenium\\chromedriver.exe")

base_url="https://www.saucedemo.com/"
driver.get(base_url)

login="standard_use"
password_all="secret_sauce"

driver.maximize_window()
username=driver.find_element("id","user-name")
print("input login")
username.send_keys(login)
pas=driver.find_element("id","password")
print("input password")
pas.send_keys(password_all)
butt=driver.find_element("id","login-button").click()
print("Click on the buttton")

error="Epic sadface: Username and password do not match any user in this service"
warring=driver.find_element(By.XPATH,"//h3[@data-test='error']")
value_warring=warring.text
assert error==value_warring
print("Good test")

driver.refresh() #оновити сторінку

time.sleep(1000)
driver.close