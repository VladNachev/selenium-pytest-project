from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ProfilePage(BasePage):

    HEADER = (By.XPATH, "//div[contains(text(),'Profile')]")
    ACCOUNT_NAME = (By.ID, "userName-value")
    LOGOUT_BUTTON = (By.ID, "submit")

    def __init__(self, driver):
        super().__init__(driver)

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


