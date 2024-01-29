from selenium.webdriver import ActionChains
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
pas=driver.find_element("id","password")
print("input password")
pas.send_keys(password_all)
butt=driver.find_element("id","login-button").click()
print("Click on the buttton")





driver.execute_script("window.scrollTo(0,500)")  #можливо скролить

                          #можливість знайти елемент на сайті
action = ActionChains(driver)      #from selenium.webdriver import ActionChains
red_sweatr = driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_sweatr).perform()



#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")     #


time.sleep(1000)
driver.close