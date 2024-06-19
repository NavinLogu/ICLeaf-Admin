import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import configparser
from selenium.webdriver import Keys, ActionChains


config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")

class Assign_Approver:
    def __init__(self, driver):
        self.driver = driver


    def Manage_user(self):


            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Manage_User')))
            ).click()

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC', 'click_assign_approver')))
            ).click()

            search_box_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Search_Box')))
            )
            search_box_element.send_keys("PMP JAN2021 ECO")
            print("Entered search term")
            time.sleep(5)

            Nxt_Page = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'next_page')))
            )
            ActionChains(self.driver).move_to_element(Nxt_Page).click().perform()
            time.sleep(5)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Assign_Approver_click')))
            ).click()

            time.sleep(5)
            approver = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_approver')))
            )
            approver.send_keys('Yash')
            approver.send_keys(Keys.ENTER)
            time.sleep(5)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'save_button')))
            ).click()

            self.driver.save_screenshot('screenshot_location.png')

            # Wait for the message element and print its text
            message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, config.get('MC', 'pop_text')))
            )
            message_text = message_element.text
            print("Text message displayed above:", message_text)
            time.sleep(5)

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_okay')))
            ).click()
            time.sleep(1)
            pass

