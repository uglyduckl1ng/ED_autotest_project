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
class Can_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    


      #Locators
      select_checkout_button = "//button[@id='checkout']"
      main_word = "(//*[text()[contains(.,'Your Cart')]])"


      #Getters
      def get_select_checkout(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_checkout_button)))
      
      def get_main_word(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

      #Actions
      def click_select_checkout(self):
           self.get_select_checkout().click()
           print("Click chekout")

           
      #Methods
      def select_checkout(self):
           with allure.step("select_checkout"):
               Logger.add_start_step(method="select_checkout")                                                     
               self.assert_word(self.get_main_word(), "Your Cart")
               self.click_select_checkout()
               Logger.add_end_step(self.driver.current_url, method="select_checkout")
           


