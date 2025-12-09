from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)

driver.implicitly_wait(10)
driver.get("https://acme-test.uipath.com/")

button_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
email_element = driver.find_element(By.ID,"email")
email_element.send_keys("amritanshlal@gmail.com")

pass_element = driver.find_element(By.NAME,"password")
pass_element.send_keys("Welcome@1234")

button_submit.click()
time.sleep(30)