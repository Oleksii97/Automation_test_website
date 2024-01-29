
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
username=driver.find_element(By.XPATH,"//input[@id='user-name']")
print("input login")
username.send_keys(login)
pas=driver.find_element("id","password")
print("input password")
pas.send_keys(password_all)
butt=driver.find_element("id","login-button").click()
print("Click on the buttton")

menu=driver.find_element(By.XPATH,"//*[@id='react-burger-menu-btn']").click()
print("Click button menu")
time.sleep(1)
link_about=driver.find_element(By.XPATH,"//*[@id='about_sidebar_link']").click()
#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")     # Зроибити СКРІНШОТ і
driver.back()   #  вернутися назад                                                                               # зберегти в папці
time.sleep(1)
driver.forward()    #  пройти назад вперед

time.sleep(1000)
driver.close