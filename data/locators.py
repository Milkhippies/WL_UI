from selenium.webdriver.common.by import By


class AppPage:
    CookieConfirm = (By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div/div[2]/button')


class NavBar:
    Logo = (By.CSS_SELECTOR, 'div:nth-child(1) > [href="/"]')
    Main = (By.LINK_TEXT, 'Главная')
    Spot = (By.LINK_TEXT, 'Спотовый кошелек')
    Transfers = (By.LINK_TEXT, 'Переводы')
    Leverages = (By.LINK_TEXT, 'Плечи')
    Api = (By.LINK_TEXT, 'API-ключи')


class AuthPageLocators:
    Email = (By.CSS_SELECTOR, '[name="email"]')
    Password = (By.CSS_SELECTOR, '[name="password"]')
    EnterButton = (By.CSS_SELECTOR, '#login-form > button > span')


class OTPFormLocators:
    Input = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/div[1]/div/div[1]/div[1]/input')
    Next = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/div[2]/div[1]/button')
    Cancel = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/div[2]/div[2]/button')
    CrossCalncel = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/div/button/span')
    ProgressBar = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/div[2]/div[1]/button/span[2]/div')
    WrongMethod = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/span')
    ErrorLabel = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/form/div[2]/div/div[2]/div/div[1]')


class ApiPageLocators:
    # Header section
    NewKeyButton = (By.CSS_SELECTOR, '#apiKeys > div > div:nth-child(2) > div > div > button')
    CopyApiKeyButton = (By.XPATH, '//*[@id="apiKeys"]/div[1]/div[2]/div/div[2]/button[1]/span')
    EditKeyButton = (By.XPATH, '//*[@id="apiKeys"]/div[1]/div[2]/div/div[2]/button[2]/span')
    DeleteKeyButton = (By.XPATH, '//*[@id="apiKeys"]/div[1]/div[2]/div/div[2]/button[3]/span')

    # Content section

    # Pop-ups
    SuccessDeleting = (By.XPATH, '//div[@class="alert_content"]')

    # Functional section
    FuncNewKeyButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/div/button')

    # ### Functional section with selected key
    FuncEditButton = (By.XPATH, '//span[text()="Редактировать"]')
    FuncDeleteButton = (By.XPATH, '//span[text()="Удалить"]')

    # ### Name setting
    KeyNameFilled = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[1]/span')
    KeyNameInput = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[1]/div/div/div[1]/div/input')
    KeyErrorLabel = (By.CSS_SELECTOR, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[1]/div/div/div[2]/div/div/div')

    # ### Create and edit right settings
    SpotRadio = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[2]/div[2]/div/div/div/div[1]/div')
    FutureRadio = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[2]/div[3]/div/div/div/div[1]/div')

    # ### Exist API key settings
    ExAPINameLabel = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/section/div/div/section/form/div[1]/span')
    ExAPINameInput = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/section/div/div/section/form/div[1]/div/div/div[1]/div/input')
    ExSaveButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/section/div/div/section/form/button/span')

    ExSpot = (By.CSS_SELECTOR, '#apiKeys > div.loadWidgetErrorShell > div > div > div > div > div.apiKeys_aside-wrapper.col.col-4 > aside > div > div > section > form > div:nth-child(2) > div:nth-child(3) > div > div > div > div.v-input__slot > div > input[type=checkbox]')
    ExFuture = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/section/section/form/div[2]/div[3]/div/div/div/div[1]/div/input')
    ExUnlimIP = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[3]/div/div/div/div/div[1]/div[1]/div/div/input')
    EXLimitIP = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[3]/div/div/div/div/div[2]/div/div/div/input')

    # ### New API key settings
    UnlimIPRadio = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[3]/div/div/div/div/div[1]/div[1]/div/div')
    PrivateIPRadio = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[3]/div/div/div/div/div[2]/div/div/div')
    IPAddButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/button/span')
    APINameInput = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[1]/div/div/div[1]/div/input')
    IPName = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[1]/div/div/div/div[1]/div/input')
    IPAddress = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[2]/div/div/div/div[1]/div/input')
    IPNameError = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[1]/div/div/div/div[2]/div/div/div')
    IPAddressError = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[2]/div/div/div/div[2]/div/div/div')
    IPSave = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[3]/button[1]')
    IPDelete = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/section/div/div/div/div[1]/section/form/div/div[3]/button[2]')

    # ### Right settings footer
    LimitSaveSettingsButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[5]/div[2]/button[1]/span')
    LimitCancelSettingsButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[5]/div[2]/button[2]/span')

    UnlimSaveSettingsButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/div[2]/button[1]/span')
    UnlimCancelSettingsButton = (By.XPATH, '//*[@id="apiKeys"]/div[2]/div/div/div/div/div[2]/aside/div/div/section/form/div[4]/div[2]/button[2]/span')

    # ### Creater frame
    OkButton = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/div[2]/button/span')
    ApiKey = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/section/div[1]/div[1]/span')
    SecretKey = (By.XPATH, '//*[@id="layoutWrapper"]/div[2]/div/section/div[2]/div[1]/span')

