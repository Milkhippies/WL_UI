from pages.api_page import ApiPage, ApiPageAsserts
from pages.application_page import ApplicationPage


class ApiSteps(ApiPage, ApplicationPage):
    def go_to_api(self):
        '''Переход на страницу ключей используя навбар'''
        appPage = ApplicationPage(self, "")
        appPage.nav_to_api()

    def create_key(self, key):
        '''Создание нового ключа'''
        pageMethods, pageAsserts = ApiPage(self, ""), ApiPageAsserts(self, "")
        ApiSteps.go_to_api(self)
        pageMethods.create_new_key(key)
        pageMethods.pass_2fa()
        pageAsserts.assert_creation_screen()

    def delete_key(self, keyTitle):
        '''Удаление существующего ключа'''
        pageMethods, pageAsserts = ApiPage(self, ""), ApiPageAsserts(self, "")
        pageMethods.refresh_page()
        ApiSteps.go_to_api(self)
        pageMethods.select_key_by_title(keyTitle)
        pageMethods.delete_exist_key()
        pageMethods.pass_2fa()
        pageAsserts.assert_key_deleting_popup()

    def check_key_params(self, key, keyTittle):
        '''Проверяем параметры ключа с именем keyTittle на соответствие параметрам ключа key'''
        pageMethods, pageAsserts = ApiPage(self, ""), ApiPageAsserts(self, "")
        pageMethods.refresh_page()
        ApiSteps.go_to_api(self)
        pageMethods.select_key_by_title(keyTittle)
        pageMethods.open_api_key_editor()
        pageAsserts.assert_api_key_params(key)

    def change_name(self, base, newParam):
        '''Меняем названия существующего ключа key на новый keyTittle'''
        pageMethods, pageAsserts = ApiPage(self, ""), ApiPageAsserts(self, "")
        pageMethods.refresh_page()
        ApiSteps.go_to_api(self)
        pageMethods.select_key_by_title(base)
        pageMethods.rename_api_key(newParam)
        pageAsserts.assert_api_key_name(newParam)

    def change_param(self, base, newParam):
        '''Меняем параметры ключа base на newParam'''
        pageMethods, pageAsserts = ApiPage(self, ""), ApiPageAsserts(self, "")
        pageMethods.refresh_page()
        ApiSteps.go_to_api(self)
        pageMethods.select_key_by_title(base)
        # сел тут



