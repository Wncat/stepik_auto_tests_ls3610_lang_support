import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: en, es, fr...')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    if user_language:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('\nStarting browser for test...')
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_language is required")
    yield browser
    print('\nQuitting browser for test...')
    browser.quit()
