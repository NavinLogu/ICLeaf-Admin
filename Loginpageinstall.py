from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class IcleafLoginAutomation:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def login(self, username, password):
        self.driver.maximize_window()
        self.driver.get("http://139.59.64.128:8080/icleaf/#/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]").click()
        self.driver.implicitly_wait(10)  # Implicitly wait for elements to be ready
        time.sleep(5)  # Wait for a few seconds to observe the result

    def quit(self):
        self.driver.quit()

if __name__ == "__main__":
    automation = IcleafLoginAutomation()
    automation.login("virat", "123")
    automation.quit()
