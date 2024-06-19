import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import configparser

config = configparser.RawConfigParser()
config.read("Manage_Content/IC_config.properties")


class Profile_Pg:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def select_language(self):
        # Select French language
        french_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'select_french')))
        )
        self.actions.move_to_element(french_element).click().perform()

        # Click on profile icon
        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()

        # Get the displayed message
        message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, config.get('MC', 'print_txt')))
        )
        message_text = message_element.text
        print("Text message displayed above:", message_text)

        # Click on 'Manage profile'
        manage_profile_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Manage_profile')))
        )
        time.sleep(5)
        self.actions.move_to_element(manage_profile_element).click().perform()

        # Fill in the profile details
        self.update_profile_info()

    def update_profile_info(self):
        # Fill in the first name
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC', 'first_name')))
        )
        time.sleep(5)
        self.clear_username_field(username_field)
        username_field.send_keys("NS")

        # Fill in the last name
        last_name_text_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, config.get('MC', 'Last_name')))
        )
        time.sleep(10)
        self.actions.move_to_element(last_name_text_box).click().perform()
        last_name_text_box.clear()
        last_name_text_box.send_keys("Navin")

        # Fill in the address
        address_text_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Address_1')))
        )
        self.actions.move_to_element(address_text_box).click().perform()
        address_text_box.clear()
        address_text_box.send_keys("NO,18,ALWARPET,")
        time.sleep(1)

        address_text_box_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Address_2')))
        )
        self.actions.move_to_element(address_text_box_2).click().send_keys("CHENNAI-600046").perform()

        # Fill in the state
        state = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'state')))
        )
        time.sleep(1)
        self.actions.move_to_element(state).click().perform()
        time.sleep(1)
        state.clear()
        state.send_keys("Tamil Nadu")

        # Scroll to the element
        self.scroll(config.get('MC', 'collage_name'))

        # Fill in the college name
        college = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'collage_name')))
        )
        self.actions.move_to_element(college).click().perform()
        college.send_keys("Anna University")

        # Fill in the company name
        company_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'company_name')))
        )
        self.actions.move_to_element(company_name).click().perform()
        company_name.send_keys("INFO")

        # Upload the photo
        photo_upload = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'photo_upload')))
        )
        photo_upload.send_keys(config.get('MC', 'image_path'))

        # Save changes
        save_changes = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'save_changes')))
        )
        self.actions.move_to_element(save_changes).click().perform()
        time.sleep(10)

        # Confirm the changes
        okay_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Okay_btn')))
        )
        self.actions.move_to_element(okay_btn).click().perform()
        time.sleep(15)

        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()
        time.sleep(10)


        next_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'change_password')))
        )
        self.actions.move_to_element(next_element).click().perform()
        time.sleep(5)

        Ex_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Exisiting_pass')))
        )
        self.actions.move_to_element(Ex_pass).click().perform()
        Ex_pass.send_keys("icleaf@admin")

        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(5)

        new_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'new_pass')))
        )
        self.actions.move_to_element(new_pass).click().perform()
        new_pass.send_keys("admin@icleaf")
        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(5)

        confirm_pass = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'confrim_password')))
        )
        self.actions.move_to_element(confirm_pass).click().perform()
        confirm_pass.send_keys("admin@icleaf")
        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(15)

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'save_changes')))
        ).click()

        time.sleep(10)

        self.driver.find_element(By.XPATH, config.get('MC', 'User_ID')).send_keys(config.get('MC', 'username'))
        time.sleep(4)
        self.driver.find_element(By.XPATH, config.get('MC', 'Password_ID')).send_keys(config.get('MC', 'password2'))
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, config.get('MC', 'eye')).click()
        time.sleep(3)
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'Login_button')))
        )
        login_button.click()

        profile_icon_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, config.get('MC', 'profile_icon')))
        )
        self.actions.move_to_element(profile_icon_element).click().perform()
        time.sleep(15
                   )








    def clear_username_field(self, username_element):
        username_element.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

    def scroll(self, path):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        self.actions.move_to_element(element).perform()
