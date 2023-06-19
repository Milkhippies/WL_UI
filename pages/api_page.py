from selenium.webdriver.common.by import By

from data.locators import ApiPageLocators
from pages.application_page import ApplicationPage


class ApiPage(ApplicationPage):
    def create_new_key(self, key):
        '''Метод создает новый ключ'''
        assert self.check_visible_element(ApiPageLocators.FuncNewKeyButton), "New key in right section not visible"
        assert self.try_click_element(ApiPageLocators.FuncNewKeyButton)

        assert self.check_visible_element(ApiPageLocators.APINameInput), "IP name input not visible"
        assert self.try_send_keys(ApiPageLocators.APINameInput, key['KeyName'])

        if key["Spot"]:
            assert self.check_visible_element(ApiPageLocators.SpotRadio), "Spot radio not visible"
            assert self.try_click_element(ApiPageLocators.SpotRadio)

        if key["Future"]:
            assert self.check_visible_element(ApiPageLocators.FutureRadio), "Future radio not visible"
            assert self.try_click_element(ApiPageLocators.FutureRadio)

        assert self.check_visible_element(ApiPageLocators.PrivateIPRadio), "Private IPs radio not visible"
        assert self.check_visible_element(ApiPageLocators.UnlimIPRadio), "Unlim IPs radio not visible"

        if key["Limit"]:
            self.select_visible_element(ApiPageLocators.PrivateIPRadio).click()

            for i in range(key['Multi']):
                assert self.check_visible_element(ApiPageLocators.IPAddButton), "Add IP button not visible"
                assert self.try_click_element(ApiPageLocators.IPAddButton)

                assert self.check_visible_element(ApiPageLocators.IPName), "Add IP name input not visible"
                assert self.try_send_keys(ApiPageLocators.IPName, key['IpName'][i])

                assert self.check_visible_element(ApiPageLocators.IPAddress), "Add IP address input not visible"
                assert self.try_send_keys(ApiPageLocators.IPAddress, key['IpAddr'][i])

                assert self.check_visible_element(ApiPageLocators.IPSave), "Save IP button not visible"
                assert self.try_click_element(ApiPageLocators.IPSave)

            assert self.check_visible_element(ApiPageLocators.LimitSaveSettingsButton), "Save key button not visible"
            assert self.try_click_element(ApiPageLocators.LimitSaveSettingsButton)

        else:
            assert self.check_visible_element(ApiPageLocators.UnlimSaveSettingsButton), "Save key button not visible"
            assert self.try_click_element(ApiPageLocators.UnlimSaveSettingsButton)

    def select_key_by_title(self, title):
        '''Метод находит ключ в спике по названию и кликает по нему'''
        locator = (By.XPATH, f'//div[contains(@title,"{title}")]')
        assert self.check_visible_element(locator), f"Title {title} not visible"
        assert self.try_click_element(locator)

    def open_api_key_editor(self):
        '''Метод находит кнопку "редактировать" в правой части страницы
        Условие: ключ должен быть выбран методом select_key_by_title'''
        assert self.check_visible_element(ApiPageLocators.FuncEditButton), "API name label not visible"
        assert self.try_click_element(ApiPageLocators.FuncEditButton)

    def delete_exist_key(self):
        '''Метод для удаления ключа с открытыми настройками'''
        assert self.check_visible_element(ApiPageLocators.DeleteKeyButton), "Delete button not visible"
        assert self.try_click_element(ApiPageLocators.DeleteKeyButton)

    def rename_api_key(self, key):
        '''Переименование ключа с уже открытыми настройками'''
        assert self.check_visible_element(ApiPageLocators.ExAPINameLabel), "API name label not visible"
        assert self.try_click_element(ApiPageLocators.ExAPINameLabel)

        assert self.send_backspace(ApiPageLocators.ExAPINameInput, 20), "Cant send backspace to API name input"

        assert self.check_visible_element(ApiPageLocators.ExAPINameInput), "IP name input not visible"
        assert self.try_send_keys(ApiPageLocators.ExAPINameInput, key['KeyName'])

        assert self.check_visible_element(ApiPageLocators.ExSaveButton), "Save button not visible"
        assert self.try_click_element(ApiPageLocators.ExSaveButton)

    # def change_key_param(self):

class ApiPageAsserts(ApplicationPage):
    def assert_key_deleting_popup(self):
        '''Метод ищет поп-ап о успешном удалении ключа на экране'''
        assert self.check_visible_element(ApiPageLocators.SuccessDeleting), "Delete pop-up not visible"
        # TODO: добавить сверку текста

    def assert_api_key_name(self, key):
        '''Проверка имени выбранного ключа'''
        assert self.check_visible_element(ApiPageLocators.ExAPINameLabel), "API name label not visible"
        assert self.check_text_to_be_presented_located(ApiPageLocators.ExAPINameLabel, key['KeyName'])
        name = self.select_visible_element(ApiPageLocators.ExAPINameLabel)
        assert name.text == key['KeyName'], f"Wrong name. Expect: {key['KeyName']}\n Found: {name.text}"

    def assert_api_key_params(self, key):
        '''Проверка чекбоксов в параметрах ключа'''
        assert self.check_checkbox(ApiPageLocators.ExSpot) == key['Spot'], f"Spot checkbox not equal"
        assert self.check_checkbox(ApiPageLocators.ExFuture) == key['Future'], "Future checkbox not equal"
        if key['Limit']:
            assert self.check_checkbox(ApiPageLocators.EXLimitIP) == True, "Limit ip checkbox not equal"
            assert self.check_checkbox(ApiPageLocators.ExUnlimIP) == False, "Unlim ip checkbox not equal"
        if not key['Limit']:
            assert self.check_checkbox(ApiPageLocators.EXLimitIP) == False, "Limit ip checkbox not equal"
            assert self.check_checkbox(ApiPageLocators.ExUnlimIP) == True, "Unlim ip checkbox not equal"

    def assert_creation_screen(self):
        '''Метод проверяет наличие полей и кликает на кнопку продолжения.
         Условие: должен быть открыт экран успешного создания ключа'''
        assert self.check_visible_element(ApiPageLocators.ApiKey, timeout=20), "Api key not found in confirm screen"
        assert self.check_visible_element(ApiPageLocators.SecretKey), "Secret key not found in confirm screen"
        assert self.check_visible_element(ApiPageLocators.OkButton), "Ok button not found in confirm screen"
        assert self.try_click_element(ApiPageLocators.OkButton)

