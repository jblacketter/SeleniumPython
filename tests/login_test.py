import pytest
from selenium import webdriver
from pages import login_page


class TestLogin():

    @pytest.fixture
    def login(self, request):
        _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver') 
        driver_ = webdriver.Firefox(executable_path=_geckodriver)

        def quit(): 
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid_credentials(self, login): 
        login.with_("revboomdoom@dispostable.com", "Welcome1@") 
        assert login.success_message_present()


    def test_invalid_credentials(self, login): 
        login.with_("tomsmith", "bad password")
        assert login.success_message_present() == False



      # driver.find_element(By.ID, "login-email").send_keys("revboomdoom@dispostable.com") 
       #driver.find_element(By.ID, "login-password").send_keys("Welcome1@") 
       #driver.find_element(By.ID, "login-button").click()
       #assert driver.find_element(By.ID, "navbar-btn-Dashboard").is_displayed()

  #  def test_invalid_credentials(self, login): 
    #    login.with_("tomsmith", "bad password") 

    #    assert login.success_message_present() == False