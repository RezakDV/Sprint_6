import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_text(driver, locator, text, timeout=10):
    WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

def attach_screenshot(driver, name="screenshot"):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
