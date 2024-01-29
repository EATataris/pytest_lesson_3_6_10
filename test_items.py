import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestBasketButton():

    def test_guest_should_see_basket_button(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")),
                                         message='NoSuchElementException - basket button not find')


if __name__ == "__main__":
    pytest.main()