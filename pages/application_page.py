from pages.base_page import BasePage
from data.link import ProjectLinks as Links
from data.locators import NavBar, AppPage, OTPFormLocators
from data.user_data import TestUserData
from external.utils.otp import get_otp_by_secret


class ApplicationPage(BasePage):
    def accept_cookie(self):
        assert self.check_visible_element(AppPage.CookieConfirm), "Confirm cookie button not found"
        assert self.try_click_element(AppPage.CookieConfirm)

    def nav_to_api(self):
        assert self.try_click_element(NavBar.Api)
        assert self.try_assert_url(Links.ApiKeys)

    def nav_to_spot(self):
        assert self.try_click_element(NavBar.Spot)
        assert self.try_assert_url(Links.SpotPage)

    def nav_to_leverages(self):
        assert self.try_click_element(NavBar.Leverages)
        assert self.try_assert_url(Links.LeveragesPage)

    def nav_to_transfers(self):
        assert self.try_click_element(NavBar.Transfers)
        assert self.try_assert_url(Links.TransfersPage)

    def nav_to_main(self):
        assert self.try_click_element(NavBar.Main)
        assert self.try_assert_url(Links.TradePage)

    def pass_2fa(self):
        '''Метод для прохождения двухфакторки'''
        if self.check_visible_element(OTPFormLocators.Input):
            # assert self.try_send_keys(OTPFormLocators.Input, "123321")    # для проверки повторного ввода
            assert self.try_send_keys(OTPFormLocators.Input, get_otp_by_secret(TestUserData.firstUser['secret']))
        if self.check_visible_element(OTPFormLocators.ErrorLabel):
            assert self.send_backspace(OTPFormLocators.Input, 6), f"Cant send backspace to input"
            assert self.try_send_keys(OTPFormLocators.Input, get_otp_by_secret(TestUserData.firstUser['secret']))
