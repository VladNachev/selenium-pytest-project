from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Profile(BaseTest):

    def test_profile_page_title(self):
        self.loginPage = LoginPage(self.driver)
        profilePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = profilePage.get_profile_page_title(TestData.PROFILE_PAGE_TITLE)
        assert title == TestData.PROFILE_PAGE_TITLE


    def test_profile_header_and_account_name(self):
        self.loginPage = LoginPage(self.driver)
        profilePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = profilePage.get_header_value()
        assert header == TestData.PROFILE_PAGE_HEADER
        account_name = profilePage.get_account_name_value()
        assert account_name == TestData.PROFILE_PAGE_ACCOUNT_NANE



