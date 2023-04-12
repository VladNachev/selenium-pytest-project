from config.config import TestData
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from tests.test_base import BaseTest


class TestLogout(BaseTest):

    def test_account_logout(self):
        self.loginPage = LoginPage(self.driver)
        profilePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = profilePage.get_profile_page_title(TestData.PROFILE_PAGE_TITLE)
        assert title == TestData.PROFILE_PAGE_TITLE
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.do_logout()
        url = self.loginPage.validate_url()
        assert url == TestData.BASE_URL
