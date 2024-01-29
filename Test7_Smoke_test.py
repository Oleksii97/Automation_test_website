
import datetime
import time# біблиотека для стоп-часу, без неї не працює
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\Phyton\\python_selenium\\chromedriver.exe")

base_url="https://www.saucedemo.com/"
driver.get(base_url)

"""LogIn"""""

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


#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")     #


"""info about product 1 """

product_1=driver.find_element(By.XPATH,"//*[@id='item_4_title_link']")
value_product_1=product_1.text
print("Name of product 1- ",value_product_1)

price_product_1=driver.find_element(By.XPATH,"//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1=price_product_1.text
print("Price of product 1", value_price_product_1)

add_to_cart=driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").click()
print("Select product 1")
cart=driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
print("Click on the cart")

time.sleep(1)



"""info about product 1 on cart"""

product1_in_cart=driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div")
value_product1_in_cart=product1_in_cart.text
print("Name of product 1 in the cart",value_product1_in_cart)

price_product1_in_cart=driver.find_element(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_product1_in_cart=price_product1_in_cart.text
print("Price of product 1 in the cart",value_price_product1_in_cart)

if value_product_1==value_product1_in_cart and value_price_product_1==value_price_product1_in_cart:
    print("Test is good, product is my")
else:
    print ("Test is bad, product is not my")


botton_check_out=driver.find_element(By.XPATH,"//*[@id='checkout']").click()
print ("CLick button check out")

username=driver.find_element(By.XPATH,"//*[@id='first-name']")
print("input First Name")
username.send_keys("Alex")

username=driver.find_element(By.XPATH,"//*[@id='last-name']")
print("input Last Name")
username.send_keys("Grigoriev")

username=driver.find_element(By.XPATH,"//*[@id='postal-code']")
print("input Postal Code")
username.send_keys("21-324")

#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")

botton_continue=driver.find_element(By.XPATH,"//*[@id='continue']").click()
print ("CLick button continue")



""""Info finish Product 1"""""

finish_product1=driver.find_element(By.XPATH,"//*[@id='item_4_title_link']/div")
value_finish_product=finish_product1.text
print("Name of product 1 in the cart",value_finish_product)
time.sleep(1)
price_finish_product1=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_price_finish_product1=price_finish_product1.text
price_total=driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_price_total=price_total.text
print("Price of product 1 in the cart",value_price_finish_product1)

if value_product_1==value_finish_product and value_price_product_1==value_price_finish_product1 and value_price_product_1==value_price_total:
    print("Test is good, i buy my product, total summary price is good")
else:
    print ("Test is bad, i buy not my product")


botton_continue=driver.find_element(By.XPATH,"//*[@id='finish']").click()
print ("CLick button finish")

#driver.save_screenshot("D:\\Phyton\\python_selenium\\screen\\screenshot.png")     #
print("Screenshot is done")


time.sleep(1000)
driver.close()