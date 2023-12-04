import time
import unittest
from selenium import webdriver



class browser(unittest.TestCase):
        def setUp(self):
                browser = webdriver.Edge()
                browser.get("https://www.saucedemo.com/")
                browser.maximize_window()
                time.sleep(2)
                return browser

