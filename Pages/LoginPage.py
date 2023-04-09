from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.ProfilePage import ProfilePage


class LoginPage(BasePage):

    """Locators"""
    USER_NAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    NEW_USER_BUTTON = (By.ID, "newUser")

    """Constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""

    def get_login_page_title(self, title):
        return self.get_title()

    def is_new_user_button_exist(self):
        return self.is_visible(self.NEW_USER_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.USER_NAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return ProfilePage(self.driver)




