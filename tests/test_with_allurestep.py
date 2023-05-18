import allure
import pytest
from allure_commons.types import Severity
from selene import browser, by, be

@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'glazasstaya')
@allure.feature('Issue в github')
@allure.story('Тест с шагами с with allure.step')
@allure.link("https://github.com", name="Testing")
def test_issue_find():
    with allure.step('Откраваю github'):
        browser.open("https://github.com")

    with allure.step('Ищу нужный репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').type('eroshenkoam/allure-example')
        browser.element('.header-search-input').press_enter()

    with allure.step('Перехожу в репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываю таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяю наличие #81'):
        browser.element(by.partial_text('#81')).should(be.visible)