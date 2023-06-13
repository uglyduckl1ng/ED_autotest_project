
import time
import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys 
sys.path.append("C:\\Users\\galov\\OneDrive\\Workspace\\Projects\\Guides\\Selenium_course\\final_project")
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.can_page import Can_page
from pages.user_info_page import UIP_page
from  pages.finish_page import Finish_page
from pages.payment_page import Payment_page
from utilities.conftest import set_group
import allure


def test_buy_product(set_group):
        driver_test = set_group
        print("Start test")
        login = Login_page(driver_test)
        mp = Main_page(driver_test)

        login.authoratization(username="standard_user", password="secret_sauce")   
        mp.click_link_about()

        
        

        


        
