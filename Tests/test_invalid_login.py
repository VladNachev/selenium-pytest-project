from config.config import TestData
from pages.login_page import LoginPage
from tests.test_base import BaseTest

class TestInvalidLogin(BaseTest):
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_invalid_username(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.INVALID_USER_NAME, TestData.PASSWORD)
        message = self.loginPage.get_message_text()
        assert message == TestData.LOGIN_FAILED_MESSAGE

    def test_invalid_password(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.INVALID_PASSWORD)
        message = self.loginPage.get_message_text()
        assert message == TestData.LOGIN_FAILED_MESSAGE
