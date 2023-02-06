from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_user_see_add_to_basket_button(browser):
    browser.implicitly_wait(20)
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-add-to-basket')
    assert button, 'Button to add item in basket not found'
