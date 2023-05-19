import allure
import pytest
import allure_pytest
from selene import browser, have, by, be
from allure_commons.types import Severity

@allure.step('Откраваю github')
def githab_open():
    browser.open("https://github.com")

@allure.step('Ищу репозиторий {repo}')
def repo_search(repo):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repo)
    browser.element('.header-search-input').press_enter()

@allure.step('Перехожу в репозиторий {repo}')
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Открываю таб Issues')
def go_to_issues():
    browser.element('#issues-tab').click()

@allure.step('Проверяю наличие {number}')
def is_issue_visible(number):
    browser.element(by.partial_text(number)).should(be.visible)

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'glazasstaya')
@allure.feature('Issue в github')
@allure.story('Тест c декораторами allure.step')
@allure.link("https://github.com", name="Testing")
def test_decorator_steps(browser_settings):
    githab_open()
    repo_search('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    go_to_issues()
    is_issue_visible("#76")