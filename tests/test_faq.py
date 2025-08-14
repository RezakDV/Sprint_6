import allure
from pages.main_page import MainPage
from test_data import FAQ_EXPECTED

@allure.feature("FAQ")
@allure.story("Вопрос 0")
def test_faq_question_0(driver):
    page = MainPage(driver)
    page.click_faq_question(0)
    assert FAQ_EXPECTED[0] in page.get_faq_answer_text(0)

@allure.feature("FAQ")
@allure.story("Вопрос 1")
def test_faq_question_1(driver):
    page = MainPage(driver)
    page.click_faq_question(1)
    assert FAQ_EXPECTED[1] in page.get_faq_answer_text(1)

@allure.feature("FAQ")
@allure.story("Вопрос 2")
def test_faq_question_2(driver):
    page = MainPage(driver)
    page.click_faq_question(2)
    assert FAQ_EXPECTED[2] in page.get_faq_answer_text(2)

@allure.feature("FAQ")
@allure.story("Вопрос 3")
def test_faq_question_3(driver):
    page = MainPage(driver)
    page.click_faq_question(3)
    assert FAQ_EXPECTED[3] in page.get_faq_answer_text(3)

@allure.feature("FAQ")
@allure.story("Вопрос 4")
def test_faq_question_4(driver):
    page = MainPage(driver)
    page.click_faq_question(4)
    assert FAQ_EXPECTED[4] in page.get_faq_answer_text(4)

@allure.feature("FAQ")
@allure.story("Вопрос 5")
def test_faq_question_5(driver):
    page = MainPage(driver)
    page.click_faq_question(5)
    assert FAQ_EXPECTED[5] in page.get_faq_answer_text(5)

@allure.feature("FAQ")
@allure.story("Вопрос 6")
def test_faq_question_6(driver):
    page = MainPage(driver)
    page.click_faq_question(6)
    assert FAQ_EXPECTED[6] in page.get_faq_answer_text(6)

@allure.feature("FAQ")
@allure.story("Вопрос 7")
def test_faq_question_7(driver):
    page = MainPage(driver)
    page.click_faq_question(7)
    assert FAQ_EXPECTED[7] in page.get_faq_answer_text(7)
