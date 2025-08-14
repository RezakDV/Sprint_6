import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as L
from locators.base_page_locators import BasePageLocators as B
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    @allure.step("Заполнить форму заказа")
    def fill_order_form(self, data: dict):
        self.type(L.FIRST_NAME, data["first"])
        self.type(L.LAST_NAME, data["last"])
        self.type(L.ADDRESS, data["address"])

        self.click(L.METRO)
        self.type(L.METRO, data["metro"])
        self.driver.find_element(*L.METRO).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*L.METRO).send_keys(Keys.ENTER)

        self.type(L.PHONE, data["phone"])
        self.click(L.NEXT_BUTTON)

        self.click(L.DATE)
        self.click(L.DATE_TODAY)

        self.click(L.RENTAL_DROPDOWN)
        self.click(L.rental_option(data["rental"]))

        if data["color"] == "black":
            self.click(L.COLOR_BLACK)
        elif data["color"] == "grey":
            self.click(L.COLOR_GREY)

        if data["comment"]:
            self.type(L.COMMENT, data["comment"])

    @allure.step("Подтвердить заказ")
    def submit_and_confirm(self):
        self.wait.until(EC.element_to_be_clickable(L.ORDER_BUTTON))
        self.click(L.ORDER_BUTTON)

        self.wait.until(EC.element_to_be_clickable(L.CONFIRM_YES))
        self.click(L.CONFIRM_YES)
        self.wait_default()
        self.wait.until(EC.visibility_of_element_located(L.MODAL_TITLE))
        self.wait.until(EC.element_to_be_clickable(L.VIEW_STATUS_BUTTON))
        self.click(L.VIEW_STATUS_BUTTON)
        

    @allure.step("Проверить, что заказ создан")
    def order_created(self):
        self.wait.until(EC.visibility_of_element_located(B.LOGO_SCOOTER))
        self.wait.until(EC.visibility_of_element_located(B.LOGO_YANDEX))
        return True
    