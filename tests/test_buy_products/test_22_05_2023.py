
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

@allure.description("Test buy product 1")
@pytest.mark.run(order = 1)
def test_buy_product(set_group):
        global driver_test
        driver_test = set_group
        login = Login_page(driver_test)
        login.authoratization(username="standard_user", password="secret_sauce")   
        mp = Main_page(driver_test)
        mp.select_product("2")
        cp = Can_page(driver_test)
        cp.select_checkout()
        uip = UIP_page(driver_test)
        uip.click_continue()
        pp = Payment_page(driver_test)
        pp.click_selected_payment_button()
        fp = Finish_page(driver_test)
        fp.finish()

@pytest.mark.run(order = 2)
def test_buy_product2():
        login = Login_page(driver_test)
        login.authoratization(username="standard_user", password="secret_sauce")   
        mp = Main_page(driver_test)
        mp.select_product("3")
        cp = Can_page(driver_test)
        cp.select_checkout()
        uip = UIP_page(driver_test)
        uip.click_continue()
        pp = Payment_page(driver_test)
        pp.click_selected_payment_button()
        fp = Finish_page(driver_test)
        fp.finish()

@pytest.mark.run(order = 3)
def test_buy_product3():
        login = Login_page(driver_test)
        login.authoratization(username="standard_user", password="secret_sauce")   
        mp = Main_page(driver_test)
        mp.select_product("1")
        cp = Can_page(driver_test)
        cp.select_checkout()
        uip = UIP_page(driver_test)
        uip.click_continue()
        pp = Payment_page(driver_test)
        pp.click_selected_payment_button()
        fp = Finish_page(driver_test)
        fp.finish()

        


        
