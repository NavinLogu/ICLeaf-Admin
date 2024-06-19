from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")

class Sub_topic:
    def __init__(self,driver):
        self.driver = driver

    def create_subject(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Create_button')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, config.get('MC','subjectName_ID')))
        ).send_keys(config.get('MC','subject_name'))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,config.get('MC','Topic_Search')))
        ).send_keys(config.get('MC','topic_name'))
        self.driver.find_element(By.XPATH, config.get('MC','Add_Button')).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','Topic_Name_search')))
        ).send_keys(config.get('MC','Additional_topic'))
        self.driver.find_element(By.XPATH,config.get('MC','save_button') ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,config.get('MC','Manage_content_button')))
        ).click()