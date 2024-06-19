import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")


class ICleafAutomation:
    def __init__(self,driver):
        self.driver = driver

    def login(self):
            self.driver.find_element(By.XPATH,config.get('MC','User_ID')).send_keys(config.get('MC','username'))
            time.sleep(4)
            self.driver.find_element(By.XPATH, config.get('MC','Password_ID')).send_keys(config.get('MC','password'))
            time.sleep(4)
            self.driver.find_element(By.CSS_SELECTOR, config.get('MC','eye')).click()
            time.sleep(3)
            login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Login_button')))
            )
            login_button.click()
            time.sleep(5)
            self.login_status = True  # Update cache after successful login
            return self.login_status



