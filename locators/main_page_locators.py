from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[contains(@class, 'Button_Button')]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(@class, 'Button_Button')]")
    COOKIE_ACCEPT = (By.ID, "rcc-confirm-button")
