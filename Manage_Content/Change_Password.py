import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import configparser

config = configparser.RawConfigParser()
config.read("Manage_Content/IC_config.properties")


class change_pass:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def change_pass(self):
        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()
        time.sleep(2)

        next_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'change_password')))
        )
        self.actions.move_to_element(next_element).click().perform()
        time.sleep(2)

        Ex_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Exisiting_pass')))
        )
        Ex_pass.click()
        Ex_pass.send_keys("icleaf@admin")
        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(2)

        new_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'new_pass')))
        )
        new_pass.click()
        new_pass.send_keys("admin@icleaf")

        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(2)

        confirm_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'confrim_password')))
        )
        confirm_pass.click()
        confirm_pass.send_keys("admin@icleaf")
        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(2)

        # Use a loop to handle potential element blocking
        for _ in range(5):
            try:
                save_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, config.get('MC', 'save_changes')))
                )
                save_button.click()
                break
            except ElementClickInterceptedException:
                time.sleep(2)

        time.sleep(10)

        self.driver.find_element(By.XPATH, config.get('MC', 'User_ID')).send_keys(config.get('MC', 'username'))
        time.sleep(2)
        self.driver.find_element(By.XPATH, config.get('MC', 'Password_ID')).send_keys(config.get('MC', 'password2'))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(2)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Login_button')))
        )
        login_button.click()

        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()
        time.sleep(2)

    def scroll(self, path):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        self.actions.move_to_element(element).perform()
