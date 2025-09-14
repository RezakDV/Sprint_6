from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def click_order_top(self):
        self.click(MainPageLocators.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.scroll_into_view(MainPageLocators.ORDER_BOTTOM_BUTTON)
        self.click(MainPageLocators.ORDER_BOTTOM_BUTTON)

    def click_logo_scooter(self):
        self.click(BasePageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(BasePageLocators.LOGO_YANDEX)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_faq_question(self, index):
        locator = (FaqLocators.QUESTION[0], FaqLocators.QUESTION[1].format(index))
        self.scroll_to_element(locator)
        self.click(locator)

    def get_faq_answer_text(self, index: int) -> str:
        locator = (FaqLocators.ANSWER[0], FaqLocators.ANSWER[1].format(index))
        self.visible(locator)
        return self.driver.find_element(*locator).text
           
    def close_cookie_banner(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT)
            ).click()
        except TimeoutException:
            pass
