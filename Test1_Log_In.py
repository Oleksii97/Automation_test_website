
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

text_products=driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span")
value_text_products=text_products.text      #Перевірка на то чи війшло в систему, на сайті коли зареєстрований
                                            #  є слово -Products
print(value_text_products)
assert value_text_products=="Products"
print("Test is good")

url="https://www.saucedemo.com/inventory.html"   #Перевірка по url чи на властивомі url, якщо на властивому,
                                                   #то теж війшло на сайт
get_url=driver.current_url
assert get_url==url
print("url is good")




#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")     # Зроибити СКРІНШОТ і
                                                                                   # зберегти в папці

time.sleep(1000)
driver.close