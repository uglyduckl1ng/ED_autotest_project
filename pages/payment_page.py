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

class Payment_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    


      #Locators
      payment_button = "//button[@id='finish']"


      #Getters
      
      def get_payment_button(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_button)))

      #Actions
      def click_payment_button(self):
           self.get_payment_button().click()
           print("Click payment_button")
           
      #Methods
     
      def click_selected_payment_button(self): 
           with allure.step("click_selected_payment_button"):
               Logger.add_start_step(method="click_selected_payment_button") 
               self.get_current_url()
               self.click_payment_button()
               Logger.add_end_step(self.driver.current_url, method="click_selected_payment_button")



