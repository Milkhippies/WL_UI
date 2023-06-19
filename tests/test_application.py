import allure
import pytest

from data.user_data import TestUserData
from data.api_keys import CreateKey, EditKey

from steps.auth_steps import AuthSteps
from steps.api_steps import ApiSteps

user = TestUserData.firstUser

unlimKey = CreateKey.UnlimKey
limitKey = CreateKey.LimitedKey
multiKey = CreateKey.MultiLimitedKey
anyKey = CreateKey.AnyKey

base = EditKey.BaseKey
changeLimit = EditKey.ChangeLimit
changeParam = EditKey.ChangeParams
changeName = EditKey.ChangeName


@pytest.mark.only_creation
@pytest.mark.parametrize('key', [unlimKey, limitKey, multiKey])
@pytest.mark.parametrize('execution_number', range(1))
@allure.title("Create new api-key")
def test_create_key(browser, execution_number, key):
    AuthSteps.auth_user(browser, user)
    ApiSteps.create_key(browser, key)


@pytest.mark.only_delete
@pytest.mark.parametrize('key', [unlimKey['Prefix'], limitKey['Prefix'], multiKey['Prefix']])
# @pytest.mark.parametrize('key', [anyKey['KeyName']])  # подчистить за собой все ключи
@pytest.mark.parametrize('execution_number', range(1))
@allure.title("Delete api-key by name prefix")
def test_delete_key(browser, execution_number, key):
    AuthSteps.auth_user(browser, user)
    ApiSteps.delete_key(browser, key)


@pytest.mark.rename
@pytest.mark.parametrize('keys', [[base, changeName]])
@pytest.mark.parametrize('execution_number', range(5))
@allure.title("Change name api-key")
def test_change_name(browser, execution_number, keys):
    AuthSteps.auth_user(browser, user)
    ApiSteps.create_key(browser, keys[0])
    ApiSteps.change_name(browser, keys[0]['KeyName'], keys[1])
    ApiSteps.delete_key(browser, keys[1]['KeyName'])


# @pytest.mark.parametrize('keys', [[base, changeParam]])
# @pytest.mark.parametrize('execution_number', range(5))
# @allure.title("Change name api-key")
# def test_change_param(browser, execution_number, keys):
#     AuthSteps.auth_user(browser, user)
#     ApiSteps.create_key(browser, keys[0])
#     ApiSteps.check_key_params(browser, keys[0], keys[0]['KeyName'])
    # ApiSteps.change_param(browser, keys[0]['KeyName'], keys[1])
    # ApiSteps.check_key_params(browser, keys[1], keys[1]['KeyName'])
    # ApiSteps.delete_key(browser, keys[1]['Prefix'])

