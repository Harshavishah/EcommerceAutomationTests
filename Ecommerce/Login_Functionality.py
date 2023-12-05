import time
import unittest
from Browser_page import *
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Login_page(unittest.TestCase):
    def test_login_fun(self):

        Browser = browser.SetUp(self,"https://www.saucedemo.com/")
        #Browser = browser_page.test_Browser_page(self)
        Exp_page = 'https://www.saucedemo.com/inventory.html'
        time.sleep(5)
        user_name = Browser.find_element(By.ID,"user-name").send_keys("standard_user")
        password = Browser.find_element(By.ID,"password").send_keys("secret_sauce")
        submit = Browser.find_element(By.ID,"login-button").click()

        assert Browser.current_url.__contains__("inventory")

    def login_fun(self,Browser):

        user_name = Browser.find_element(By.ID, "user-name").send_keys("standard_user")
        password = Browser.find_element(By.ID, "password").send_keys("secret_sauce")
        submit = Browser.find_element(By.ID, "login-button").click()




