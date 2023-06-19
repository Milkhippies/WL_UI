from pages.base_page import BasePage
from data.locators import AuthPageLocators


class AuthPage(BasePage):
    def fill_auth_form(self, data):
        self.select_visible_element(AuthPageLocators.Email).send_keys(data["email"])
        self.select_visible_element(AuthPageLocators.Password).send_keys(data["password"])
        self.select_visible_element(AuthPageLocators.EnterButton).click()
