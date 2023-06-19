import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(save_fail_video):
    options = Options()
    print("\nstart chrome browser for test..")

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "113.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "videoFrameRate": 24,
            "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
            "logName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.log"
        }
    }

    browser = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities)  # в контейнере селенода
    # browser = webdriver.Chrome(options=options)    # для локального запуска

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='function')
def save_fail_video(request):
    yield
    if request.node.rep_call.failed:
        name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        path = "/opt/selenoid/video"
        file = f"{path}/{name}.mp4"

        print(f'Try to save video for {name}')

        time_to_wait = 10
        time_counter = 0
        while not os.path.exists(file):
            time.sleep(0.5)
            time_counter += 0.5
            if time_counter > time_to_wait: break

        try:
            allure.attach.file(source=f"{path}/{name}.mp4", name=name,
                               attachment_type=allure.attachment_type.MP4, extension=allure.attachment_type.MP4)
        except Exception:
            print(f"Error when trying to save video for {name}")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
