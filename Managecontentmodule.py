from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class ICleafAutomation:
    def __init__(self):
        self.driver = None

    def setup(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("http://139.59.64.128:8080/icleaf/#/login")

    def select_language(self, language):
        select_language = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "select"))
        )
        Select(select_language).select_by_value(language)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "svg.eye-icon_login").click()
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
        )
        login_button.click()

    def create_subject(self, subject_name, topic_name, topic_name2):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Create')]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'subjectName'))
        ).send_keys(subject_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Topic Name"]'))
        ).send_keys(topic_name)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Topic Name'])[2]"))
        ).send_keys(topic_name2)
        self.driver.find_element(By.XPATH, "//button[.='Save']").click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="button" and @class="modalcommad_btn info"]'))
        ).click()

    def manage_content(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Manage Content')]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/UploadQuestions"]'))
        ).click()

    def select_subject_and_topic(self, subject_name, topic_name, num_questions):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='css-8mmkcg'])[1]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{subject_name}']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='css-8mmkcg'])[2]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{topic_name}']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[name()='svg'][@class='css-8mmkcg'])[3]"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[text()='{num_questions}']"))
        ).click()

    def add_question(self, reference_name, question_text, answer):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='text'])[4]"))
        ).send_keys(reference_name)
        self.driver.find_element(By.XPATH, "//button[@class='addQues-btn']").click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='modalcommad_btn']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//textarea[@class='textareaquestion'])[1]"))
        ).send_keys(question_text)

    def select_question_type(self, file_path):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@aria-hidden="true"])[1]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Image"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='iconDiv'])[1]/input[@type='file']"))
        ).send_keys(file_path)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//text[.="Okay"]'))
        ).click()

    def set_answer(self, answer):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@aria-hidden="true"])[2]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Fillup type"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//input[@type="text"])[3]'))
        ).send_keys(answer)

    def add_video_question(self, video_path):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//textarea[@class="textareaquestion"])[2]'))
        ).send_keys("Importance in Flight")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@aria-hidden="true"])[3]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Video"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='iconDiv'])[1]/input[@type='file']"))
        ).send_keys(video_path)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="modalcommad_btn info"]'))
        ).click()

    def finalize_question(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//div[@aria-hidden="true"])[4]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Medium"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[1]"))
        ).send_keys("2")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//text[.='Go To']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.='Previous']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//text[.='Save and Exit']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
        ).click()

    def bulk_upload_questions(self, file_path):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@type="radio"])[2]'))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
        ).send_keys(file_path)
        time.sleep(20)

    def click_parse_file(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Parse File")]'))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]'))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[@class="input-txt-box"]'))
        ).send_keys("AAAAAA")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[.="Upload"]'))
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modalcommad_btn"))
        ).click()
        time.sleep(10)

    def manage_question_bank(self, sub, topic):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Manage Content')]"))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/manageQuestionbank"]'))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-8mmkcg"))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Advance Java']"))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@type = 'text'])[2]"))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Media']"))).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Download')]"))
        ).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@class="table-button"])[1]'))
        ).click()
        time.sleep(5)
        self.scroll('//button[contains(text(),"Save")]')
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[contains(text(),"Save")])'))
        ).click()
        self.driver.save_screenshot("test.png")
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[.="Okay"]'))
        ).click()
        time.sleep(10)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@class="table-button"])[2]'))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Close")]'))
        ).click()
        time.sleep(5)

    def scroll(self, path):
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def manage_elearn_content(self, sub, topic):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Manage Content')]"))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="#/manageElearnContent"]'))
        ).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-8mmkcg"))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Advance Java']"))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@type = 'text'])[2]"))).click()
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text() = 'Media']"))).click()
        time.sleep(10)


# Example usage
if __name__ == "__main__":
    automation = ICleafAutomation()
    automation.setup()
    automation.select_language("english")
    automation.login("icadmin", "icleaf@admin")
    automation.create_subject("testCases1", "whiteboxtesting11", "Blackboxtesting11")
    automation.manage_content()
    automation.select_subject_and_topic("Aeronautical Engineering", "Engineering", "2")
    automation.add_question("icleafadminauto1", "The component of an aircraft that provides thrust is known as the ______", "Engine")
    automation.select_question_type("C://Users/navin/OneDrive/Ratan-Tata-Quotes-14.jpg")
    automation.set_answer("Engine")
    automation.add_video_question("C://Users/navin/OneDrive/20770858-hd_1080_1920_30fps.mp4")
    automation.finalize_question()
    automation.bulk_upload_questions("C://Users/navin/Downloads/Engineering.txt")
    automation.click_parse_file()
    sub = "Advance Java"
    topic = "Engineering"
    automation.manage_question_bank(sub, topic)
    automation.manage_elearn_content(sub, topic)
