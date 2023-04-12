from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from config.config import TestData
from pages.base_page import BasePage
from pages.profile_page import ProfilePage


class LoginPage(BasePage):

    """Locators"""
    USER_NAME = (By.ID, "userName")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    NEW_USER_BUTTON = (By.ID, "newUser")
    MESSAGE_LOGIN_FAILED = (By.ID, "name")

    """Constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions"""

    def get_login_page_title(self, title):
        return self.get_title()

    def validate_url(self):
        return self.driver.current_url

    def is_new_user_button_exist(self):
        return self.is_visible(self.NEW_USER_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.USER_NAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return ProfilePage(self.driver)

    def get_message_text(self):
        if self.is_visible(self.MESSAGE_LOGIN_FAILED):
            return self.get_element_text(self.MESSAGE_LOGIN_FAILED)
