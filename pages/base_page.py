import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data import DEFAULT_TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def type(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    @allure.step("Получить текст из элемента: {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверка видимости элемента: {locator}")
    def visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Прокрутка к элементу: {locator}")
    def scroll_into_view(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        return elem

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        new_tab = [h for h in self.driver.window_handles if h != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_tab)
        self.wait.until(lambda d: d.current_url != "about:blank")

    @allure.step("Ожидание появления элемента: {locator}")
    def presence(self, locator):
        return EC.presence_of_element_located(locator)
    
    @allure.step("Явное ожидание DEFAULT_TIMEOUT секунд")
    def wait_default(self):
        WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(lambda _: True)
        
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    