import pytest
import allure
from pages.main_page import MainPage
from test_data import FAQ_EXPECTED

@allure.feature("FAQ")
@pytest.mark.parametrize("index, expected", FAQ_EXPECTED.items(), ids=[f"Question {i}" for i in FAQ_EXPECTED])
def test_faq_question(driver, index, expected):
    page = MainPage(driver)
    page.click_faq_question(index)
    assert expected == page.get_faq_answer_text(index)