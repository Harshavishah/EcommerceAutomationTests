import time
import unittest
from selenium import webdriver

class browser(unittest.TestCase):
        def SetUp(self,url):
                browser = webdriver.Edge()
                browser.get(url)
                browser.maximize_window()
               # time.sleep(2)
                return browser

