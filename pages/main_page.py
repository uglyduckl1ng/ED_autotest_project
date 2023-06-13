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

class Main_page(Base):

      url = "https://www.saucedemo.com/"

      def __init__(self, driver):    
          super().__init__(driver) 
          self.driver = driver

    

      
      #Locators
      select_product_1 = "(//*[text()[contains(.,'Add to cart')]])"
      cart = "//a[@class='shopping_cart_link']"
      burger_menu = "//button[@id='react-burger-menu-btn']"
      about_b = "//a[@id='about_sidebar_link']"
      



      #Getters
      def get_select_product_1(self, num):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1 + "[" + num + "]")))
      
      def get_cart(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
      def get_burger_menu(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))
      def get_about_b(self):
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_b)))
      
      

      #Actions
      def click_select_product_1(self, num):
           self.get_select_product_1(num).click()
           print("Click select product")

      def click_cart(self):
           self.get_cart().click()
           print("Click cart")
     
      def click_burger_menu(self):
           self.get_burger_menu().click()
           print("click Burger Menu")
      def click_about_b(self):
           self.get_about_b().click()
           print("click About")
      
           
      #Methods
      def select_product(self, num): 
           with allure.step("select_product"): 
               Logger.add_start_step(method="select_product") 
               self.get_current_url()
               self.click_select_product_1(num)
               self.click_cart()
               Logger.add_end_step(self.driver.current_url, method="select_product")
     
      def click_link_about(self):
          with allure.step("click_link_about"):
               Logger.add_start_step(method="click_link_about")
               self.get_current_url()
               self.click_burger_menu()
               self.click_about_b()
               self.assert_url("https://saucelabs.com/")
               self.get_screenshot()
               Logger.add_end_step(self.driver.current_url, method="click_link_about")


