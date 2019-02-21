import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin():

    @pytest.fixture
    def driver(self, request):
        _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver') 
        driver_ = webdriver.Firefox(executable_path=_geckodriver)

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_


    def test_valid_credentials(self, driver):
       driver.get("https://revelar-qa-portal-practitioner.azurewebsites.net/login") 
       time.sleep(3)
       driver.find_element(By.ID, "login-email").send_keys("revboomdoom@dispostable.com") 
       driver.find_element(By.ID, "login-password").send_keys("Welcome1@") 
       driver.find_element(By.ID, "login-button").click()
       time.sleep(1)
       assert driver.find_element(By.ID, "navbar-btn-Dashboard").is_displayed()

       time.sleep(5)
