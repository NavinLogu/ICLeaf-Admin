import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import configparser

config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")


class Assign_Evaluator:
    def __init__(self, driver):
        self.driver = driver

    def Manage_user(self):

        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Manage_User')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC', 'clck_assign_Evaluator')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_Arrow')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'que_bank_sub')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_arrow_btn')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'exam_pack')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_sec_arrow')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'exam_name')))
        ).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_nxt_arrow')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Intro')))
        ).click()

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_nxt_nxt_arrow')))
        ).click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'for_evaluation')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','assign_clk')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'assign_ok_button')))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_okay')))
        ).click()
        time.sleep(5)
