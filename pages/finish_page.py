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

class Finish_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    


      #Locators



      #Getters

      

      #Actions

           
      #Methods
      def finish(self):  
           with allure.step("finish"):
                Logger.add_start_step(method="finish")                                 
                self.get_current_url()
                self.assert_url("https://www.saucedemo.com/checkout-complete.html")
                self.get_screenshot()
                Logger.add_end_step(self.driver.current_url, method="finish")



