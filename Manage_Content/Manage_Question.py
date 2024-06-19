from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")

class Question:
    def __init__(self, driver):
        self.driver = driver

    def manage_questions(self):
        # Navigate to Manage Content
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Manage_content_click')))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.get('MC', 'Manage_Question')))
        ).click()

        # Select Subject
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'click_Arrow')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', f'Select_Subject')))
        ).click()
        # Select Topic
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','click_arrow_btn')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC',f"Select_topic")))
        ).click()

        # Select Number of Questions
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','no_of_Que')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','select_no_of_que')))
        ).click()

        # Add Question
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','ref_name')))
        ).send_keys(config.get('MC','reference_name'))
        self.driver.find_element(By.XPATH, config.get('MC','add_Que')).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Btn_click')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,config.get('MC','Send_Que')))
        ).send_keys(config.get('MC','question_text'))

        # Select Question Type and Upload Image
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_arrow')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','select_img')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','img_path')))
        ).send_keys(config.get('MC','image_path'))
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','click_okay')))
        ).click()
        # Set Answere
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_ans')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Fill_up')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC', 'Send_ans')))
        ).send_keys(config.get('MC','answer'))

        # Add Video Question
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','Send_Que_Ans')))
        ).send_keys("Importance in Flight")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'arrow_down')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'video_btn')))
        ).click()
        time.sleep(20)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC', 'img_path')))
        ).send_keys(config.get('MC','video_path'))
        time.sleep(30)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','pop_click')))
        ).click()
        time.sleep(5)

        # Finalize Question
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'difficult_arrow_btn')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'medium_btn')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','input_file')))
        ).send_keys("2")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','Send_key')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'previous_page')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'save_Exit')))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Okay_btn')))
        ).click()

        # Bulk Upload Questions
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'bulk_Que')))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC', 'bulk_file')))
        ).send_keys(config.get('MC','bulk_file_path'))
        time.sleep(20)  # Adjust the sleep time according to the upload time for large files

        # Click Parse File
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'parse_file')))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Okay_btn')))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC','send_value')))
        ).send_keys("AAAAAA")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC','upload')))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, config.get('MC','press_okay')))
        ).click()
        time.sleep(10)
