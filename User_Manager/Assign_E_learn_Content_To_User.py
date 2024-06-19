import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import configparser

config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")


class Assign_E_learn_Content_To_User:

    def __init__(self, driver):
        self.driver = driver

    def Manage_user(self):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Manage_User')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC', 'Assign_E_learn_Content_To_User')))
        ).click()
        time.sleep(5)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'user_name')))
        )
        username.send_keys('ns')
        username.send_keys(Keys.ENTER)
        search_button = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','search_button')))
        )
        search_button.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'edit_pack_details')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_arrow')))
        ).click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'subject_name_Artificial_Intelligence')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'down_arrow_btn')))
        ).click()

        date_pick = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC', 'Data_picker'))))
        ActionChains(self.driver).move_to_element(date_pick).click().perform()

        #date = WebDriverWait(self.driver, 30).until(
           # EC.element_to_be_clickable((By.XPATH, config.get('MC', 'date_box'))))
        #date_value = "2024-06-31"
        #self.driver.execute_script(f"arguments[0].value = '{date_value}';", date)
        time.sleep(1)
        assign_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Assign_button')))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", assign_button)
        time.sleep(1)
        assign_button.click()

        time.sleep(1)

        okay_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_okay')))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", okay_button)
        okay_button.click()

        time.sleep(5)

        message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC', 'e_learn_assigned_pop')))
        )
        message_text = message_element.text
        print("Text message displayed above:", message_text)

        time.sleep(5)



