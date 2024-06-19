import profile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Manage_Content.Change_Password import change_pass
from Manage_Content.Configure_Account import ConfigAcc
from Manage_Content.LoginManagecontent import ICleafAutomation
from Manage_Content.Manage_Elearn_Content import Elearn_content
import configparser
from Manage_Content.Manage_Question import Question
from Manage_Content.Manage_Question_Bank import Question_Bank
from Manage_Content.Manage_subject_topic import Sub_topic
from User_Manager.Assign_Approver import Assign_Approver
from User_Manager.Assign_Evaluator import Assign_Evaluator
from User_Manager.Assign_E_learn_Content_To_User import Assign_E_learn_Content_To_User
from Manage_Content.Profile_page import Profile_Pg
from Manage_Content import Change_Password
from Manage_Content import Configure_Account

config = configparser.RawConfigParser()
config.read("Manage_Content\\IC_config.properties")



class ICLEAF:
    def __init__(self):
        self.driver = None

    def run_test_cases(self):
        # Set up WebDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(config.get('MC', 'url'))
        self.driver.maximize_window()
        time.sleep(5)



    def test_cases(self):
        # Initialize automation classes
        IC_admin_login = ICleafAutomation(self.driver)
        IC_admin_login.login()

        # Manage subject and topic

        #create_subject_topic = Sub_topic(self.driver)
        #create_subject_topic.create_subject()

        # Manage question
        #Upload_Question = Question(self.driver)
        #Upload_Question.manage_questions()

        # Manage question bank
        #Create_Que_bank = Question_Bank(self.driver)
        #Create_Que_bank.manage_question_bank()

        # Manage e-learning content
        #Elearn_content_upload = Elearn_content(self.driver)
        #Elearn_content_upload.manage_elearn_content()

        # Manage user (assign approver)
        #Manage_User = Assign_Approver(self.driver)
        #Manage_User.Manage_user()

        # Manage user (assign evaluator)
        #Manage_User = Assign_Evaluator(self.driver)
        #Manage_User.Manage_user()

        #Manage_User = Assign_E_learn_Content_To_User(self.driver)
        #Manage_User.Manage_user()

        #profile = Profile_Pg(self.driver)
        #profile.select_language()

        #change_password = change_pass(self.driver)
        #change_password.change_pass()

        configure_account = ConfigAcc(self.driver)
        configure_account.config_account()



        # Close the driver after the test cases
        self.driver.quit()

if __name__ == "__main__":
    ic = ICLEAF()
    ic.run_test_cases()
    ic.test_cases()