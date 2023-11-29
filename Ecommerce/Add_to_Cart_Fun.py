import unittest
import pandas as pd
from Ecommerce.Login_Functionality import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import Login_Functionality

class Add_to_cart(unittest.TestCase):
    def test_login_fun(self):
       pass

    def test_add_to_cart(self):
        Browser = webdriver.Edge()
        Browser.get("https://www.saucedemo.com/")
        Browser.maximize_window()
        add_to_cart_btn = Browser.find_elements(By.ID,"add-to-cart-sauce-labs-backpack")
        for btns in add_to_cart_btn[:3]:
            btns.click()
        time.sleep(5)
        cart_value = Browser.find_elements(By.CLASS_NAME,"cart_quantity")
        assert "3" in cart_value.text
        print("There are 3 items in cart")