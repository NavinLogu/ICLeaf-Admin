from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import configparser
config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")


class Elearn_content:
    def __init__(self,driver):
        self.driver = driver

    def manage_elearn_content(self):
        (WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Manage_content_click')))).click())

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC','manage_elearn_content')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','elearn_new_add')))
        ).click()


        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('MC','select_que')))
        ).click()


        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','que_bank_sub')))
        ).click()


        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC','que_bank_click')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','que_bank_topic')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','arrow_down')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','listen_to_trainers')))
        ).click()
        time.sleep(10)


        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','upload_audio')))
        ).send_keys(config.get('MC','audio_path'))
        time.sleep(10)

        WebDriverWait(self.driver, 30).until(
           EC.element_to_be_clickable((By.XPATH, config.get('MC','elearn_table_actn_btn')))
        ).click()
        time.sleep(25)


        WebDriverWait(self.driver, 30).until(
           EC.element_to_be_clickable((By.XPATH, config.get('MC','click_okay')))
        ).click()
        time.sleep(25)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('MC','select_que')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC',f'elearn_subject')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC','que_bank_click')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC',f'elearn_topic')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','listen_to_trainers_click')))
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, config.get('MC','view_btn')))
        ).click()


        self.driver.save_screenshot(config.get('MC','screenshot_location'))

        message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC','copy_txt')))
        )
        message_text = message_element.text
        print("Text message displayed above ", message_text)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, config.get('MC','cancel_btn')))
        ).click()
        time.sleep(5)
