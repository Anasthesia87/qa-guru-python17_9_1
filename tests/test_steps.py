import allure
from selene import browser, by
from selene_in_action_py13.conditions import match


def test_github_issue_title():
    with allure.step('Открываем главную страницу сайта GitHub'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий eroshenkoam/allure-example'):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type('eroshenkoam/allure-example')
        browser.element('[id="query-builder-test"]').press_enter()

    with allure.step('Переходим на страницу репозитория'):
        browser.element('a[href="/eroshenkoam/allure-example"]').click()

    with allure.step('Открываем список доступных issues'):
        browser.element('#issues-tab').click()

    with allure.step('В общем списке находим issue с названием "С Новым Годом (2022)"'):
        browser.element(by.partial_text('С Новым Годом (2022)')).should(match.visible)
