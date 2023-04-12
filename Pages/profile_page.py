from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProfilePage(BasePage):

    """Locators"""
    HEADER = (By.XPATH, "//div[contains(text(),'Profile')]")
    ACCOUNT_NAME = (By.ID, "userName-value")
    LOGOUT_BUTTON = (By.ID, "submit")
    BOOKSTORE_LINK = (By.XPATH, "//span[contains(@class, 'text') and text() = 'Book Store']")

    """Constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page actions"""
    def get_profile_page_title(self, title):
        return self.get_title(title)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)

    def do_logout(self):
        self.do_click(self.LOGOUT_BUTTON)
        return ProfilePage(self.driver)

    def click_bookstore_link(self):
        self.do_click(self.BOOKSTORE_LINK)
        return ProfilePage(self.driver)


