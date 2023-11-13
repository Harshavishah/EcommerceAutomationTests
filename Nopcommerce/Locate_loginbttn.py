from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

browser =webdriver.Edge()
browser.get("https://www.nopcommerce.com/en/login?returnUrl=%2Fen")
browser.maximize_window()
delay = 2
try:
    element_present = EC.presence_of_element_located((By.XPATH,'//*[@id="login-page"]/body/div[7]/section/div/div/div/div/div/div[2]/div[1]/div[2]/form/div[2]/div[4]/input'))# page will wait for 5 seconds until username element load otherwise will show message
    WebDriverWait(browser,delay).until(element_present)

except TimeoutException:
    print("Failed to load page")

browser.quit()


