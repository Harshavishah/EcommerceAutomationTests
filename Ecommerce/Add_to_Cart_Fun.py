import time
import unittest
import pandas as pd
from Ecommerce.Login_Functionality import *
from selenium.webdriver.common.by import By
#from selenium import webdriver
from Ecommerce.Browser_page import browser
class Add_to_cart(unittest.TestCase):

        def test_add_to_cart(self):
            Browser = browser.SetUp(self,"https://www.saucedemo.com/")
            # This is generic login function to login into website
            Login_page.login_fun(self,Browser)
            assert Browser.current_url.__contains__("inventory")
            add_item = Browser.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
            add_item.click()
            cart_value = Browser.find_element(By.CLASS_NAME,"shopping_cart_badge")
            print(cart_value.text)
            self.assertTrue(cart_value.text == "1")
            print("there is 1 item in cart")
