from pages.auth_page import AuthPage
from pages.application_page import ApplicationPage
from data.link import ProjectLinks as Links


class AuthSteps(AuthPage, ApplicationPage):
    def auth_user(self, user):
        authPage = AuthPage(self, Links.PassportPage)
        authPage.open()
        authPage.fill_auth_form(user)
        authPage.try_assert_url(Links.TradePage)

        appPage = ApplicationPage(self, "")
        appPage.accept_cookie()
