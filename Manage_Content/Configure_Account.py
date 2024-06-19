import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import configparser

config = configparser.RawConfigParser()
config.read("Manage_Content/IC_config.properties")


class ConfigAcc:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def config_account(self):
        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Configure_Account')))
        ).click()
        time.sleep(5)

        company_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'company_name2'))))
        self.actions.move_to_element(company_name).click().perform()
        company_name.send_keys(Keys.CONTROL + "a")
        company_name.send_keys(Keys.BACKSPACE)
        company_name.send_keys("INFO")

        company_url = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'company_name2'))))
        company_url.send_keys(Keys.CONTROL + "a")
        company_url.send_keys(Keys.BACKSPACE)
        company_url.send_keys("www.infocareerindia.com")

        address_text_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'confi_address1')))
        )
        self.actions.move_to_element(address_text_box).click().perform()
        address_text_box.send_keys(Keys.CONTROL + "a")
        address_text_box.send_keys(Keys.BACKSPACE)
        address_text_box.send_keys("NO,18,ALWARPET,")
        time.sleep(1)

        address_text_box_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'confi_address2')))
        )
        address_text_box_2.send_keys(Keys.BACKSPACE)
        self.actions.move_to_element(address_text_box_2).click().send_keys("CHENNAI-600046").perform()

        state = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'state')))
        )
        time.sleep(1)
        self.actions.move_to_element(state).click().perform()
        time.sleep(1)
        state.clear()
        state.send_keys("Tamil Nadu")
        state.send_keys("Madurai")