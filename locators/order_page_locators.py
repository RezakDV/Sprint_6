from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_TODAY = (By.CLASS_NAME, "react-datepicker__day--today")
    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    CONFIRM_YES = (By.XPATH, "//div[contains(@class,'Order_Buttons')]/button[text()='Да']")
    MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")

    @classmethod
    def metro_option(cls, name: str):
        return (By.XPATH, f"//div[contains(@class,'select-search__option') and contains(text(), '{name}')]")

    @classmethod
    def rental_option(cls, duration: str):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{duration}']")
    