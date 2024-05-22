import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Create a WebDriver instance
#Maximize the browser window
driver.maximize_window()
# Open the URL https://courses.icleaf.in/login
driver.get("https://courses.icleaf.in/login")
# Wait for the login page to load
time.sleep(2)
# Find the username and password input fields
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
# Enter username and password
username_field.send_keys("evaluator1")  # Replace "your_username" with your actual username
password_field.send_keys("user@123")  # Replace "your_password" with your actual password
# Find the login button using XPath
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
# Click the login button
login_button.click()
# Wait for a few seconds to see the result
time.sleep(5)
# Close the browser
driver.quit()
