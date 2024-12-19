from selene import browser, by
from selene_in_action_py13.conditions import match


def test_github_issue_title():
    browser.open('https://github.com')
    browser.driver.fullscreen_window()

    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type('eroshenkoam/allure-example')
    browser.element('[id="query-builder-test"]').press_enter()

    browser.element('a[href="/eroshenkoam/allure-example"]').click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('С Новым Годом (2022)')).should(match.visible)
