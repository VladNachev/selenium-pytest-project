from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from config.config import TestData
from pages.base_page import BasePage

class BookPage(BasePage):

    """Locators"""
    HEADER = (By.XPATH, "//div[contains(@class, 'main-header') and text() = 'Book Store']")
    LATEST_BOOK = (By.CSS_SELECTOR, "span.mr-2")
    ADD_BOOK_BUTTON = (By.XPATH, "//button[contains(@class, 'btn btn-primary') and text() = 'Add To Your Collection']")
    REMOVE_BOOKS = (By.XPATH, "//button[contains(@class, 'btn btn-primary') and text() = 'Delete All Books']")
    CONFIRM_DELETION = (By.ID, "closeSmallModal-ok")

    """Constructor of the class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page actions"""
    def max_win(self):
        self.driver.maximize_window()
        return BookPage(self.driver)

    def select_book(self):
        self.do_click(self.LATEST_BOOK)
        return BookPage(self.driver)

    def add_book(self):
        self.do_click(self.ADD_BOOK_BUTTON)
        return BookPage(self.driver)

    def remove_all_books(self):
        self.do_click(self.REMOVE_BOOKS)
        return BookPage(self.driver)

    def confirm_deletion(self):
        self.do_click(self.CONFIRM_DELETION)
        return BookPage(self.driver)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)
