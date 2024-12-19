import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver.maximize_window()

    yield

    browser.quit()
