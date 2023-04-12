from config.config import TestData
from pages.login_page import LoginPage
from tests.test_base import BaseTest
from pages.profile_page import ProfilePage
from pages.book_page import BookPage

class TestBooks(BaseTest):
    def test_add_book(self):
        self.loginPage = LoginPage(self.driver)
        profilePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = profilePage.get_header_value()
        assert header == TestData.PROFILE_PAGE_HEADER
        self.profilePage = ProfilePage(self.driver)
        self.profilePage.click_bookstore_link()
        self.bookPage = BookPage(self.driver)
        header = self.bookPage.get_header_value()
        assert header == TestData.BOOK_PAGE_HEADER
        self.bookPage.max_win()
        self.bookPage.select_book()
        self.bookPage.add_book()

    def test_remove_books(self):
        self.loginPage = LoginPage(self.driver)
        profilePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = profilePage.get_header_value()
        assert header == TestData.PROFILE_PAGE_HEADER
        self.profilePage = ProfilePage(self.driver)
        self.bookPage = BookPage(self.driver)
        self.bookPage.max_win()
        self.bookPage.remove_all_books()
        self.bookPage.confirm_deletion()
