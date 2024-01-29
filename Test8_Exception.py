import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


driver=webdriver.Chrome(executable_path="D:\\Phyton\\python_selenium\\chromedriver.exe")

base_url="https://demoqa.com/dynamic-properties"
driver.get(base_url)



driver.maximize_window()


try:
  visible_button=driver.find_element(By.XPATH,"//*[@id='visibleAfter']").click()
  print("Click visible button")
except NoSuchElementException as exception:
  print("Error don't found element")
  time.sleep(6)
  visible_button=driver.find_element(By.XPATH,"//*[@id='visibleAfter']").click()
  print("Click visible button")
time.sleep(1000)
