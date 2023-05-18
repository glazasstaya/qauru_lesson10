import pytest
import allure
from allure_commons.types import Severity

from selene import browser, have, by, be


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'glazasstaya')
@allure.feature('Issue в github')
@allure.story('Тест без шагов')
@allure.link("https://github.com", name="Testing")
def test_issue_find():
    browser.open("https://github.com")

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type('eroshenkoam/allure-example')
    browser.element('.header-search-input').press_enter()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#81')).should(be.visible)
