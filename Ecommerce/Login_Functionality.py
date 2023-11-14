import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


Browser = webdriver.Edge()
Browser.get("https://www.saucedemo.com/")
Browser.maximize_window()

user_name = Browser.find_element(By.ID,"user-name").send_keys("standard_user")
password = Browser.find_element(By.ID,"password").send_keys("secret_sauce")
submit = Browser.find_element(By.ID,"login-button").click()
time.sleep(10)

Act_title ="Swag Labs"
assert Act_title == Browser.title

Browser.quit()
