from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://139.59.64.128:8080/icleaf/#/login")
driver.find_element(By.ID, "username").send_keys("virat")
driver.find_element(By.ID, "password").send_keys(123)
driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()
driver.wait(1000)
driver.sleep(5)