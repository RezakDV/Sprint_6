from selenium.webdriver.common.by import By

class FaqLocators:
    QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']")
