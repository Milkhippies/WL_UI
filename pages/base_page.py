from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.settings import TestSettings


class BasePage:
    def __init__(self, browser, url, timeout=TestSettings.ECTimeout):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def try_assert_url(self, url, timeout=TestSettings.ECTimeout):
        try:
            flag = WebDriverWait(self.browser, timeout).until(
                EC.url_contains(url)), f"Fail, current url is {self.browser.current_url}"
            return flag
        except Exception:
            print(f"\nFail when try check url")
            return False

    def select_visible_element(self, locator, timeout=TestSettings.ECTimeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return self.browser.find_element(*locator)
        except Exception:
            print(f"\nElement {locator} not found")

    def check_visible_element(self, locator, timeout=TestSettings.ECTimeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except EC.NoSuchElementException:
            print(f"\nElement {locator} not found")
            return False
        except TimeoutException:
            return False
        except Exception:
            print(f"\nElement {locator} not visible")
            return False

    def try_send_keys(self, locator, text):
        try:
            self.select_visible_element(locator).send_keys(text)
            return True
        except Exception:
            print(f"\nError while send {text} to {locator}")
            return False

    def try_click_element(self, locator):
        try:
            self.select_visible_element(locator).click()
            return True
        except Exception:
            print(f"\nError while trying to click {locator}")
            return False

    def check_text_to_be_presented_located(self, locator, text, timeout=TestSettings.ECTimeout):
        try:
            flag = WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return flag
        except EC.NoSuchElementException:
            return False
        except TimeoutException:
            return False

    def send_backspace_once(self, locator):
        try:
            self.select_visible_element(locator).send_keys(Keys.BACK_SPACE)
            return True
        except Exception:
            # print(f"\nCant send backspace to {locator}")
            return False

    def send_backspace(self, locator, num):
        try:
            for i in range(num):
                self.send_backspace_once(locator)
            return True
        except Exception:
            return False

    def refresh_page(self):
        try:
            self.browser.execute_script("location.reload()")
            return True
        except Exception:
            return False

    def check_checkbox(self, locator):
        checkbox = self.browser.find_element(*locator)
        try:
            return checkbox.getAttribute('aria-checked').equals('true')
        except Exception as e:
            return e.__str__()
