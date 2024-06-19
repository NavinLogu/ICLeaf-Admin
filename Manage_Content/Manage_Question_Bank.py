from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")

class Question_Bank:
    def __init__(self,driver):
        self.driver = driver

    def manage_question_bank(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Manage_content_click')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC','manage_que_bank')))
        ).click()

        # Select the subject
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, config.get('MC','select_que')))).click()


        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','que_bank_sub')))).click()

        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC','que_bank_click')))).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','que_bank_topic')))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Download_que')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','edit_que')))
        ).click()


        Question_Bank.scroll(self, config.get('MC','save_que_bank'))

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[contains(text(),"Save")])'))
        ).click()
        self.driver.save_screenshot("test.png")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','click_okay')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Severity_Que')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Que_bank_close')))
        ).click()


    def scroll(self, path):
        element = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, path)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        return