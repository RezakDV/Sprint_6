import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import ORDER_DATASETS
from urls import MAIN_URL

@allure.feature("Заказ самоката")
@allure.story("Позитивный сценарий заказа с разными данными и точками входа")
@pytest.mark.parametrize("data", ORDER_DATASETS, ids=["top_button_dataset1", "bottom_button_dataset2"])
def test_order_scooter_positive_flow(driver, data):
    main = MainPage(driver)
    order = OrderPage(driver)

    with allure.step("Открыть точку входа на страницу заказа"):
        if data["entry_point"] == "top":
            main.click_order_top()
        else:
            main.click_order_bottom()

    order.fill_order_form(data)
    order.submit_and_confirm()

    with allure.step("Проверить, что заказ успешно создан"):
        assert order.order_created()

    with allure.step("Проверить переход по логотипу Самоката"):
        main.click_logo_scooter()
        assert driver.current_url == MAIN_URL

    with allure.step("Проверить переход по логотипу Яндекса"):
        main.click_logo_yandex()
        main.switch_to_new_tab()
        assert "dzen" in driver.current_url in driver.current_url
