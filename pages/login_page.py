from selenium.webdriver.common.by import By 
from .base_page import BasePage
import time


class LoginPage(BasePage):
    _login_form = {"by": By.ID, "value": "login"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "button"} 
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"} 
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}

    def __init__(self, driver):
        self.driver = driver 
        self.driver.get("https://revelar-qa-portal-practitioner.azurewebsites.net/login") 

    def with_(self, username, password): 
        self._type(self._username_input, username) 
        self._type(self._password_input, password) 
        self._click(self._submit_button)

    def success_message_present(self): 
        self._wait_for_is_displayed(self._success_message, 1) 
        return self._is_displayed(self._success_message)

    def failure_message_present(self): 
        self._wait_for_is_displayed(self._failure_message, 1) 
        return self._is_displayed(self._failure_message)
