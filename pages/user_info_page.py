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

class UIP_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    


      #Locators
      first_name = "//input[@id='first-name']"
      last_name = "//input[@id='last-name']"
      zip_code = "//input[@id='postal-code']"
      continue_button = "//input[@id='continue']"


      #Getters
      def get_first_name(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
      
      def get_last_name(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
      
      def get_zip_code(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))
     
      def get_continue_button(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))
      

      #Actions
      def input_first_name(self, first_name):

           self.get_first_name().send_keys(first_name)
           print("Input first_name")

      def input_last_name(self, last_name):
           self.get_last_name().send_keys(last_name)
           print("Input last_name")

      def input_zip_code(self, zip_code):
           self.get_zip_code().send_keys(zip_code)
           print("Input zip_code")
      def click_continue_button(self):
           self.get_continue_button().click()
           print("Click continue_button")
           
      #Methods
      def click_continue(self):  
           with allure.step("click_continue"):
               Logger.add_start_step(method="click_continue")                                            
               self.input_first_name("dadada")
               self.input_last_name("password")
               self.input_zip_code("2w323232")
               self.click_continue_button()
               Logger.add_end_step(self.driver.current_url, method="click_continue")



