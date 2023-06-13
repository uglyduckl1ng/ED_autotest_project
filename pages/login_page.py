from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains, Keys
import sys 
sys.path.append("C:\\Users\\galov\\OneDrive\\Workspace\\Projects\\Guides\\Selenium_course\\final_project")
from base.base_class import Base 
from utilities.logger import Logger 
import allure

class Login_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    


      #Locators
      user_name = "(//input[@id='user-name'])"
      password = "(//input[@id='password'])"
      login_button = "//input[@id='login-button']"
      main_word = "(//*[text()[contains(.,'Products')]])"


      #Getters
      def get_user_name(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
      
      def get_password(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
      
      def get_login_button(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
     
      def get_main_word(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
      

      #Actions
      def input_user_name(self, user_name):

           self.get_user_name().send_keys(user_name)
           print("Input user_name")

      def input_password(self, password):
           self.get_password().send_keys(password)
           print("Input password")

      def click_login_button(self):
           self.get_login_button().click()
           print("Click login_button")
           
      #Methods
      def authoratization(self, username, password): 
           with allure.step("authoratization"):
               Logger.add_start_step(method="authoratization")             
               self.driver.get(self.url)
               self.driver.maximize_window()
               self.get_current_url()
               self.input_user_name(username)
               self.input_password(password)
               self.click_login_button()
               self.assert_word(self.get_main_word(), "Products")
               Logger.add_end_step(self.driver.current_url, method="authoratization")


