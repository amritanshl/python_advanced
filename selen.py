from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://acme-test.uipath.com/")
driver.implicitly_wait(10)
email_element = driver.find_element(By.ID,"email")
email_element.send_keys("amritanshlal@gmail.com")
time.sleep(5)
pass_element = driver.find_element(By.NAME,"password")
pass_element.send_keys("Welcome@1234")
time.sleep(30)