import allure
from selene import browser, by
from selene_in_action_py13.conditions import match


def test_github_issue_title():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_title('С Новым Годом (2022)')


@allure.step('Открываем главную страницу сайта GitHub')
def open_main_page():
    browser.open('https://github.com')



@allure.step('Ищем репозиторий {repository_name}')
def search_for_repository(repository_name):
    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type(repository_name)
    browser.element('[id="query-builder-test"]').press_enter()


@allure.step('Переходим на страницу репозитория')
def go_to_repository(repository_name):
    browser.element('a[href="/eroshenkoam/allure-example"]').click()


@allure.step('Открываем список доступных issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('В общем списке находим issue с названием {issue_title}')
def should_see_issue_with_title(issue_title):
    browser.element(by.partial_text(issue_title)).should(match.visible)
